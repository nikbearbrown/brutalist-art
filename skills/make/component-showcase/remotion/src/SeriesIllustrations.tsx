/**
 * SeriesIllustrations.tsx
 * Shared illustration components for claude-hai and claude-medhavy episodes.
 * All components use the claude stage palette (#F2F0E9) and accept an optional
 * evidenceNote prop (shown bottom-right for Medhavy on-screen evidence discipline).
 */
import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig } from 'remotion';
import { CLAUDE_FONT } from '../../../../../../brutalist-art/runtime/remotion/src/tokens/claude';
import { DivergentFates, FatesData } from './deckPatterns';

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;
const STAGE = '#F2F0E9';
const INK   = '#3D3929';
const INK_SOFT = '#73705F';
const SPARK = '#D97757';
const WARN  = '#A44A32';

const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));
const remap = (x: number, x0: number, x1: number, y0: number, y1: number) => {
  const t = clamp((x - x0) / (x1 - x0 || 1), 0, 1);
  return y0 + (y1 - y0) * t;
};
const ease = (t: number) => 1 - Math.pow(1 - clamp(t, 0, 1), 3);

const useP = () => {
  const f = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  return clamp(f / Math.max(1, durationInFrames - 1), 0, 1);
};

// ── Primitives ─────────────────────────────────────────────────────────────────

export const SparkLineSeries: React.FC<{ text: string; pos?: 'top' | 'bottom' }> = ({ text, pos = 'top' }) => {
  const op = ease(remap(useP(), 0, 0.07, 0, 1));
  return (
    <div style={{
      position: 'absolute',
      ...(pos === 'top' ? { top: 44 } : { bottom: 40 }),
      left: 0, right: 0, display: 'flex',
      justifyContent: 'center', alignItems: 'center', gap: 16, opacity: op,
    }}>
      <svg width={26} height={26} viewBox="0 0 24 24">
        {Array.from({ length: 8 }, (_, i) => (
          <line key={i} x1={12} y1={12}
            x2={12 + 10 * Math.cos(i * Math.PI / 4 + 0.2)}
            y2={12 + 10 * Math.sin(i * Math.PI / 4 + 0.2)}
            stroke={SPARK} strokeWidth={3.2} strokeLinecap="round" />
        ))}
      </svg>
      <div style={{ fontFamily: SERIF, fontSize: 38, color: INK }}>{text}</div>
    </div>
  );
};

const EvidenceFlag: React.FC<{ note?: string }> = ({ note }) => {
  if (!note) return null;
  const op = ease(remap(useP(), 0.08, 0.20, 0, 1));
  return (
    <div style={{
      position: 'absolute', bottom: 32, right: 44,
      fontFamily: SANS, fontSize: 16, color: INK_SOFT,
      background: '#fff', border: '1px solid #C8C5BC',
      borderRadius: 4, padding: '5px 12px', opacity: op * 0.85,
    }}>
      {note}
    </div>
  );
};

const Stage: React.FC<{ spark?: string; children: React.ReactNode; evidenceNote?: string }> = ({ spark, children, evidenceNote }) => (
  <AbsoluteFill style={{ background: STAGE }}>
    {children}
    {spark && <SparkLineSeries text={spark} />}
    <EvidenceFlag note={evidenceNote} />
  </AbsoluteFill>
);

