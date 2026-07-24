/**
 * VercelRefactorIllu.tsx — reel-local compositions for claude-liam-vercel-refactor.
 *
 * Wraps structural illustration components (ChipGrid, LayerStack, SourceFlow,
 * PredictCard from illustrations/structural.tsx) with reel-specific zod schemas,
 * plus bespoke components for beats the structural library doesn't cover.
 *
 * All compositions are 1280×720, 30fps. Duration is audio-driven (compile.py
 * conforms each composition to actual_duration_s at render time).
 *
 * Composition IDs (must match shot.remotion.pattern in beat_sheet.json):
 *   Structural wrappers:   VRChipGrid | VRLayerStack | VRSourceFlow | VRPredictCard
 *   Bespoke beats:         VRSegmentCard | VRBoundaryShift | VRGateCard |
 *                          VRRenameCard | VRTwoColCard | VRChecklistCard |
 *                          VRLadderCard | VRCycleCard | VRDangerCard
 */
import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from './tokens/claude';
import { IlluStage, clamp, remap, ease, useP } from './illustrations/kit';
import { ChipGrid, LayerStack, SourceFlow, PredictCard } from './illustrations/structural';

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;
const MONO  = CLAUDE_FONT.mono;

const sp = (frame: number, fps: number, delay = 0) =>
  clamp(spring({ frame: frame - delay, fps, config: { damping: 28, stiffness: 125, mass: 0.88 } }), 0, 1);

const SparkRow: React.FC<{ text: string; opacity: number; height: number }> = ({ text, opacity, height }) => (
  <div style={{ position: 'absolute', bottom: height * 0.07, left: 0, right: 0,
    display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 12, opacity }}>
    <svg width={22} height={22} viewBox="0 0 24 24">
      {Array.from({ length: 8 }, (_, i) => (
        <line key={i} x1={12} y1={12}
          x2={12 + 10 * Math.cos((i * Math.PI) / 4 + 0.2)}
          y2={12 + 10 * Math.sin((i * Math.PI) / 4 + 0.2)}
          stroke={CLAUDE.SPARK} strokeWidth={3.2} strokeLinecap="round" />
      ))}
    </svg>
    <span style={{ fontFamily: SERIF, fontSize: 22, fontStyle: 'italic', color: CLAUDE.INK }}>{text}</span>
  </div>
);

// ── Structural wrappers ──────────────────────────────────────────────────────

export const vrChipGridSchema = z.object({
  sparkLine: z.string().default('capabilities.'),
  items: z.array(z.string()).default([]),
  cols: z.number().optional(),
  caption: z.string().optional(),
});
export type VRChipGridProps = z.infer<typeof vrChipGridSchema>;
export const VRChipGrid: React.FC<VRChipGridProps> = (p) => (
  <IlluStage spark={p.sparkLine}>
    <ChipGrid items={p.items} cols={p.cols} caption={p.caption} />
  </IlluStage>
);

export const vrLayerStackSchema = z.object({
  sparkLine: z.string().default('layers.'),
  layers: z.array(z.object({
    title: z.string(),
    sub:   z.string(),
    accent: z.boolean().optional(),
  })).default([]),
  caption: z.string().optional(),
  top: z.number().optional(),
});
export type VRLayerStackProps = z.infer<typeof vrLayerStackSchema>;
export const VRLayerStack: React.FC<VRLayerStackProps> = (p) => (
  <IlluStage spark={p.sparkLine}>
    <LayerStack layers={p.layers} caption={p.caption} top={p.top} />
  </IlluStage>
);

export const vrSourceFlowSchema = z.object({
  sparkLine: z.string().default('flow.'),
  sourceLabel: z.string().default('source'),
  feeds: z.array(z.object({ label: z.string(), tint: z.string().optional() })).default([]),
  destApp: z.string().default('destination'),
  destTitle: z.string().default(''),
  arcCaption: z.string().optional(),
  settleLine: z.string().optional(),
  rackRows: z.number().optional(),
});
export type VRSourceFlowProps = z.infer<typeof vrSourceFlowSchema>;
export const VRSourceFlow: React.FC<VRSourceFlowProps> = (p) => (
  <IlluStage spark={p.sparkLine}>
    <SourceFlow
      sourceLabel={p.sourceLabel} feeds={p.feeds}
      destApp={p.destApp} destTitle={p.destTitle}
      arcCaption={p.arcCaption} settleLine={p.settleLine} rackRows={p.rackRows} />
  </IlluStage>
);

