import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * ClockWheel — sixty-minute pie clock for claude-liam-one-hour-on-cowork.
 *
 * WHAT: Six wedges (5+15+10+10+10+10 min) in infographic clock order.
 *       Three fill states per wedge: unfilled (muted) / filled (ink) / active (terracotta sweep).
 * WHEN: Every act transition, the intro overview, and the verdict.
 * PROPS:
 *   filledThrough  0–6  wedges 1..N shown solid warm ink (completed)
 *   activeWedge    0–6  0=none; 1–6=hand sweeps this wedge in terracotta
 *   label          serif text below the clock
 *   folderLabel    footer chip
 * ADAPTED FROM: CoworkHourClock.tsx — wedge ORDER corrected to match Hassid's infographic
 *               (clockwise from 12: 5 / 15 / 10 / 10 / 10 / 10 min).
 */

export const clockWheelSchema = z.object({
  filledThrough: z.number().int().min(0).max(6).default(0),
  activeWedge:   z.number().int().min(0).max(6).default(0),
  label:         z.string().default('The sixty-minute plan.'),
  folderLabel:   z.string().default('@NikBearBrown'),
});
export type ClockWheelProps = z.infer<typeof clockWheelSchema>;

// Wedges in Hassid's infographic clock order (clockwise from 12 o'clock):
const WEDGE_DEFS = [
  { name: 'Run Your First Task',       minutes: 5,  shortMin: '5 min'  },
  { name: 'Write Your Files',          minutes: 15, shortMin: '15 min' },
  { name: 'Create a Cowork Project',   minutes: 10, shortMin: '10 min' },
  { name: 'Build Your Folder',         minutes: 10, shortMin: '10 min' },
  { name: 'Set Global Instructions',   minutes: 10, shortMin: '10 min' },
  { name: 'Plugins & Schedule',        minutes: 10, shortMin: '10 min' },
] as const;

const TOTAL_MIN = 60;
const GAP_DEG   = 1.8; // gap between wedges in degrees

// Palette
const UNFILLED = '#E5E2D9';
const FILLED   = CLAUDE.INK;
const ACTIVE   = CLAUDE.SPARK;
const PAGE     = CLAUDE.PAGE;

function toRad(deg: number) { return (deg - 90) * (Math.PI / 180); }

function xyAt(cx: number, cy: number, r: number, deg: number) {
  const a = toRad(deg);
  return { x: cx + r * Math.cos(a), y: cy + r * Math.sin(a) };
}

function arcPath(
  cx: number, cy: number, r: number,
  startDeg: number, endDeg: number,
  innerR = 0,
): string {
  const s = startDeg + GAP_DEG / 2;
  const e = endDeg   - GAP_DEG / 2;
  if (e <= s) return '';
  const large = (e - s) > 180 ? 1 : 0;

  if (innerR > 0) {
    // donut wedge
    const p1 = xyAt(cx, cy, r, s);
    const p2 = xyAt(cx, cy, r, e);
    const p3 = xyAt(cx, cy, innerR, e);
    const p4 = xyAt(cx, cy, innerR, s);
    return [
      `M ${p1.x} ${p1.y}`,
      `A ${r} ${r} 0 ${large} 1 ${p2.x} ${p2.y}`,
      `L ${p3.x} ${p3.y}`,
      `A ${innerR} ${innerR} 0 ${large} 0 ${p4.x} ${p4.y}`,
      'Z',
    ].join(' ');
  }

  // full pie wedge
  const p1 = xyAt(cx, cy, r, s);
  const p2 = xyAt(cx, cy, r, e);
  return [
    `M ${cx} ${cy}`,
    `L ${p1.x} ${p1.y}`,
    `A ${r} ${r} 0 ${large} 1 ${p2.x} ${p2.y}`,
    'Z',
  ].join(' ');
}

// Build cumulative angles for all wedges
function buildAngles() {
  const out: { start: number; end: number }[] = [];
  let cursor = 0;
  for (const w of WEDGE_DEFS) {
    const span = (w.minutes / TOTAL_MIN) * 360;
    out.push({ start: cursor, end: cursor + span });
    cursor += span;
  }
  return out;
}
const ANGLES = buildAngles();