// ── TwoColumnCard ──────────────────────────────────────────────────────────────
// Covered/open · Banned/allowed · Crutch/scaffold · Use/don't-use · Machine/human
export const TwoColumnCard: React.FC<{
  sparkLine?: string;
  leftHeader: string;
  rightHeader: string;
  leftItems?: string[];
  rightItems?: string[];
  coveredItems?: string[];
  openItems?: string[];
  bannedItems?: string[];
  evidenceNote?: string;
}> = (props) => {
  const p = useP();
  const left  = props.leftItems  ?? props.coveredItems ?? props.bannedItems ?? [];
  const right = props.rightItems ?? props.openItems ?? [];
  const hOp = ease(remap(p, 0.04, 0.14, 0, 1));
  return (
    <Stage spark={props.sparkLine} evidenceNote={props.evidenceNote}>
      <div style={{ position: 'absolute', top: 110, left: 80, right: 80, bottom: 80, display: 'flex' }}>
        <div style={{ flex: 1, paddingRight: 48, borderRight: '1px solid #C8C5BC' }}>
          <div style={{ fontFamily: SERIF, fontSize: 32, fontWeight: 700, color: WARN, marginBottom: 26, opacity: hOp }}>
            {props.leftHeader}
          </div>
          {left.map((item, i) => {
            const op = ease(remap(p, 0.14 + i * 0.09, 0.26 + i * 0.09, 0, 1));
            return (
              <div key={i} style={{ display: 'flex', gap: 14, marginBottom: 20, opacity: op, alignItems: 'flex-start' }}>
                <div style={{ width: 6, height: 6, borderRadius: '50%', background: WARN, marginTop: 12, flexShrink: 0 }} />
                <div style={{ fontFamily: SANS, fontSize: 26, color: INK, lineHeight: 1.35 }}>{item}</div>
              </div>
            );
          })}
        </div>
        <div style={{ flex: 1, paddingLeft: 48 }}>
          <div style={{ fontFamily: SERIF, fontSize: 32, fontWeight: 700, color: SPARK, marginBottom: 26, opacity: hOp }}>
            {props.rightHeader}
          </div>
          {right.map((item, i) => {
            const op = ease(remap(p, 0.22 + i * 0.09, 0.34 + i * 0.09, 0, 1));
            return (
              <div key={i} style={{ display: 'flex', gap: 14, marginBottom: 20, opacity: op, alignItems: 'flex-start' }}>
                <div style={{ width: 6, height: 6, borderRadius: '50%', background: SPARK, marginTop: 12, flexShrink: 0 }} />
                <div style={{ fontFamily: SANS, fontSize: 26, color: INK, lineHeight: 1.35 }}>{item}</div>
              </div>
            );
          })}
        </div>
      </div>
    </Stage>
  );
};

// ── ThreeCardFlow ──────────────────────────────────────────────────────────────
// Three sequential labeled cards with arrows (e.g. H1-B02 ExemptionTrap)
export const ThreeCardFlow: React.FC<{
  sparkLine?: string;
  vaguePhrase?: string;
  interpretations?: string[];
  safeMove?: string;
  cards?: { label: string; content: string }[];
  evidenceNote?: string;
}> = (props) => {
  const p = useP();
  const cards = props.cards ?? [
    { label: 'the policy says', content: props.vaguePhrase ?? '' },
    { label: 'teachers interpret it as', content: (props.interpretations ?? []).join(' · ') },
    { label: 'the safe move', content: props.safeMove ?? '' },
  ];
  return (
    <Stage spark={props.sparkLine} evidenceNote={props.evidenceNote}>
      <div style={{ position: 'absolute', top: 110, left: 52, right: 52, bottom: 80, display: 'flex', alignItems: 'center', gap: 18 }}>
        {cards.map((card, i) => {
          const op = ease(remap(p, 0.08 + i * 0.18, 0.22 + i * 0.18, 0, 1));
          const isLast = i === cards.length - 1;
          return (
            <React.Fragment key={i}>
              {i > 0 && (
                <svg width={30} height={30} viewBox="0 0 24 24" style={{ flexShrink: 0, opacity: ease(remap(p, 0.14 + (i - 1) * 0.18, 0.24 + (i - 1) * 0.18, 0, 1)) }}>
                  <path d="M5 12h14M14 6l6 6-6 6" stroke={SPARK} strokeWidth={2.5} strokeLinecap="round" fill="none" />
                </svg>
              )}
              <div style={{
                flex: 1, background: '#fff', borderRadius: 10,
                border: `2px solid ${isLast ? SPARK : '#C8C5BC'}`,
                padding: '28px 22px', opacity: op,
              }}>
                <div style={{ fontFamily: SANS, fontSize: 15, fontWeight: 700, color: isLast ? SPARK : INK_SOFT, letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: 14 }}>
                  {card.label}
                </div>
                <div style={{ fontFamily: SERIF, fontSize: 24, color: INK, lineHeight: 1.45 }}>
                  {card.content}
                </div>
              </div>
            </React.Fragment>
          );
        })}
      </div>
    </Stage>
  );
};