export const vrPredictCardSchema = z.object({
  sparkLine: z.string().default('predict first.'),
  question: z.string().default(''),
  commit:   z.string().default(''),
});
export type VRPredictCardProps = z.infer<typeof vrPredictCardSchema>;
export const VRPredictCard: React.FC<VRPredictCardProps> = (p) => (
  <IlluStage spark={p.sparkLine}>
    <PredictCard question={p.question} commit={p.commit} />
  </IlluStage>
);

// ── VRSegmentCard — Act announcement card ───────────────────────────────────
// B04 (Act II — The Map), B10 (Act III — The Gate).

export const vrSegmentCardSchema = z.object({
  act:       z.string().default('II'),
  title:     z.string().default('Act Title'),
  sub:       z.string().optional(),
  sparkLine: z.string().default('act.'),
});
export type VRSegmentCardProps = z.infer<typeof vrSegmentCardSchema>;

export const VRSegmentCard: React.FC<VRSegmentCardProps> = ({ act, title, sub, sparkLine }) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const eyeIn   = sp(frame, fps, 0);
  const lineIn  = sp(frame, fps, 4);
  const titleIn = sp(frame, fps, 8);
  const subIn   = sp(frame, fps, 16);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, display: 'flex',
      flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
      <div style={{ fontFamily: MONO, fontSize: 16, letterSpacing: 5, color: CLAUDE.SPARK,
        textTransform: 'uppercase', opacity: eyeIn, marginBottom: 10 }}>
        ACT {act}
      </div>
      <div style={{ width: 80 * lineIn, height: 2, background: CLAUDE.SPARK, borderRadius: 2,
        marginBottom: 22, opacity: lineIn }} />
      <div style={{ fontFamily: SERIF, fontSize: 72, color: CLAUDE.INK, textAlign: 'center',
        lineHeight: 1.1, opacity: titleIn, transform: `translateY(${(1 - titleIn) * 18}px)`,
        maxWidth: width * 0.78 }}>
        {title}
      </div>
      {sub && (
        <div style={{ fontFamily: SANS, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 22,
          textAlign: 'center', opacity: subIn, transform: `translateY(${(1 - subIn) * 10}px)`,
          maxWidth: width * 0.62 }}>
          {sub}
        </div>
      )}
      <SparkRow text={sparkLine} opacity={subIn} height={height} />
    </AbsoluteFill>
  );
};

// ── VRBoundaryShift — before/after the boundary moved ───────────────────────
// B03. Two-panel: old rule (greyed) vs new rule (terracotta border).

export const vrBoundaryShiftSchema = z.object({
  oldLabel: z.string().default('old boundary'),
  oldItems: z.array(z.string()).default([]),
  newLabel: z.string().default('new boundary'),
  newItems: z.array(z.string()).default([]),
  sparkLine: z.string().default('the boundary moved.'),
});
export type VRBoundaryShiftProps = z.infer<typeof vrBoundaryShiftSchema>;

