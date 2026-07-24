import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * CoworkFolderTree — animated folder tree for Act 4 of claude-liam-one-hour-on-cowork.
 *
 * WHAT: Root folder + four subfolders draw on sequentially. The write-permitted
 *       folder (accent=true) highlights in terracotta — ONE accent, SPARK-LINE LAW.
 * WHEN: Act 4 body beat — file-system beat, NOT a Claude UI beat.
 * PROPS: rootName, folders[{name, accent}], caption, sparkLine, folderLabel
 */

const folderItemSchema = z.object({
  name:   z.string(),
  accent: z.boolean().default(false),
});

export const coworkFolderTreeSchema = z.object({
  rootName:    z.string().default('CLAUDE COWORK'),
  folders:     z.array(folderItemSchema).default([
    { name: 'ABOUT ME',       accent: false },
    { name: 'TEMPLATES',      accent: false },
    { name: 'PROJECTS',       accent: false },
    { name: 'CLAUDE OUTPUTS', accent: true  },
  ]),
  caption:     z.string().default('Real read/write access.'),
  sparkLine:   z.string().default('Keep it tight.'),
  folderLabel: z.string().default('@NikBearBrown'),
});
export type CoworkFolderTreeProps = z.infer<typeof coworkFolderTreeSchema>;

// Each subfolder draws in at a staggered frame offset
const ROOT_APPEAR      = 2;
const SUBFOLDER_STRIDE = 8; // frames between each subfolder
const CAPTION_APPEAR   = ROOT_APPEAR + 4 * SUBFOLDER_STRIDE + 10;

const FolderIcon: React.FC<{ size: number; accent: boolean }> = ({ size, accent }) => (
  <svg width={size} height={size * 0.8} viewBox="0 0 24 20" style={{ flexShrink: 0 }}>
    <path
      d="M2 4 L2 17 Q2 18 3 18 L21 18 Q22 18 22 17 L22 6 Q22 5 21 5 L11 5 L9 3 Q8.5 2 7.5 2 L3 2 Q2 2 2 4 Z"
      fill={accent ? CLAUDE.SPARK : CLAUDE.INK}
      opacity={accent ? 1 : 0.85}
    />
  </svg>
);

export const CoworkFolderTree: React.FC<CoworkFolderTreeProps> = ({
  rootName, folders, caption, sparkLine, folderLabel,
}) => {
  const frame = useCurrentFrame();
  const { fps, width: vw, height: vh } = useVideoConfig();

  const rootIn    = spring({ frame: frame - ROOT_APPEAR,   fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });
  const captionIn = spring({ frame: frame - CAPTION_APPEAR, fps, config: { damping: 28, stiffness: 140, mass: 0.8 } });

  const subfolderSprings = folders.map((_, i) =>
    spring({ frame: frame - (ROOT_APPEAR + (i + 1) * SUBFOLDER_STRIDE), fps, config: { damping: 26, stiffness: 130, mass: 0.9 } })
  );

  const iconSize = Math.max(28, vw * 0.028);
  const rootFontSize  = Math.max(22, vh * 0.038);
  const subFontSize   = Math.max(18, vh * 0.030);
  const treeLeft      = vw * 0.18;
  const nodeGap       = vh * 0.072;
  const rootY         = vh * 0.24;
  const branchX       = treeLeft + vw * 0.015;
  const subX          = branchX  + vw * 0.038;

  // Vertical line endpoints
  const lineTop    = rootY + vh * 0.035;
  const lineBottom = rootY + nodeGap * folders.length;

  return (
    <AbsoluteFill style={{ backgroundColor: CLAUDE.PAGE, overflow: 'hidden' }}>
      {/* Spark line */}
      <div style={{
        position: 'absolute',
        top: vh * 0.055,
        left: 0, right: 0,
        textAlign: 'center',
        fontFamily: CLAUDE_FONT.serif,
        fontSize: Math.max(16, vh * 0.028),
        fontStyle: 'italic',
        color: CLAUDE.INK_SOFT,
        opacity: rootIn * 0.7,
      }}>
        {sparkLine}
      </div>

      {/* SVG for branch lines */}
      <svg
        width={vw} height={vh}
        viewBox={`0 0 ${vw} ${vh}`}
        style={{ position: 'absolute', top: 0, left: 0, pointerEvents: 'none' }}
      >
        {/* Vertical trunk */}
        {subfolderSprings.length > 0 && (
          <line
            x1={branchX} y1={lineTop}
            x2={branchX} y2={Math.min(lineBottom, lineTop + subfolderSprings.reduce((acc, s, i) => i < folders.length ? Math.max(acc, s > 0.01 ? (i + 1) * nodeGap : acc) : acc, 0))}
            stroke={CLAUDE.INK} strokeWidth={1.5} strokeOpacity={0.3}
            style={{ opacity: rootIn }}
          />
        )}
        {/* Horizontal branches */}
        {folders.map((_, i) => (
          <line key={i}
            x1={branchX} y1={rootY + nodeGap * (i + 1) + vh * 0.01}
            x2={subX - vw * 0.005} y2={rootY + nodeGap * (i + 1) + vh * 0.01}
            stroke={CLAUDE.INK} strokeWidth={1.5} strokeOpacity={0.3}
            style={{ opacity: subfolderSprings[i] }}
          />
        ))}
      </svg>

      {/* Root folder */}
      <div style={{
        position: 'absolute',
        left: treeLeft,
        top: rootY,
        display: 'flex',
        alignItems: 'center',
        gap: vw * 0.015,
        opacity: rootIn,
        transform: `translateX(${(1 - rootIn) * -20}px)`,
      }}>
        <FolderIcon size={iconSize * 1.25} accent={false} />
        <span style={{
          fontFamily: CLAUDE_FONT.serif,
          fontSize: rootFontSize,
          fontWeight: 700,
          color: CLAUDE.INK,
          letterSpacing: '-0.01em',
        }}>
          {rootName}
        </span>
      </div>

      {/* Subfolders */}
      {folders.map((folder, i) => {
        const sp = subfolderSprings[i];
        return (
          <div key={i} style={{
            position: 'absolute',
            left: subX,
            top: rootY + nodeGap * (i + 1),
            display: 'flex',
            alignItems: 'center',
            gap: vw * 0.012,
            opacity: sp,
            transform: `translateX(${(1 - sp) * -16}px)`,
          }}>
            <FolderIcon size={iconSize} accent={folder.accent} />
            <span style={{
              fontFamily: CLAUDE_FONT.ui,
              fontSize: subFontSize,
              fontWeight: folder.accent ? 700 : 500,
              color: folder.accent ? CLAUDE.SPARK : CLAUDE.INK,
              letterSpacing: folder.accent ? '0.02em' : 0,
            }}>
              {folder.name}
            </span>
            {folder.accent && (
              <span style={{
                fontFamily: CLAUDE_FONT.ui,
                fontSize: Math.max(11, vh * 0.018),
                color: CLAUDE.INK_SOFT,
                marginLeft: vw * 0.008,
                opacity: 0.6,
              }}>
                write-permitted
              </span>
            )}
          </div>
        );
      })}

      {/* Caption */}
      <div style={{
        position: 'absolute',
        bottom: vh * 0.12,
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
        bottom: vh * 0.095,
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