// ── ContrastBoxes ──────────────────────────────────────────────────────────────
// Two large side-by-side boxes — neutral left, terracotta-highlighted right
export const ContrastBoxes: React.FC<{
  sparkLine?: string;
  leftLabel: string;
  leftStatus: string;
  rightLabel: string;
  rightStatus: string;
  evidenceNote?: string;
}> = (props) => {
  const p = useP();
  const lOp = ease(remap(p, 0.06, 0.18, 0, 1));
  const rOp = ease(remap(p, 0.22, 0.34, 0, 1));
  return (
    <Stage spark={props.sparkLine} evidenceNote={props.evidenceNote}>
      <div style={{ position: 'absolute', top: 120, left: 80, right: 80, bottom: 80, display: 'flex', gap: 44, alignItems: 'center' }}>
        <div style={{ flex: 1, background: '#fff', borderRadius: 14, border: '2px solid #C8C5BC', padding: '52px 36px', opacity: lOp, textAlign: 'center' }}>
          <div style={{ fontFamily: SERIF, fontSize: 44, fontWeight: 700, color: INK_SOFT, marginBottom: 18 }}>{props.leftLabel}</div>
          <div style={{ fontFamily: SANS, fontSize: 24, color: INK_SOFT, lineHeight: 1.4 }}>{props.leftStatus}</div>
        </div>
        <div style={{ flex: 1, background: '#fff', borderRadius: 14, border: `3px solid ${SPARK}`, padding: '52px 36px', opacity: rOp, textAlign: 'center' }}>
          <div style={{ fontFamily: SERIF, fontSize: 44, fontWeight: 700, color: SPARK, marginBottom: 18 }}>{props.rightLabel}</div>
          <div style={{ fontFamily: SANS, fontSize: 24, color: INK, lineHeight: 1.4 }}>{props.rightStatus}</div>
        </div>
      </div>
    </Stage>
  );
};

// ── ConceptCard ────────────────────────────────────────────────────────────────
// Centered heading + body paragraph — the workhorse for most inner beats
export const ConceptCard: React.FC<{
  sparkLine?: string;
  heading: string;
  body: string;
  evidenceNote?: string;
}> = (props) => {
  const p = useP();
  const hOp = ease(remap(p, 0.05, 0.17, 0, 1));
  const bOp = ease(remap(p, 0.20, 0.34, 0, 1));
  return (
    <Stage spark={props.sparkLine} evidenceNote={props.evidenceNote}>
      <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
        <div style={{ padding: '0 120px', textAlign: 'center', maxWidth: 1040 }}>
          <div style={{ fontFamily: SERIF, fontSize: 52, fontWeight: 700, color: INK, lineHeight: 1.15, marginBottom: 34, opacity: hOp }}>
            {props.heading}
          </div>
          <div style={{ fontFamily: SANS, fontSize: 27, color: INK, lineHeight: 1.55, opacity: bOp }}>
            {props.body}
          </div>
        </div>
      </AbsoluteFill>
    </Stage>
  );
};