export const VRBoundaryShift: React.FC<VRBoundaryShiftProps> = (
  { oldLabel, oldItems, newLabel, newItems, sparkLine }
) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const leftIn  = sp(frame, fps, 0);
  const arrowIn = sp(frame, fps, 12);
  const rightIn = sp(frame, fps, 22);
  const PW = width * 0.37, PH = height * 0.54, PT = height * 0.19;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <div style={{ position: 'absolute', top: height * 0.08, left: 0, right: 0,
        textAlign: 'center', fontFamily: MONO, fontSize: 16, letterSpacing: 4,
        color: CLAUDE.INK_SOFT, textTransform: 'uppercase', opacity: leftIn }}>
        CLAUDE CODE HAS A BROWSER NOW
      </div>
      {/* Left panel — before */}
      <div style={{ position: 'absolute', left: width * 0.06, top: PT, width: PW, height: PH,
        background: CLAUDE.FOOTER, border: `1px solid ${CLAUDE.BORDER}`, borderRadius: 16,
        padding: '26px 28px', opacity: leftIn, transform: `translateX(${(1 - leftIn) * -20}px)` }}>
        <div style={{ fontFamily: MONO, fontSize: 16, letterSpacing: 3, color: CLAUDE.INK_SOFT,
          textTransform: 'uppercase', marginBottom: 10 }}>BEFORE</div>
        <div style={{ fontFamily: SERIF, fontSize: 28, color: CLAUDE.INK, marginBottom: 18 }}>{oldLabel}</div>
        {oldItems.map((it, i) => (
          <div key={i} style={{ fontFamily: SANS, fontSize: 19, color: CLAUDE.INK_SOFT,
            marginBottom: 10, display: 'flex', alignItems: 'center', gap: 10 }}>
            <div style={{ width: 8, height: 8, borderRadius: 4, background: CLAUDE.BORDER, flexShrink: 0 }} />
            {it}
          </div>
        ))}
      </div>
      {/* Arrow */}
      <svg width={width} height={height} style={{ position: 'absolute', inset: 0, pointerEvents: 'none' }}>
        <path d={`M ${width * 0.465} ${height * 0.46} L ${width * 0.535} ${height * 0.46}`}
          stroke={CLAUDE.SPARK} strokeWidth={4} strokeLinecap="round"
          strokeDasharray={`${width * 0.07}`} strokeDashoffset={`${width * 0.07 * (1 - arrowIn)}`} />
        <polygon
          points={`${width * 0.535},${height * 0.435} ${width * 0.56},${height * 0.46} ${width * 0.535},${height * 0.485}`}
          fill={CLAUDE.SPARK} opacity={arrowIn} />
      </svg>
      {/* Right panel — now */}
      <div style={{ position: 'absolute', right: width * 0.06, top: PT, width: PW, height: PH,
        background: CLAUDE.CARD, border: `2px solid ${CLAUDE.SPARK}`, borderRadius: 16,
        padding: '26px 28px', opacity: rightIn, transform: `translateX(${(1 - rightIn) * 20}px)` }}>
        <div style={{ fontFamily: MONO, fontSize: 16, letterSpacing: 3, color: CLAUDE.SPARK,
          textTransform: 'uppercase', marginBottom: 10 }}>NOW</div>
        <div style={{ fontFamily: SERIF, fontSize: 28, color: CLAUDE.INK, marginBottom: 18 }}>{newLabel}</div>
        {newItems.map((it, i) => (
          <div key={i} style={{ fontFamily: SANS, fontSize: 19, color: CLAUDE.INK,
            marginBottom: 10, display: 'flex', alignItems: 'center', gap: 10 }}>
            <div style={{ width: 8, height: 8, borderRadius: 4, background: CLAUDE.SPARK, flexShrink: 0 }} />
            {it}
          </div>
        ))}
      </div>
      <SparkRow text={sparkLine} opacity={rightIn} height={height} />
    </AbsoluteFill>
  );
};

// ── VRGateCard — horizontal explore | gate | edit layout ────────────────────
// B05 (plan mode gate), B14 (deploy checks before promote).

export const vrGateCardSchema = z.object({
  leftLabel:  z.string().default('explore'),
  leftItems:  z.array(z.string()).default([]),
  gateLabel:  z.string().default('human approval'),
  rightLabel: z.string().default('edit'),
  rightItems: z.array(z.string()).default([]),
  sparkLine:  z.string().default('gate first.'),
});
export type VRGateCardProps = z.infer<typeof vrGateCardSchema>;

