import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * DeepExplainerPatterns — reusable body-beat scenes for deep-explainer reels.
 *
 * ChipGrid   — titled grid of concept chips (enumeration beats).
 *              Props: title, chips[], sparkLine
 *
 * DeckPattern — rhetorical layout dispatcher.
 *   pattern='divergence' → two-column split: what engineering fixes vs what architecture can't
 *   pattern='threshold'  → centred concept-line card: a line the validator must not cross
 *
 * Both sit on the Claude cream stage (#FAF9F5), use EB Garamond for body type,
 * and reserve terracotta exclusively as the one accent spark.
 *
 * Registered as Compositions 'ChipGrid' and 'DeckPattern' in Root.tsx.
 * Duration-agnostic — compile.py conforms to actual_duration_s.
 */

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;
const clamp = (v: number, lo: number, hi: number) => Math.min(hi, Math.max(lo, v));

// ─────────────────────────────────────────────────────────────────────────────
// ChipGrid
// ─────────────────────────────────────────────────────────────────────────────

export const chipGridSchema = z.object({
  title:     z.string().default('The Categories'),
  chips:     z.array(z.string()).default([]),
  sparkLine: z.string().default(''),
});
export type ChipGridProps = z.infer<typeof chipGridSchema>;

export const ChipGrid: React.FC<ChipGridProps> = ({ title, chips, sparkLine }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const titleIn = spring({ frame, fps, config: { damping: 28, stiffness: 140, mass: 0.8 } });
  const sparkIn = spring({
    frame: frame - (chips.length + 3) * 8,
    fps,
    config: { damping: 28, stiffness: 140, mass: 0.8 },
  });

  // 2-column grid; odd last chip spans both columns
  const cols = 2;
  const isOddLast = chips.length % 2 === 1;

  return (
    <AbsoluteFill style={{
      background: CLAUDE.PAGE,
      alignItems: 'center',
      justifyContent: 'center',
      flexDirection: 'column',
      padding: '0 140px',
    }}>
      {/* Title */}
      <div style={{
        fontFamily: SERIF,
        fontSize: 52,
        fontWeight: 600,
        color: CLAUDE.INK,
        textAlign: 'center',
        marginBottom: 52,
        opacity: clamp(titleIn, 0, 1),
        transform: `translateY(${(1 - clamp(titleIn, 0, 1)) * 24}px)`,
        lineHeight: 1.2,
      }}>
        {title}
      </div>

      {/* Chip grid */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: `repeat(${cols}, 1fr)`,
        gap: 28,
        width: '100%',
        maxWidth: 1440,
      }}>
        {chips.map((chip, i) => {
          const chipIn = spring({
            frame: frame - (i + 2) * 8,
            fps,
            config: { damping: 28, stiffness: 140, mass: 0.8 },
          });
          const spanFull = isOddLast && i === chips.length - 1;
          return (
            <div key={i} style={{
              background: CLAUDE.CARD,
              border: `1.5px solid ${CLAUDE.BORDER}`,
              borderLeft: `5px solid ${CLAUDE.SPARK}`,
              borderRadius: 14,
              padding: '26px 36px',
              fontFamily: SERIF,
              fontSize: 60,
              color: CLAUDE.INK,
              lineHeight: 1.4,
              opacity: clamp(chipIn, 0, 1),
              transform: `translateY(${(1 - clamp(chipIn, 0, 1)) * 18}px)`,
              boxShadow: '0 4px 18px rgba(61,57,41,0.09)',
              ...(spanFull ? { gridColumn: '1 / -1', textAlign: 'center' as const } : {}),
            }}>
              {chip}
            </div>
          );
        })}
      </div>

      {/* SparkLine */}
      {sparkLine && (
        <div style={{
          marginTop: 52,
          fontFamily: SANS,
          fontSize: 36,
          color: CLAUDE.INK,
          fontStyle: 'italic',
          textAlign: 'center',
          opacity: clamp(sparkIn, 0, 1),
          transform: `translateY(${(1 - clamp(sparkIn, 0, 1)) * 14}px)`,
        }}>
          {sparkLine}
        </div>
      )}
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// DeckPattern
// ─────────────────────────────────────────────────────────────────────────────

const columnSchema = z.object({ label: z.string(), note: z.string() });

export const deckPatternSchema = z.object({
  pattern:   z.enum(['divergence', 'threshold']).default('divergence'),
  title:     z.string().default(''),
  left:      columnSchema.optional(),
  right:     columnSchema.optional(),
  note:      z.string().optional(),
  sparkLine: z.string().default(''),
});
export type DeckPatternProps = z.infer<typeof deckPatternSchema>;

export const DeckPattern: React.FC<DeckPatternProps> = ({
  pattern, title, left, right, note, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const cfg = { damping: 28, stiffness: 140, mass: 0.8 };
  const titleIn = spring({ frame,           fps, config: cfg });
  const leftIn  = spring({ frame: frame - 12, fps, config: cfg });
  const rightIn = spring({ frame: frame - 22, fps, config: cfg });
  const sparkIn = spring({ frame: frame - 36, fps, config: cfg });

  // ── divergence ──────────────────────────────────────────────────────────
  if (pattern === 'divergence') {
    return (
      <AbsoluteFill style={{
        background: CLAUDE.PAGE,
        alignItems: 'center',
        justifyContent: 'center',
        flexDirection: 'column',
        padding: '0 100px',
      }}>
        {/* Title */}
        <div style={{
          fontFamily: SERIF,
          fontSize: 46,
          fontWeight: 600,
          color: CLAUDE.INK,
          textAlign: 'center',
          marginBottom: 60,
          opacity: clamp(titleIn, 0, 1),
          transform: `translateY(${(1 - clamp(titleIn, 0, 1)) * 22}px)`,
          lineHeight: 1.2,
        }}>
          {title}
        </div>

        {/* Two-column split */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: '1fr 1px 1fr',
          width: '100%',
          maxWidth: 1560,
          alignItems: 'stretch',
        }}>
          {/* Left column */}
          <div style={{
            padding: '36px 60px 36px 0',
            opacity: clamp(leftIn, 0, 1),
            transform: `translateX(${(1 - clamp(leftIn, 0, 1)) * -28}px)`,
          }}>
            <div style={{
              fontFamily: SANS,
              fontSize: 36,
              fontWeight: 700,
              color: CLAUDE.INK,
              letterSpacing: '0.16em',
              textTransform: 'uppercase' as const,
              marginBottom: 20,
            }}>
              {left?.label}
            </div>
            <div style={{
              fontFamily: SERIF,
              fontSize: 60,
              color: CLAUDE.INK,
              lineHeight: 1.55,
            }}>
              {left?.note}
            </div>
          </div>

          {/* Divider */}
          <div style={{
            background: CLAUDE.BORDER,
            width: 1,
            opacity: clamp(leftIn, 0, 1),
          }} />

          {/* Right column — label in terracotta */}
          <div style={{
            padding: '36px 0 36px 60px',
            opacity: clamp(rightIn, 0, 1),
            transform: `translateX(${(1 - clamp(rightIn, 0, 1)) * 28}px)`,
          }}>
            <div style={{
              fontFamily: SANS,
              fontSize: 36,
              fontWeight: 700,
              color: CLAUDE.INK,
              letterSpacing: '0.16em',
              textTransform: 'uppercase' as const,
              marginBottom: 20,
            }}>
              {right?.label}
            </div>
            <div style={{
              fontFamily: SERIF,
              fontSize: 60,
              color: CLAUDE.INK,
              lineHeight: 1.55,
            }}>
              {right?.note}
            </div>
          </div>
        </div>

        {/* SparkLine */}
        {sparkLine && (
          <div style={{
            marginTop: 60,
            fontFamily: SANS,
            fontSize: 36,
            color: CLAUDE.INK,
            fontStyle: 'italic',
            textAlign: 'center',
            opacity: clamp(sparkIn, 0, 1),
            transform: `translateY(${(1 - clamp(sparkIn, 0, 1)) * 14}px)`,
          }}>
            {sparkLine}
          </div>
        )}
      </AbsoluteFill>
    );
  }

  // ── threshold ────────────────────────────────────────────────────────────
  return (
    <AbsoluteFill style={{
      background: CLAUDE.PAGE,
      alignItems: 'center',
      justifyContent: 'center',
      flexDirection: 'column',
      padding: '0 180px',
    }}>
      {/* Title */}
      <div style={{
        fontFamily: SERIF,
        fontSize: 58,
        fontWeight: 600,
        color: CLAUDE.INK,
        textAlign: 'center',
        marginBottom: 52,
        opacity: clamp(titleIn, 0, 1),
        transform: `translateY(${(1 - clamp(titleIn, 0, 1)) * 22}px)`,
        lineHeight: 1.2,
      }}>
        {title}
      </div>

      {/* Concept card */}
      {note && (
        <div style={{
          background: CLAUDE.CARD,
          border: `1.5px solid ${CLAUDE.BORDER}`,
          borderLeft: `6px solid ${CLAUDE.SPARK}`,
          borderRadius: 16,
          padding: '40px 60px',
          fontFamily: SERIF,
          fontSize: 60,
          color: CLAUDE.INK,
          lineHeight: 1.6,
          maxWidth: 1200,
          textAlign: 'center',
          opacity: clamp(leftIn, 0, 1),
          transform: `translateY(${(1 - clamp(leftIn, 0, 1)) * 24}px)`,
          boxShadow: '0 8px 36px rgba(61,57,41,0.10)',
        }}>
          {note}
        </div>
      )}

      {/* SparkLine */}
      {sparkLine && (
        <div style={{
          marginTop: 52,
          fontFamily: SANS,
          fontSize: 36,
          color: CLAUDE.INK,
          fontStyle: 'italic',
          textAlign: 'center',
          opacity: clamp(sparkIn, 0, 1),
          transform: `translateY(${(1 - clamp(sparkIn, 0, 1)) * 14}px)`,
        }}>
          {sparkLine}
        </div>
      )}
    </AbsoluteFill>
  );
};
