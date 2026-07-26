import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * HaiBrutalistE01Pipeline — the 7-stage pipeline as an ENDLESS RING for
 * "What Is Brutalist?". Seven stages sit on a circle; `./art` is the single
 * entry point in the center; a pulse travels the ring forever, lighting each
 * stage as it passes; PUBLISH is the one node that outputs OUT (terracotta,
 * with an arrow leaving the loop). Beat B01 of hai-brutalist-what-is.
 */

export const haiBrutalistE01PipelineSchema = z.object({
  sparkLine: z.string().default('One command. One entry point. One sitting.'),
});
export type HaiBrutalistE01PipelineProps = z.infer<typeof haiBrutalistE01PipelineSchema>;

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));
const NODE_BG = '#FFF8F5';
const NODE_BORDER = '#F5C4B0';

const Spark: React.FC<{ size?: number }> = ({ size = 18 }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" style={{ flexShrink: 0 }}>
    {Array.from({ length: 8 }, (_, i) => (
      <line key={i} x1={12} y1={12}
        x2={12 + 10 * Math.cos((i * Math.PI) / 4 + 0.2)}
        y2={12 + 10 * Math.sin((i * Math.PI) / 4 + 0.2)}
        stroke={CLAUDE.SPARK} strokeWidth={3.2} strokeLinecap="round" />
    ))}
  </svg>
);

const STAGES = [
  { label: 'IDEAS', sub: 'scout' },
  { label: 'SCRIPT/\nBEATS', sub: 'script-writer' },
  { label: 'AUDIO', sub: 'gen_audio' },
  { label: 'VISUALS', sub: 'Manim/Remotion' },
  { label: 'ASSEMBLE', sub: 'run.sh' },
  { label: 'VARIANTS', sub: 'audience-preset' },
  { label: 'PUBLISH', sub: 'youtube-publisher' },
];
const N = STAGES.length;
const FOCAL = N - 1; // PUBLISH is the one that goes out
const START_DEG = -90; // IDEAS at top, flowing clockwise