export const VRGateCard: React.FC<VRGateCardProps> = (
  { leftLabel, leftItems, gateLabel, rightLabel, rightItems, sparkLine }
) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const leftIn  = sp(frame, fps, 0);
  const gateIn  = sp(frame, fps, 10);
  const rightIn = sp(frame, fps, 20);
  const ZW = width * 0.31, ZH = height * 0.52, ZT = height * 0.21;
  const GX = width * 0.5;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      {/* Left zone — explore */}
      <div style={{ position: 'absolute', left: width * 0.06, top: ZT, width: ZW, height: ZH,
        background: CLAUDE.FOOTER, border: `1px solid ${CLAUDE.BORDER}`, borderRadius: 14,
        padding: '20px 22px', opacity: leftIn, transform: `translateX(${(1 - leftIn) * -16}px)` }}>
        <div style={{ fontFamily: MONO, fontSize: 16, letterSpacing: 3, color: CLAUDE.INK_SOFT,
          textTransform: 'uppercase', marginBottom: 10 }}>{leftLabel}</div>
        {leftItems.map((it, i) => (
          <div key={i} style={{ fontFamily: SANS, fontSize: 18, color: CLAUDE.INK_SOFT,
            marginBottom: 8, display: 'flex', alignItems: 'center', gap: 8 }}>
            <div style={{ width: 7, height: 7, borderRadius: 4, background: CLAUDE.INK_SOFT, flexShrink: 0 }} />
            {it}
          </div>
        ))}
      </div>
      {/* Gate post */}
      <div style={{ position: 'absolute', left: GX - 4, top: ZT - 28, width: 8, height: ZH + 56,
        background: CLAUDE.SPARK, borderRadius: 4, opacity: gateIn,
        transform: `scaleY(${gateIn})`, transformOrigin: 'top' }} />
      <div style={{ position: 'absolute', left: GX - 90, top: ZT - 62, width: 180,
        textAlign: 'center', fontFamily: SERIF, fontSize: 18, color: CLAUDE.SPARK, fontStyle: 'italic',
        opacity: gateIn, transform: `translateY(${(1 - gateIn) * -10}px)` }}>
        {gateLabel}
      </div>
      {/* Right zone — edit */}
      <div style={{ position: 'absolute', right: width * 0.06, top: ZT, width: ZW, height: ZH,
        background: CLAUDE.CARD, border: `1px solid ${CLAUDE.BORDER}`, borderRadius: 14,
        padding: '20px 22px', opacity: rightIn, transform: `translateX(${(1 - rightIn) * 16}px)` }}>
        <div style={{ fontFamily: MONO, fontSize: 16, letterSpacing: 3, color: CLAUDE.INK,
          textTransform: 'uppercase', marginBottom: 10 }}>{rightLabel}</div>
        {rightItems.map((it, i) => (
          <div key={i} style={{ fontFamily: SANS, fontSize: 18, color: CLAUDE.INK,
            marginBottom: 8, display: 'flex', alignItems: 'center', gap: 8 }}>
            <div style={{ width: 7, height: 7, borderRadius: 4, background: CLAUDE.SPARK, flexShrink: 0 }} />
            {it}
          </div>
        ))}
      </div>
      <SparkRow text={sparkLine} opacity={rightIn} height={height} />
    </AbsoluteFill>
  );
};

// ── VRRenameCard — old name → new name with "audit both" stamp ──────────────
// B08: middleware.ts → proxy.ts, next lint → eslint CLI.

export const vrRenameCardSchema = z.object({
  renames: z.array(z.object({
    old: z.string(), new: z.string(),
  })).default([]),
  auditNote: z.string().default('audit BOTH names in your grep'),
  sparkLine: z.string().default("check yesterday's filenames too."),
});
export type VRRenameCardProps = z.infer<typeof vrRenameCardSchema>;

