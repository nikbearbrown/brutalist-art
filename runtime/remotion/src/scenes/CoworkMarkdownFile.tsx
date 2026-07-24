import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * CoworkMarkdownFile — two animated .md file cards for Act 2 of claude-liam-one-hour-on-cowork.
 *
 * WHAT: Shows about-me.md and anti-AI-writing-style.md as ink-on-cream cards
 *       that slide in sequentially. A bottom caption reinforces the "files beat prompts" rule.
 * WHEN: Act 2 body beat — file-system beat, NOT a Claude UI beat.
 * PROPS: file1Name, file1Lines[], file2Name, file2Lines[], caption, sparkLine, folderLabel
 */

const fileLineSchema = z.string();

export const coworkMarkdownFileSchema = z.object({
  file1Name:   z.string().default('about-me.md'),
  file1Lines:  z.array(fileLineSchema).default(['Who I am, how I write', 'What I don\'t want Claude doing', 'My preferred output formats']),
  file2Name:   z.string().default('anti-AI-writing-style.md'),
  file2Lines:  z.array(fileLineSchema).default(['Phrases to avoid', 'Patterns to skip', 'Tone calibration']),
  caption:     z.string().default('1 great .md file > 50 random uploads'),
  sparkLine:   z.string().default('Files beat prompts.'),
  folderLabel: z.string().default('@NikBearBrown'),
});
export type CoworkMarkdownFileProps = z.infer<typeof coworkMarkdownFileSchema>;

const CARD_APPEAR_1 = 4;  // frame when card 1 starts sliding in
const CARD_APPEAR_2 = 18; // frame when card 2 starts sliding in
const CAPTION_APPEAR = 34;

const FileCard: React.FC<{
  filename: string;
  lines: string[];
  slideIn: number; // spring 0→1
  accent?: boolean;
}> = ({ filename, lines, slideIn, accent = false }) => {
  const { width: vw, height: vh } = useVideoConfig();
  const cardW = vw * 0.37;
  const cardH = vh * 0.52;

  return (
    <div style={{
      width: cardW,
      height: cardH,
      background: CLAUDE.INK,
      borderRadius: 12,
      padding: `${vh * 0.028}px ${vw * 0.022}px`,
      boxShadow: '0 8px 32px rgba(61,57,41,0.18)',
      opacity: slideIn,
      transform: `translateY(${(1 - slideIn) * 36}px)`,
      display: 'flex',
      flexDirection: 'column',
      gap: vh * 0.018,
    }}>
      {/* Header row: file icon + name */}
      <div style={{ display: 'flex', alignItems: 'center', gap: vw * 0.012 }}>
        {/* Markdown file icon (M↓) */}
        <div style={{
          width: vw * 0.035,
          height: vh * 0.055,
          background: accent ? CLAUDE.SPARK : '#5A5642',
          borderRadius: 5,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          flexShrink: 0,
        }}>
          <span style={{
            fontFamily: CLAUDE_FONT.ui,
            fontSize: Math.max(9, vh * 0.018),
            color: '#FFFFFF',
            fontWeight: 700,
            letterSpacing: 0,
          }}>md</span>
        </div>
        <span style={{
          fontFamily: CLAUDE_FONT.mono || CLAUDE_FONT.ui,
          fontSize: Math.max(12, vh * 0.022),
          color: CLAUDE.SPARK,
          fontWeight: 600,
          letterSpacing: '-0.01em',
          overflow: 'hidden',
          textOverflow: 'ellipsis',
          whiteSpace: 'nowrap',
        }}>
          {filename}
        </span>
      </div>

      {/* Divider */}
      <div style={{ height: 1, background: '#4A4738', flexShrink: 0 }} />

      {/* Content lines */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: vh * 0.014, flex: 1 }}>
        {lines.map((line, i) => (
          <div key={i} style={{ display: 'flex', alignItems: 'flex-start', gap: vw * 0.008 }}>
            <span style={{
              color: CLAUDE.SPARK,
              fontFamily: CLAUDE_FONT.ui,
              fontSize: Math.max(10, vh * 0.018),
              flexShrink: 0,
              marginTop: 1,
            }}>—</span>
            <span style={{
              color: '#D4CEB8',
              fontFamily: CLAUDE_FONT.ui,
              fontSize: Math.max(12, vh * 0.022),
              lineHeight: 1.4,
            }}>
              {line}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};

export const CoworkMarkdownFile: React.FC<CoworkMarkdownFileProps> = ({
  file1Name, file1Lines, file2Name, file2Lines, caption, sparkLine, folderLabel,
}) => {
  const frame = useCurrentFrame();
  const { fps, width: vw, height: vh } = useVideoConfig();

  const card1In = spring({ frame: frame - CARD_APPEAR_1, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });
  const card2In = spring({ frame: frame - CARD_APPEAR_2, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });
  const captionIn = spring({ frame: frame - CAPTION_APPEAR, fps, config: { damping: 28, stiffness: 140, mass: 0.8 } });

  return (
    <AbsoluteFill style={{ backgroundColor: CLAUDE.PAGE, overflow: 'hidden' }}>
      {/* Spark line — top */}
      <div style={{
        position: 'absolute',
        top: vh * 0.055,
        left: 0, right: 0,
        textAlign: 'center',
        fontFamily: CLAUDE_FONT.serif,
        fontSize: Math.max(16, vh * 0.028),
        fontStyle: 'italic',
        color: CLAUDE.INK_SOFT,
        opacity: card1In * 0.7,
      }}>
        {sparkLine}
      </div>

      {/* Two-card layout */}
      <div style={{
        position: 'absolute',
        top: vh * 0.12,
        left: 0, right: 0,
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'flex-start',
        gap: vw * 0.04,
      }}>
        <FileCard filename={file1Name} lines={file1Lines} slideIn={card1In} />
        <FileCard filename={file2Name} lines={file2Lines} slideIn={card2In} accent />
      </div>

      {/* Caption */}
      <div style={{
        position: 'absolute',
        bottom: vh * 0.1,
        left: 0, right: 0,
        textAlign: 'center',
        fontFamily: CLAUDE_FONT.serif,
        fontSize: Math.max(18, vh * 0.032),
        fontWeight: 600,
        color: CLAUDE.INK,
        opacity: captionIn,
        transform: `translateY(${(1 - captionIn) * 10}px)`,
        padding: '0 15%',
      }}>
        {caption}
      </div>

      {/* Terracotta rule */}
      <div style={{
        position: 'absolute',
        bottom: vh * 0.075,
        left: vw * 0.08,
        width: vw * 0.07,
        height: 2,
        background: CLAUDE.SPARK,
        opacity: captionIn,
      }} />

      {/* Folder chip */}
      <div style={{
        position: 'absolute',
        right: vw * 0.04,
        bottom: vh * 0.03,
        fontFamily: CLAUDE_FONT.ui,
        fontSize: Math.max(12, vh * 0.015),
        fontWeight: 600,
        color: CLAUDE.INK_SOFT,
        opacity: 0.2,
      }}>
        {folderLabel}
      </div>
    </AbsoluteFill>
  );
};