export const ClockWheel: React.FC<ClockWheelProps> = ({
  filledThrough, activeWedge, label, folderLabel,
}) => {
  const frame = useCurrentFrame();
  const { fps, width: vw, height: vh } = useVideoConfig();

  // Global clock fade-in
  const clockIn  = spring({ frame,        fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });
  // Active wedge sweep progress (0 → 1)
  const sweepPct = spring({ frame,        fps, config: { damping: 26, stiffness: 70,  mass: 1.2 } });
  // Label rise
  const labelIn  = spring({ frame: frame - 8, fps, config: { damping: 28, stiffness: 140, mass: 0.8 } });

  const CX = vw / 2;
  const CY = vh * 0.46;
  const R      = Math.min(vw, vh) * 0.285;
  const INNER  = R * 0.32;   // donut hole radius

  const activeIdx = activeWedge - 1; // 0-based, or -1 when no active wedge

  return (
    <AbsoluteFill style={{ backgroundColor: PAGE, overflow: 'hidden' }}>
      <svg
        width={vw} height={vh}
        viewBox={`0 0 ${vw} ${vh}`}
        style={{ position: 'absolute', top: 0, left: 0 }}
      >
        {WEDGE_DEFS.map((wedge, i) => {
          const { start, end } = ANGLES[i];
          const isFilled = i < filledThrough;
          const isActive = i === activeIdx;
          const midAngle = (start + end) / 2;

          // Determine fill color for static wedges
          const staticFill = isFilled ? FILLED : UNFILLED;

          // Inside-wedge label position
          const labelR = R * 0.68;
          const lp     = xyAt(CX, CY, labelR, midAngle);
          const minFontSize = Math.max(13, R * 0.072);

          // Outer name label
          const outerR = R * 1.46;
          const op     = xyAt(CX, CY, outerR, midAngle);
          const nameFontSize = Math.max(17, R * 0.09);

          if (isActive) {
            // Animated sweep wedge
            const sweepEnd = start + sweepPct * (end - start);
            const showLabel = sweepPct > 0.7;

            return (
              <g key={i} style={{ opacity: clockIn }}>
                {/* Swept fill (terracotta) */}
                {sweepPct > 0.01 && (
                  <path
                    d={arcPath(CX, CY, R, start, sweepEnd, INNER)}
                    fill={ACTIVE}
                  />
                )}
                {/* Unfilled remainder */}
                <path
                  d={arcPath(CX, CY, R, Math.max(start, sweepEnd), end, INNER)}
                  fill={UNFILLED}
                  opacity={0.6}
                />
                {/* Clock hand — thin terracotta line at sweep leading edge */}
                {sweepPct > 0.01 && (() => {
                  const hp = xyAt(CX, CY, R * 0.96, sweepEnd);
                  const hInner = xyAt(CX, CY, INNER * 1.05, sweepEnd);
                  return (
                    <line
                      x1={hInner.x} y1={hInner.y}
                      x2={hp.x}     y2={hp.y}
                      stroke={PAGE} strokeWidth={2.5} strokeLinecap="round"
                    />
                  );
                })()}
                {/* Minute label inside wedge */}
                <text
                  x={lp.x} y={lp.y}
                  textAnchor="middle" dominantBaseline="middle"
                  fill="#FFFFFF" fontSize={minFontSize}
                  fontFamily={CLAUDE_FONT.ui} fontWeight={700}
                  style={{ opacity: sweepPct }}
                >
                  {wedge.shortMin}
                </text>
                {/* Outer name — appears after sweep */}
                {showLabel && (
                  <text
                    x={op.x} y={op.y}
                    textAnchor="middle" dominantBaseline="middle"
                    fill={ACTIVE} fontSize={nameFontSize}
                    fontFamily={CLAUDE_FONT.ui} fontWeight={700}
                    style={{ opacity: interpolate(sweepPct, [0.7, 1], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }) }}
                  >
                    {wedge.name}
                  </text>
                )}
              </g>
            );
          }

          // Non-active wedge (filled or unfilled)
          return (
            <g key={i} style={{ opacity: clockIn }}>
              <path
                d={arcPath(CX, CY, R, start, end, INNER)}
                fill={staticFill}
                opacity={isFilled ? 1 : 0.55}
              />
              {/* Minute label */}
              <text
                x={lp.x} y={lp.y}
                textAnchor="middle" dominantBaseline="middle"
                fill={isFilled ? PAGE : CLAUDE.INK_SOFT}
                fontSize={minFontSize}
                fontFamily={CLAUDE_FONT.ui}
                fontWeight={isFilled ? 600 : 400}
                style={{ opacity: isFilled ? 0.85 : 0.6 }}
              >
                {wedge.shortMin}
              </text>
              {/* Outer name — show on overview (activeWedge=0) or filled */}
              {(activeWedge === 0) && (
                <text
                  x={op.x} y={op.y}
                  textAnchor="middle" dominantBaseline="middle"
                  fill={isFilled ? CLAUDE.INK : CLAUDE.INK_SOFT}
                  fontSize={nameFontSize * 0.88}
                  fontFamily={CLAUDE_FONT.ui}
                  fontWeight={isFilled ? 600 : 400}
                  style={{ opacity: isFilled ? 0.8 : 0.45 }}
                >
                  {wedge.name}
                </text>
              )}
            </g>
          );
        })}

        {/* Center text: "60 min" */}
        <text
          x={CX} y={CY - R * 0.1}
          textAnchor="middle" dominantBaseline="middle"
          fill={CLAUDE.INK} fontSize={R * 0.25}
          fontFamily={CLAUDE_FONT.serif} fontWeight={700}
          style={{ opacity: clockIn }}
        >
          60
        </text>
        <text
          x={CX} y={CY + R * 0.13}
          textAnchor="middle" dominantBaseline="middle"
          fill={CLAUDE.INK_SOFT} fontSize={R * 0.1}
          fontFamily={CLAUDE_FONT.ui}
          style={{ opacity: clockIn * 0.75 }}
        >
          min
        </text>

        {/* Terracotta rule line — brand signature */}
        <rect
          x={vw * 0.08} y={vh * 0.93}
          width={vw * 0.07} height={2}
          fill={CLAUDE.SPARK}
          style={{ opacity: clockIn }}
        />
      </svg>

      {/* Serif label below clock */}
      <div style={{
        position: 'absolute',
        left: 0, right: 0,
        bottom: vh * 0.085,
        textAlign: 'center',
        fontFamily: CLAUDE_FONT.serif,
        fontSize: Math.max(20, vh * 0.036),
        fontWeight: 600,
        color: CLAUDE.INK,
        letterSpacing: '-0.01em',
        opacity: labelIn,
        transform: `translateY(${(1 - labelIn) * 12}px)`,
        padding: '0 12%',
      }}>
        {label}
      </div>

      {/* @NikBearBrown watermark — lower-right, low opacity */}
      <div style={{
        position: 'absolute',
        right: vw * 0.04,
        bottom: vh * 0.03,
        fontFamily: CLAUDE_FONT.ui,
        fontSize: Math.max(12, vh * 0.015),
        fontWeight: 600,
        color: CLAUDE.INK_SOFT,
        opacity: 0.2,
        letterSpacing: 1,
      }}>
        {folderLabel}
      </div>
    </AbsoluteFill>
  );
};