export const VRRenameCard: React.FC<VRRenameCardProps> = ({ renames, auditNote, sparkLine }) => {
  const frame = useCurrentFrame();
  const { fps, height } = useVideoConfig();
  const titleIn = sp(frame, fps, 0);
  const noteIn  = sp(frame, fps, 8 * (renames.length + 2));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, display: 'flex',
      flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
      <div style={{ fontFamily: MONO, fontSize: 16, letterSpacing: 4, color: CLAUDE.INK_SOFT,
        textTransform: 'uppercase', marginBottom: 28, opacity: titleIn }}>
        NEXT 16 RENAMES
      </div>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 22, marginBottom: 36 }}>
        {renames.map((r, i) => {
          const cardIn = sp(frame, fps, 8 + i * 10);
          return (
            <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 28,
              opacity: cardIn, transform: `translateY(${(1 - cardIn) * 14}px)` }}>
              <div style={{ background: CLAUDE.FOOTER, border: `1px solid ${CLAUDE.BORDER}`,
                borderRadius: 12, padding: '14px 28px', fontFamily: MONO, fontSize: 26,
                color: CLAUDE.INK_SOFT, minWidth: 300, textAlign: 'center' }}>
                {r.old}
              </div>
              <svg width={44} height={24} viewBox="0 0 44 24">
                <path d="M 0 12 L 36 12 M 29 5 L 36 12 L 29 19"
                  stroke={CLAUDE.SPARK} strokeWidth={3.5} strokeLinecap="round" fill="none" />
              </svg>
              <div style={{ background: CLAUDE.CARD, border: `2px solid ${CLAUDE.SPARK}`,
                borderRadius: 12, padding: '14px 28px', fontFamily: MONO, fontSize: 26,
                color: CLAUDE.INK, minWidth: 300, textAlign: 'center' }}>
                {r.new}
              </div>
            </div>
          );
        })}
      </div>
      {/* Audit stamp */}
      <div style={{ background: CLAUDE.FOOTER, border: `1px solid ${CLAUDE.BORDER}`,
        borderRadius: 12, padding: '14px 36px', fontFamily: SANS, fontSize: 18,
        color: CLAUDE.SPARK, fontWeight: 700, letterSpacing: 1, textTransform: 'uppercase',
        opacity: noteIn, transform: `translateY(${(1 - noteIn) * 8}px)` }}>
        ⚑ {auditNote}
      </div>
      <SparkRow text={sparkLine} opacity={noteIn} height={height} />
    </AbsoluteFill>
  );
};

// ── VRTwoColCard — two-column comparison ─────────────────────────────────────
// B12: local next dev vs vercel runtime.

export const vrTwoColCardSchema = z.object({
  leftTitle:  z.string().default('local'),
  leftItems:  z.array(z.string()).default([]),
  rightTitle: z.string().default('vercel'),
  rightItems: z.array(z.string()).default([]),
  bridgeNote: z.string().optional(),
  sparkLine:  z.string().default('local ≠ deployed.'),
});
export type VRTwoColCardProps = z.infer<typeof vrTwoColCardSchema>;

export const VRTwoColCard: React.FC<VRTwoColCardProps> = (
  { leftTitle, leftItems, rightTitle, rightItems, bridgeNote, sparkLine }
) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const leftIn   = sp(frame, fps, 0);
  const rightIn  = sp(frame, fps, 14);
  const bridgeIn = sp(frame, fps, 26);
  const CW = width * 0.37, CT = height * 0.16, CH = height * 0.57;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      {/* Left col */}
      <div style={{ position: 'absolute', left: width * 0.06, top: CT, width: CW, height: CH,
        background: CLAUDE.FOOTER, border: `1px solid ${CLAUDE.BORDER}`, borderRadius: 16,
        padding: '26px 28px', opacity: leftIn, transform: `translateX(${(1 - leftIn) * -16}px)` }}>
        <div style={{ fontFamily: MONO, fontSize: 16, letterSpacing: 4, color: CLAUDE.INK_SOFT,
          textTransform: 'uppercase', marginBottom: 16 }}>{leftTitle}</div>
        {leftItems.map((it, i) => (
          <div key={i} style={{ fontFamily: SANS, fontSize: 19, color: CLAUDE.INK_SOFT,
            marginBottom: 12, display: 'flex', alignItems: 'flex-start', gap: 10 }}>
            <div style={{ width: 7, height: 7, borderRadius: 4, background: CLAUDE.BORDER,
              marginTop: 7, flexShrink: 0 }} />
            {it}
          </div>
        ))}
      </div>
      {/* Bridge */}
      {bridgeNote && (
        <div style={{ position: 'absolute', left: 0, right: 0, top: height * 0.44,
          textAlign: 'center', fontFamily: SERIF, fontSize: 20, color: CLAUDE.SPARK,
          fontStyle: 'italic', opacity: bridgeIn }}>
          {bridgeNote}
        </div>
      )}
      {/* Right col */}
      <div style={{ position: 'absolute', right: width * 0.06, top: CT, width: CW, height: CH,
        background: CLAUDE.CARD, border: `2px solid ${CLAUDE.SPARK}`, borderRadius: 16,
        padding: '26px 28px', opacity: rightIn, transform: `translateX(${(1 - rightIn) * 16}px)` }}>
        <div style={{ fontFamily: MONO, fontSize: 16, letterSpacing: 4, color: CLAUDE.SPARK,
          textTransform: 'uppercase', marginBottom: 16 }}>{rightTitle}</div>
        {rightItems.map((it, i) => (
          <div key={i} style={{ fontFamily: SANS, fontSize: 19, color: CLAUDE.INK,
            marginBottom: 12, display: 'flex', alignItems: 'flex-start', gap: 10 }}>
            <div style={{ width: 7, height: 7, borderRadius: 4, background: CLAUDE.SPARK,
              marginTop: 7, flexShrink: 0 }} />
            {it}
          </div>
        ))}
      </div>
      <SparkRow text={sparkLine} opacity={bridgeIn} height={height} />
    </AbsoluteFill>
  );
};