// ── ListCard ───────────────────────────────────────────────────────────────────
// Single labelled bullet list — for USE / DON'T USE / what-not-to-delegate
export const ListCard: React.FC<{
  sparkLine?: string;
  heading?: string;
  items: string[];
  accentFirst?: boolean;
  evidenceNote?: string;
}> = (props) => {
  const p = useP();
  const hOp = ease(remap(p, 0.05, 0.14, 0, 1));
  return (
    <Stage spark={props.sparkLine} evidenceNote={props.evidenceNote}>
      <div style={{ position: 'absolute', top: 110, left: 180, right: 180, bottom: 80 }}>
        {props.heading && (
          <div style={{ fontFamily: SERIF, fontSize: 36, fontWeight: 700, color: INK, marginBottom: 32, opacity: hOp }}>
            {props.heading}
          </div>
        )}
        {props.items.map((item, i) => {
          const op = ease(remap(p, 0.14 + i * 0.10, 0.25 + i * 0.10, 0, 1));
          const dot = i === 0 && props.accentFirst ? SPARK : SPARK;
          return (
            <div key={i} style={{ display: 'flex', gap: 22, marginBottom: 24, opacity: op, alignItems: 'flex-start' }}>
              <div style={{ width: 8, height: 8, borderRadius: '50%', background: dot, marginTop: 13, flexShrink: 0 }} />
              <div style={{ fontFamily: SANS, fontSize: 28, color: INK, lineHeight: 1.35 }}>{item}</div>
            </div>
          );
        })}
      </div>
    </Stage>
  );
};

// ── PairRuleCard ───────────────────────────────────────────────────────────────
// AI-yes / not-AI-here paired rule display
export const PairRuleCard: React.FC<{
  sparkLine?: string;
  heading?: string;
  pairs: { ai: string; notAi: string }[];
  evidenceNote?: string;
}> = (props) => {
  const p = useP();
  const hOp = ease(remap(p, 0.04, 0.14, 0, 1));
  return (
    <Stage spark={props.sparkLine} evidenceNote={props.evidenceNote}>
      <div style={{ position: 'absolute', top: 110, left: 80, right: 80, bottom: 80 }}>
        {props.heading && (
          <div style={{ fontFamily: SERIF, fontSize: 32, color: INK, fontWeight: 700, marginBottom: 20, opacity: hOp }}>
            {props.heading}
          </div>
        )}
        <div style={{ display: 'flex', marginBottom: 14, opacity: hOp }}>
          <div style={{ flex: 1, fontFamily: SANS, fontSize: 18, fontWeight: 700, color: SPARK, letterSpacing: '0.07em', textTransform: 'uppercase', paddingRight: 44 }}>AI-yes</div>
          <div style={{ flex: 1, fontFamily: SANS, fontSize: 18, fontWeight: 700, color: INK_SOFT, letterSpacing: '0.07em', textTransform: 'uppercase', paddingLeft: 44 }}>not-AI-here</div>
        </div>
        <div style={{ height: 1, background: '#C8C5BC', marginBottom: 18, opacity: hOp }} />
        {props.pairs.map((pair, i) => {
          const op = ease(remap(p, 0.18 + i * 0.13, 0.30 + i * 0.13, 0, 1));
          return (
            <div key={i} style={{ display: 'flex', marginBottom: 20, opacity: op, alignItems: 'flex-start' }}>
              <div style={{ flex: 1, paddingRight: 44, display: 'flex', gap: 14, alignItems: 'flex-start' }}>
                <div style={{ width: 7, height: 7, borderRadius: '50%', background: SPARK, marginTop: 11, flexShrink: 0 }} />
                <div style={{ fontFamily: SANS, fontSize: 25, color: INK, lineHeight: 1.35 }}>{pair.ai}</div>
              </div>
              <div style={{ flex: 1, paddingLeft: 44, borderLeft: '1px solid #C8C5BC', display: 'flex', gap: 14, alignItems: 'flex-start' }}>
                <div style={{ width: 7, height: 7, borderRadius: '50%', background: INK_SOFT, marginTop: 11, flexShrink: 0 }} />
                <div style={{ fontFamily: SANS, fontSize: 25, color: INK_SOFT, lineHeight: 1.35 }}>{pair.notAi}</div>
              </div>
            </div>
          );
        })}
      </div>
    </Stage>
  );
};

