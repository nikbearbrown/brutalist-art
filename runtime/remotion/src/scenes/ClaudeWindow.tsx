import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * ClaudeWindow — the Claude app window frame in the fidelity skin.
 * view:'artifact'  — artifact panel (staggered numbered lines, terracotta spark line).
 * view:'composer'  — empty composer window (future use).
 * view:'blank'     — cream stage only.
 *
 * Per ILLUSTRATE LAW: this is a UI beat — the Claude UI is the subject.
 * Used for verdict pages and ASK→RESULT artifact pages.
 * Duration-agnostic — compile.py conforms to actual audio length.
 */

export const claudeWindowSchema = z.object({
  view:           z.enum(['artifact', 'composer', 'blank']).default('artifact'),
  artifactTitle:  z.string().default('Verdict'),
  artifactHeading:z.string().default('The verdict'),
  artifactLines:  z.array(z.string()).default([]),
  sparkLine:      z.string().default(''),
  width:          z.number().optional(),
  height:         z.number().optional(),
  fontSize:       z.number().optional(),
});
export type ClaudeWindowProps = z.infer<typeof claudeWindowSchema>;

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;
const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));

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

export const ClaudeWindow: React.FC<ClaudeWindowProps> = ({
  view, artifactTitle, artifactHeading, artifactLines, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { fps, height } = useVideoConfig();
  // §8.1 floor: 3.2% of 1080px logical = 34.6px physical at 4K.
  // SANS (SF Pro Text) x-height ratio ≈ 0.53: 37px CSS → 39.2px physical ✓
  // SERIF (EB Garamond) x-height ratio ≈ 0.43: needs 43px CSS → 37.0px physical ✓
  const BODY_FS  = Math.round(height * 0.034);  // 37px — SANS body lines
  const SERIF_FS = Math.round(height * 0.040);  // 43px — SERIF title bar + sparkLine

  const cardIn = spring({ frame,        fps, config: { damping: 28, stiffness: 140, mass: 0.8 } });
  const headIn = spring({ frame: frame - 8, fps, config: { damping: 28, stiffness: 140, mass: 0.8 } });
  const sparkIn = spring({ frame: frame - (artifactLines.length + 3) * 7, fps, config: { damping: 28, stiffness: 140, mass: 0.8 } });

  const lines = artifactLines ?? [];

  if (view === 'blank') {
    return <AbsoluteFill style={{ background: CLAUDE.PAGE }} />;
  }

  return (
    <AbsoluteFill style={{ background: '#F2F0E9' }}>
    {/* Inner safe-zone container: 6% padding top+bottom keeps all content inside the 5% title-safe box */}
    <div style={{
      display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
      height: '100%',
      paddingTop: Math.round(height * 0.06), paddingBottom: Math.round(height * 0.06),
      boxSizing: 'border-box', overflow: 'hidden',
    }}>
      {/* Artifact card */}
      <div style={{
        width: 1360,
        background: CLAUDE.CARD,
        borderRadius: 20,
        boxShadow: '0 12px 48px rgba(61,57,41,0.14)',
        border: `1px solid ${CLAUDE.BORDER}`,
        overflow: 'hidden',
        transform: `scale(${clamp(cardIn, 0, 1)})`,
        opacity: clamp(cardIn, 0, 1),
      }}>
        {/* Title bar */}
        <div style={{
          background: CLAUDE.PAGE,
          borderBottom: `1px solid ${CLAUDE.BORDER}`,
          padding: '16px 28px',
          display: 'flex',
          alignItems: 'center',
          gap: 10,
        }}>
          <Spark />
          <span style={{ fontFamily: SERIF, fontSize: SERIF_FS, color: CLAUDE.INK, fontWeight: 600 }}>
            {artifactTitle}
          </span>
        </div>

        {/* Body */}
        <div style={{ padding: '36px 52px 44px' }}>
          {/* Heading */}
          <div style={{
            fontFamily: SERIF,
            fontSize: 42,
            fontWeight: 700,
            color: CLAUDE.INK,
            marginBottom: 24,
            opacity: clamp(headIn, 0, 1),
          }}>
            {artifactHeading}
          </div>

          {/* Lines */}
          {lines.map((line, i) => {
            const lineIn = spring({ frame: frame - (i + 2) * 7, fps, config: { damping: 28, stiffness: 140, mass: 0.8 } });
            const op = clamp(lineIn, 0, 1);
            const ty = (1 - op) * 12;
            return (
              <div key={i} style={{
                display: 'flex',
                alignItems: 'flex-start',
                gap: 16,
                marginBottom: 26,
                opacity: op,
                transform: `translateY(${ty}px)`,
              }}>
                <span style={{
                  fontFamily: SANS,
                  fontSize: BODY_FS,
                  color: CLAUDE.INK,
                  flexShrink: 0,
                  marginTop: 2,
                  fontWeight: 700,
                }}>
                  {i + 1}.
                </span>
                <span style={{
                  fontFamily: SANS,
                  fontSize: BODY_FS,
                  color: CLAUDE.INK,
                  lineHeight: 1.55,
                }}>
                  {line}
                </span>
              </div>
            );
          })}
        </div>
      </div>

      {/* Spark line below card */}
      {sparkLine ? (
        <div style={{
          marginTop: 28,
          display: 'flex',
          alignItems: 'center',
          gap: 10,
          opacity: clamp(sparkIn, 0, 1),
          transform: `translateY(${(1 - clamp(sparkIn, 0, 1)) * 8}px)`,
        }}>
          <Spark size={18} />
          <span style={{
            fontFamily: SERIF,
            fontSize: SERIF_FS,
            fontStyle: 'italic',
            color: CLAUDE.INK,
          }}>
            {sparkLine}
          </span>
        </div>
      ) : null}
    </div>
    </AbsoluteFill>
  );
};