// ── VRChecklistCard — Cowork QA checklist card ───────────────────────────────
// B16: prod URL · preview URL · flows to walk · evidence out.

export const vrChecklistCardSchema = z.object({
  title:       z.string().default("Cowork's checklist"),
  items:       z.array(z.string()).default([]),
  outputLabel: z.string().optional(),
  sparkLine:   z.string().default('bounded checklist.'),
});
export type VRChecklistCardProps = z.infer<typeof vrChecklistCardSchema>;

export const VRChecklistCard: React.FC<VRChecklistCardProps> = (
  { title, items, outputLabel, sparkLine }
) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const titleIn = sp(frame, fps, 0);
  const outIn   = sp(frame, fps, 8 * (items.length + 2));
  const CARD_W  = width * 0.55;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, display: 'flex',
      flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
      <div style={{ width: CARD_W, background: CLAUDE.CARD, border: `1px solid ${CLAUDE.BORDER}`,
        borderRadius: 20, padding: '36px 42px', boxShadow: '0 10px 32px rgba(61,57,41,0.09)' }}>
        <div style={{ fontFamily: SERIF, fontSize: 36, color: CLAUDE.INK, marginBottom: 28, opacity: titleIn }}>
          {title}
        </div>
        {items.map((it, i) => {
          const itemIn = sp(frame, fps, 8 + i * 8);
          return (
            <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 16,
              marginBottom: 18, opacity: itemIn, transform: `translateX(${(1 - itemIn) * 12}px)` }}>
              <div style={{ width: 26, height: 26, borderRadius: 6,
                border: `2px solid ${itemIn >= 1 ? CLAUDE.SPARK : CLAUDE.BORDER}`,
                background: itemIn >= 1 ? '#FEF0EA' : 'transparent',
                display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
                {itemIn >= 1 && (
                  <svg width={14} height={14} viewBox="0 0 14 14">
                    <path d="M2 7 L6 11 L12 3" stroke={CLAUDE.SPARK} strokeWidth={2.5}
                      strokeLinecap="round" fill="none" />
                  </svg>
                )}
              </div>
              <span style={{ fontFamily: SANS, fontSize: 22, color: CLAUDE.INK }}>{it}</span>
            </div>
          );
        })}
        {outputLabel && (
          <div style={{ marginTop: 20, paddingTop: 20, borderTop: `1px solid ${CLAUDE.BORDER}`,
            fontFamily: SANS, fontSize: 18, color: CLAUDE.SPARK, opacity: outIn }}>
            ↳ {outputLabel}
          </div>
        )}
      </div>
      <SparkRow text={sparkLine} opacity={outIn} height={height} />
    </AbsoluteFill>
  );
};

// ── VRLadderCard — numbered priority ladder ──────────────────────────────────
// B17: connectors (1, accent) → browser (2) → screen interaction (3).

export const vrLadderCardSchema = z.object({
  steps: z.array(z.object({
    label:  z.string(),
    sub:    z.string(),
    accent: z.boolean().optional(),
  })).default([]),
  sparkLine: z.string().default('connectors first.'),
});
export type VRLadderCardProps = z.infer<typeof vrLadderCardSchema>;