// ── TimelineCard ───────────────────────────────────────────────────────────────
// Horizontal spaced-repetition timeline
export const TimelineCard: React.FC<{
  sparkLine?: string;
  slots: { label: string; detail: string }[];
  evidenceNote?: string;
}> = (props) => {
  const p = useP();
  const N = props.slots.length;
  const TRACK_W = 1060;
  const slotX = (i: number) => 80 + i * (TRACK_W / Math.max(1, N - 1));

  return (
    <Stage spark={props.sparkLine} evidenceNote={props.evidenceNote}>
      <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
        <div style={{ width: 1200, position: 'relative', height: 260 }}>
          {/* track line */}
          <svg width={1200} height={20} style={{ position: 'absolute', top: 28, left: 0 }}>
            {props.slots.map((_, i) => {
              if (i === N - 1) return null;
              const x0 = slotX(i), x1 = slotX(i + 1);
              return <line key={i} x1={x0} y1={10} x2={x1} y2={10} stroke="#C8C5BC" strokeWidth={2}
                opacity={ease(remap(p, 0.18 + i * 0.10, 0.28 + i * 0.10, 0, 1))} />;
            })}
          </svg>
          {/* dots + labels */}
          {props.slots.map((slot, i) => {
            const op = ease(remap(p, 0.08 + i * 0.13, 0.20 + i * 0.13, 0, 1));
            const x = slotX(i);
            const isCurrent = i === 0;
            return (
              <div key={i} style={{ position: 'absolute', left: x - 90, top: 0, width: 180, textAlign: 'center', opacity: op }}>
                <div style={{ width: 22, height: 22, borderRadius: '50%', background: isCurrent ? SPARK : '#C8C5BC', margin: '0 auto 20px', border: `3px solid ${STAGE}` }} />
                <div style={{ fontFamily: SANS, fontSize: 18, fontWeight: 700, color: isCurrent ? SPARK : INK_SOFT, letterSpacing: '0.06em', textTransform: 'uppercase', marginBottom: 8 }}>
                  {slot.label}
                </div>
                <div style={{ fontFamily: SERIF, fontSize: 24, color: INK, lineHeight: 1.35 }}>
                  {slot.detail}
                </div>
              </div>
            );
          })}
        </div>
      </AbsoluteFill>
    </Stage>
  );
};