export const HaiBrutalistE01Pipeline: React.FC<HaiBrutalistE01PipelineProps> = ({ sparkLine }) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();

  const cx = width / 2;
  const cy = height * 0.55;
  const R = height * 0.285;
  const NODE_W = 150;
  const NODE_H = 84;
  const degOf = (i: number) => START_DEG + (i * 360) / N;
  const radOf = (i: number) => (degOf(i) * Math.PI) / 180;

  const titleIn = spring({ frame, fps, config: { damping: 30, stiffness: 100, mass: 0.8 } });
  const ringIn = spring({ frame: frame - 8, fps, config: { damping: 26, stiffness: 80 } });
  const artIn = spring({ frame: frame - 95, fps, config: { damping: 22, stiffness: 90 } });
  const sparkIn = spring({ frame: frame - 120, fps, config: { damping: 28, stiffness: 100 } });

  // endless pulse around the ring
  const loopFrames = fps * 6;
  const pulseDeg = START_DEG + (frame / loopFrames) * 360;
  const pr = (pulseDeg * Math.PI) / 180;
  const dotX = cx + R * Math.cos(pr);
  const dotY = cy + R * Math.sin(pr);
  // comet trail dots
  const trail = [10, 20, 32, 46].map((lagDeg, k) => {
    const a = ((pulseDeg - lagDeg) * Math.PI) / 180;
    return { x: cx + R * Math.cos(a), y: cy + R * Math.sin(a), o: 0.28 - k * 0.06, r: 7 - k * 1.2 };
  });
  // angular activation of each node by the passing pulse
  const activation = (i: number) => {
    let d = Math.abs(((pulseDeg % 360) + 360) % 360 - (((degOf(i) % 360) + 360) % 360));
    d = Math.min(d, 360 - d);
    return clamp(1 - d / 26, 0, 1);
  };

  // PUBLISH out-arrow geometry (radially outward)
  const fr = radOf(FOCAL);
  const ux = Math.cos(fr), uy = Math.sin(fr);
  const fxN = cx + R * ux, fyN = cy + R * uy;
  const aStart = { x: fxN + ux * (NODE_W * 0.42), y: fyN + uy * (NODE_H * 0.42) };
  const aEnd = { x: fxN + ux * (NODE_W * 0.42 + 66), y: fyN + uy * (NODE_H * 0.42 + 66) };

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>

      {/* Eyebrow + title */}
      <div style={{
        position: 'absolute', left: width * 0.05, top: height * 0.09,
        fontFamily: SANS, fontSize: height * 0.033, fontWeight: 700,
        letterSpacing: 3, textTransform: 'uppercase' as const,
        color: CLAUDE.INK_SOFT, opacity: clamp(titleIn, 0, 1),
      }}>
        HUMANITARIANS AI · BRUTALIST SERIES
      </div>
      <div style={{
        position: 'absolute', left: width * 0.05, top: height * 0.14,
        fontFamily: SERIF, fontSize: height * 0.038, fontWeight: 600,
        color: CLAUDE.INK, letterSpacing: '-0.01em',
        opacity: clamp(titleIn, 0, 1), transform: `translateY(${(1 - titleIn) * 10}px)`,
      }}>
        The 7-Stage Pipeline
      </div>

      {/* Ring, flow chevrons, out-arrow, traveling pulse */}
      <svg width={width} height={height} style={{ position: 'absolute', inset: 0 }}>
        <circle cx={cx} cy={cy} r={R} fill="none" stroke={CLAUDE.BORDER}
          strokeWidth={2} strokeDasharray="2 9" opacity={clamp(ringIn, 0, 1) * 0.9} />

        {/* clockwise flow chevrons at the midpoint between adjacent stages */}
        {STAGES.map((_, i) => {
          const a = ((degOf(i) + 180 / N) * Math.PI) / 180;
          const mx = cx + R * Math.cos(a), my = cy + R * Math.sin(a);
          const tx = -Math.sin(a), ty = Math.cos(a); // clockwise tangent
          const nx = Math.cos(a), ny = Math.sin(a);  // radial (outward)
          const s = 8 * clamp(ringIn, 0, 1);
          const tip = { x: mx + tx * s, y: my + ty * s };
          const b1 = { x: mx - tx * s + nx * s * 0.85, y: my - ty * s + ny * s * 0.85 };
          const b2 = { x: mx - tx * s - nx * s * 0.85, y: my - ty * s - ny * s * 0.85 };
          return (
            <path key={i}
              d={`M ${b1.x} ${b1.y} L ${tip.x} ${tip.y} L ${b2.x} ${b2.y}`}
              stroke={CLAUDE.BORDER} strokeWidth={2.2} fill="none"
              strokeLinecap="round" strokeLinejoin="round" opacity={0.85} />
          );
        })}

        {/* comet trail + pulse dot */}
        {trail.map((t, k) => (
          <circle key={k} cx={t.x} cy={t.y} r={t.r} fill={CLAUDE.SPARK} opacity={t.o} />
        ))}
        <circle cx={dotX} cy={dotY} r={24} fill={CLAUDE.SPARK} opacity={0.16} />
        <circle cx={dotX} cy={dotY} r={9} fill={CLAUDE.SPARK} />

        {/* the one output: PUBLISH → out */}
        <line x1={aStart.x} y1={aStart.y} x2={aEnd.x} y2={aEnd.y}
          stroke={CLAUDE.SPARK} strokeWidth={3} strokeLinecap="round" opacity={clamp(artIn, 0, 1)} />
        <path
          d={`M ${aEnd.x - ux * 12 - uy * 7} ${aEnd.y - uy * 12 + ux * 7} L ${aEnd.x} ${aEnd.y} L ${aEnd.x - ux * 12 + uy * 7} ${aEnd.y - uy * 12 - ux * 7}`}
          stroke={CLAUDE.SPARK} strokeWidth={3} fill="none"
          strokeLinecap="round" strokeLinejoin="round" opacity={clamp(artIn, 0, 1)} />
      </svg>

      {/* Stage nodes on the ring */}
      {STAGES.map((stage, i) => {
        const x = cx + R * Math.cos(radOf(i));
        const y = cy + R * Math.sin(radOf(i));
        const nodeIn = spring({ frame: frame - (12 + i * 11), fps, config: { damping: 24, stiffness: 90, mass: 0.9 } });
        const isFocal = i === FOCAL;
        const act = activation(i);
        const glow = isFocal ? 1 : act;
        const scale = clamp(nodeIn, 0, 1) * (1 + 0.05 * glow);
        return (
          <div key={i} style={{
            position: 'absolute',
            left: x - NODE_W / 2, top: y - NODE_H / 2,
            width: NODE_W, height: NODE_H,
            background: isFocal ? CLAUDE.INK : NODE_BG,
            border: `2px solid ${isFocal ? CLAUDE.INK : NODE_BORDER}`,
            borderRadius: 14,
            boxShadow: isFocal
              ? `0 10px 34px ${CLAUDE.INK}55`
              : `0 4px 16px rgba(217,119,87,${0.10 + 0.22 * act})`,
            display: 'flex', flexDirection: 'column',
            alignItems: 'center', justifyContent: 'center', gap: 4,
            opacity: clamp(nodeIn, 0, 1),
            transform: `scale(${scale})`,
          }}>
            <div style={{
              fontFamily: SANS, fontSize: Math.round(height * 0.033), fontWeight: 700,
              letterSpacing: 1.4, textTransform: 'uppercase' as const,
              color: isFocal ? '#FFFFFF' : CLAUDE.INK,
              textAlign: 'center', whiteSpace: 'pre-line', lineHeight: 1.25,
            }}>
              {stage.label}
            </div>
            <div style={{
              fontFamily: SANS, fontSize: Math.round(height * 0.033),
              color: isFocal ? 'rgba(255,255,255,0.85)' : CLAUDE.INK_SOFT,
              textAlign: 'center',
            }}>
              {stage.sub}
            </div>
          </div>
        );
      })}

      {/* ./art — the single entry point, in the center of the loop */}
      <div style={{
        position: 'absolute', left: cx, top: cy,
        transform: `translate(-50%,-50%) scale(${clamp(artIn, 0, 1)})`,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6,
        opacity: clamp(artIn, 0, 1),
      }}>
        <div style={{
          background: CLAUDE.INK, borderRadius: 22, padding: '8px 26px',
          fontFamily: SANS, fontWeight: 700, fontSize: height * 0.02,
          color: '#FFFFFF', letterSpacing: 2,
          boxShadow: `0 8px 28px ${CLAUDE.INK}44`,
        }}>
          ./art
        </div>
        <div style={{
          fontFamily: SANS, fontSize: Math.round(height * 0.033), fontWeight: 600,
          letterSpacing: 2, textTransform: 'uppercase' as const, color: CLAUDE.INK_SOFT,
        }}>
          one entry point
        </div>
      </div>

      {/* Spark line */}
      <div style={{
        position: 'absolute', left: 0, right: 0, bottom: height * 0.06,
        display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 10,
        opacity: clamp(sparkIn, 0, 1),
      }}>
        <Spark size={height * 0.040} />
        <span style={{ fontFamily: SERIF, fontSize: height * 0.040, fontStyle: 'italic', color: CLAUDE.INK }}>
          {sparkLine}
        </span>
      </div>
    </AbsoluteFill>
  );
};