export const VRLadderCard: React.FC<VRLadderCardProps> = ({ steps, sparkLine }) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const N       = steps.length;
  const STEP_H  = 92, GAP = 18;
  const totalH  = N * (STEP_H + GAP) - GAP;
  const startY  = (height - totalH) / 2 - 24;
  const sparkIn = sp(frame, fps, 8 * (N + 2));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      {steps.map((s, i) => {
        const stepIn = sp(frame, fps, i * 9);
        const y = startY + i * (STEP_H + GAP);
        return (
          <React.Fragment key={i}>
            {/* Circle badge */}
            <div style={{ position: 'absolute', left: width * 0.13, top: y + (STEP_H - 48) / 2,
              width: 48, height: 48, borderRadius: '50%',
              background: s.accent ? CLAUDE.SPARK : CLAUDE.FOOTER,
              border: `2px solid ${s.accent ? CLAUDE.SPARK : CLAUDE.BORDER}`,
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              fontFamily: MONO, fontSize: 20, fontWeight: 700,
              color: s.accent ? '#fff' : CLAUDE.INK_SOFT,
              opacity: stepIn, transform: `scale(${stepIn})` }}>
              {i + 1}
            </div>
            {/* Row card */}
            <div style={{ position: 'absolute', left: width * 0.13 + 62, top: y,
              width: width * 0.66, height: STEP_H,
              background: s.accent ? CLAUDE.CARD : CLAUDE.FOOTER,
              border: `${s.accent ? 2 : 1}px solid ${s.accent ? CLAUDE.SPARK : CLAUDE.BORDER}`,
              borderRadius: 14, padding: '18px 26px',
              opacity: stepIn, transform: `translateX(${(1 - stepIn) * 18}px)` }}>
              <div style={{ fontFamily: SERIF, fontSize: 28,
                color: s.accent ? CLAUDE.INK : CLAUDE.INK_SOFT, marginBottom: 4 }}>
                {s.label}
              </div>
              <div style={{ fontFamily: SANS, fontSize: 17, color: CLAUDE.INK_SOFT }}>{s.sub}</div>
            </div>
          </React.Fragment>
        );
      })}
      <SparkRow text={sparkLine} opacity={sparkIn} height={height} />
    </AbsoluteFill>
  );
};

// ── VRCycleCard — closed-loop cycle diagram ──────────────────────────────────
// B18: Code edits → Vercel preview → Cowork inspects → finding written → Code.

export const vrCycleCardSchema = z.object({
  nodes:     z.array(z.string()).default([]),
  centerNote: z.string().optional(),
  sparkLine: z.string().default('nobody freelances.'),
});
export type VRCycleCardProps = z.infer<typeof vrCycleCardSchema>;