// ── SeasonDeckCard ─────────────────────────────────────────────────────────────
// Row of episode recap cards — last card gets terracotta (current episode)
export const SeasonDeckCard: React.FC<{
  sparkLine?: string;
  heading?: string;
  cards: { title: string }[];
  channelPrefix?: string;
  evidenceNote?: string;
}> = (props) => {
  const p = useP();
  const hOp = ease(remap(p, 0.05, 0.15, 0, 1));
  const prefix = props.channelPrefix ?? 'H';
  return (
    <Stage spark={props.sparkLine} evidenceNote={props.evidenceNote}>
      <div style={{ position: 'absolute', top: 110, left: 50, right: 50, bottom: 70 }}>
        {props.heading && (
          <div style={{ fontFamily: SERIF, fontSize: 32, color: INK, fontWeight: 700, marginBottom: 30, opacity: hOp, textAlign: 'center' }}>
            {props.heading}
          </div>
        )}
        <div style={{ display: 'flex', gap: 18, justifyContent: 'center', marginTop: props.heading ? 0 : 60 }}>
          {props.cards.map((card, i) => {
            const op = ease(remap(p, 0.12 + i * 0.11, 0.24 + i * 0.11, 0, 1));
            const isLast = i === props.cards.length - 1;
            return (
              <div key={i} style={{
                flex: 1, maxWidth: 210,
                background: isLast ? SPARK : '#fff',
                borderRadius: 10, border: `2px solid ${isLast ? SPARK : '#C8C5BC'}`,
                padding: '22px 14px', opacity: op, textAlign: 'center',
              }}>
                <div style={{ fontFamily: SANS, fontSize: 17, fontWeight: 800, color: isLast ? '#fff' : INK_SOFT, letterSpacing: '0.05em', marginBottom: 10 }}>
                  {prefix}{i + 1}
                </div>
                <div style={{ fontFamily: SERIF, fontSize: 20, color: isLast ? '#fff' : INK, lineHeight: 1.35 }}>
                  {card.title}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </Stage>
  );
};

// ── TierDiagram ────────────────────────────────────────────────────────────────
// 4-tier irreducibly-human taxonomy (H4-B01)
export const TierDiagram: React.FC<{
  sparkLine?: string;
  tiers: { level: number; label: string; owner: string; note: string }[];
  evidenceNote?: string;
}> = (props) => {
  const p = useP();
  return (
    <Stage spark={props.sparkLine} evidenceNote={props.evidenceNote}>
      <div style={{ position: 'absolute', top: 110, left: 100, right: 100, bottom: 70 }}>
        {props.tiers.map((tier, i) => {
          const op = ease(remap(p, 0.08 + i * 0.12, 0.20 + i * 0.12, 0, 1));
          const isHuman = tier.level >= 3;
          return (
            <div key={i} style={{
              display: 'flex', alignItems: 'center', gap: 28, marginBottom: 20, opacity: op,
              padding: '14px 18px', borderRadius: 8,
              background: isHuman ? 'rgba(217,119,87,0.06)' : 'transparent',
              border: isHuman ? '1px solid rgba(217,119,87,0.22)' : '1px solid transparent',
            }}>
              <div style={{
                width: 44, height: 44, borderRadius: '50%',
                background: isHuman ? SPARK : '#C8C5BC',
                display: 'flex', alignItems: 'center', justifyContent: 'center',
                fontFamily: SANS, fontSize: 18, fontWeight: 800, color: '#fff', flexShrink: 0,
              }}>
                {tier.level}
              </div>
              <div style={{ flex: 1, fontFamily: SERIF, fontSize: 28, color: INK, lineHeight: 1.2 }}>
                {tier.label}
              </div>
              <div style={{ textAlign: 'right', minWidth: 210 }}>
                <div style={{ fontFamily: SANS, fontSize: 17, fontWeight: 700, color: isHuman ? SPARK : INK_SOFT, letterSpacing: '0.06em', textTransform: 'uppercase' }}>
                  {tier.owner}
                </div>
                <div style={{ fontFamily: SANS, fontSize: 15, color: INK_SOFT }}>{tier.note}</div>
              </div>
            </div>
          );
        })}
      </div>
    </Stage>
  );
};

// ── DivergentFatesBeat ─────────────────────────────────────────────────────────
// Wraps deckPatterns DivergentFates for use in reel data JSONs (H2-B01, M2-B02)
export const DivergentFatesBeat: React.FC<{
  sparkLine?: string;
  title?: string;
  startLabel?: string;
  splitLabel?: string;
  leftTrack: { label: string; direction?: string; delta?: string; note?: string };
  rightTrack: { label: string; direction?: string; delta?: string; note?: string };
  evidenceNote?: string;
}> = (props) => {
  const data: FatesData = {
    slideMeta: props.evidenceNote ?? '',
    startLabel: props.startLabel ?? 'same tool',
    splitLabel: props.splitLabel ?? 'divergent outcomes',
    tracks: [
      {
        label: props.leftTrack.label,
        outcome: props.leftTrack.delta ?? '',
        tone: 'good',
        path: 'up',
        notes: props.leftTrack.note ? [props.leftTrack.note] : [],
      },
      {
        label: props.rightTrack.label,
        outcome: props.rightTrack.delta ?? '',
        tone: 'warn',
        path: 'down',
        notes: props.rightTrack.note ? [props.rightTrack.note] : [],
      },
    ],
  };
  return <DivergentFates data={data} />;
};