export const VRCycleCard: React.FC<VRCycleCardProps> = ({ nodes, centerNote, sparkLine }) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const N = nodes.length;
  const CX = width / 2, CY = height / 2 - 24, R = 196;
  const sparkIn = sp(frame, fps, 8 * (N + 2));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <svg width={width} height={height} style={{ position: 'absolute', inset: 0 }}>
        {nodes.map((_, i) => {
          const a1 = ((i / N) - 0.25) * Math.PI * 2;
          const a2 = (((i + 1) % N) / N - 0.25) * Math.PI * 2;
          const x1 = CX + R * Math.cos(a1), y1 = CY + R * Math.sin(a1);
          const x2 = CX + R * Math.cos(a2), y2 = CY + R * Math.sin(a2);
          const mid = ((i + 0.5) / N - 0.25) * Math.PI * 2;
          const arcIn = sp(frame, fps, 6 + i * 8);
          return (
            <path key={i}
              d={`M ${x1} ${y1} Q ${CX + R * 1.25 * Math.cos(mid)} ${CY + R * 1.25 * Math.sin(mid)} ${x2} ${y2}`}
              stroke={CLAUDE.SPARK} strokeWidth={3} fill="none" strokeLinecap="round"
              strokeDasharray={320} strokeDashoffset={320 * (1 - arcIn)} />
          );
        })}
      </svg>
      {nodes.map((n, i) => {
        const angle = ((i / N) - 0.25) * Math.PI * 2;
        const nx = CX + R * Math.cos(angle), ny = CY + R * Math.sin(angle);
        const nodeIn = sp(frame, fps, i * 8);
        const isCode = i === 0;
        return (
          <div key={i} style={{ position: 'absolute', left: nx - 90, top: ny - 36,
            width: 180, height: 72,
            background: isCode ? CLAUDE.CARD : CLAUDE.FOOTER,
            border: `${isCode ? 2 : 1}px solid ${isCode ? CLAUDE.SPARK : CLAUDE.BORDER}`,
            borderRadius: 12, display: 'flex', alignItems: 'center', justifyContent: 'center',
            fontFamily: SANS, fontSize: 17, fontWeight: isCode ? 700 : 400,
            color: isCode ? CLAUDE.INK : CLAUDE.INK_SOFT, textAlign: 'center',
            opacity: nodeIn, transform: `scale(${nodeIn})`, padding: '0 12px' }}>
            {n}
          </div>
        );
      })}
      {centerNote && (
        <div style={{ position: 'absolute', left: 0, right: 0, top: CY - 14, textAlign: 'center',
          fontFamily: MONO, fontSize: 16, letterSpacing: 4, color: CLAUDE.INK_SOFT,
          textTransform: 'uppercase', opacity: sparkIn }}>
          {centerNote}
        </div>
      )}
      <SparkRow text={sparkLine} opacity={sparkIn} height={height} />
    </AbsoluteFill>
  );
};

// ── VRDangerCard — danger chip nested inside safety boxes ────────────────────
// B19: sandbox > worktree > branch > commits, bypass chip at center.

export const vrDangerCardSchema = z.object({
  layers:      z.array(z.string()).default([]),
  dangerLabel: z.string().default('--dangerously-skip-permissions'),
  dangerNote:  z.string().optional(),
  sparkLine:   z.string().default('the bypass, contained.'),
});
export type VRDangerCardProps = z.infer<typeof vrDangerCardSchema>;

export const VRDangerCard: React.FC<VRDangerCardProps> = (
  { layers, dangerLabel, dangerNote, sparkLine }
) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const N = layers.length;
  const centerIn = sp(frame, fps, 6);
  const sparkIn  = sp(frame, fps, 8 * (N + 2));
  const MARGIN   = 48;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      {layers.map((l, i) => {
        const boxIn = sp(frame, fps, (N - 1 - i) * 8);
        const inset = i * MARGIN;
        return (
          <div key={i} style={{
            position: 'absolute',
            left: inset, top: inset * 0.6, right: inset, bottom: inset * 0.6 + 72,
            border: `${i === 0 ? 2 : 1}px solid ${CLAUDE.BORDER}`,
            borderRadius: Math.max(6, 20 - i * 3),
            opacity: boxIn,
            display: 'flex', alignItems: 'flex-start', padding: '12px 18px',
            background: i === N - 1 ? CLAUDE.FOOTER : 'transparent',
          }}>
            <span style={{ fontFamily: MONO, fontSize: 16, letterSpacing: 2,
              color: CLAUDE.INK_SOFT, textTransform: 'uppercase' as const }}>
              {l}
            </span>
          </div>
        );
      })}
      {/* Center danger chip */}
      <div style={{ position: 'absolute', left: 0, right: 0, top: 0, bottom: 72,
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        opacity: centerIn, pointerEvents: 'none' }}>
        <div style={{ background: '#FEF0EA', border: `2px solid ${CLAUDE.SPARK}`,
          borderRadius: 12, padding: '16px 32px',
          display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 10,
          transform: `scale(${centerIn})` }}>
          <div style={{ fontFamily: MONO, fontSize: 18, color: CLAUDE.SPARK, fontWeight: 700 }}>
            ⚠ {dangerLabel}
          </div>
          {dangerNote && (
            <div style={{ fontFamily: SANS, fontSize: 16, color: CLAUDE.INK_SOFT,
              textAlign: 'center', maxWidth: 360 }}>
              {dangerNote}
            </div>
          )}
        </div>
      </div>
      <SparkRow text={sparkLine} opacity={sparkIn} height={height} />
    </AbsoluteFill>
  );
};
