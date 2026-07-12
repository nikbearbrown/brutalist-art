// The 12 --onda-* CSS variables remapped to the teardown palette (DESIGN.md).
// onda ships dark (near-black canvas, dusty-rose accent); setting these on a wrapper
// flips any onda component to the teardown light look: white ground, ink text, ONE red
// accent. onda's "the accent is earned, one focal moment" IS teardown's one-red rule,
// so the retint is native — the earned accent simply becomes red.
export const ONDA_VARS: React.CSSProperties = {
  ['--onda-bg' as any]: '#FFFFFF',
  ['--onda-surface' as any]: '#FFFFFF',
  ['--onda-surface-2' as any]: '#F0EEE9',
  ['--onda-border' as any]: '#D4D4D4',
  ['--onda-border-lit' as any]: '#545454',
  ['--onda-text' as any]: '#2A1A0E',
  ['--onda-dim' as any]: '#545454',
  ['--onda-faint' as any]: '#545454',
  ['--onda-accent' as any]: '#C8102E',
  ['--onda-accent-soft' as any]: '#F6D8DC',
  ['--onda-font-display' as any]: 'Montserrat, "Helvetica Neue", Arial, sans-serif',
  ['--onda-font-body' as any]: '"EB Garamond", Georgia, serif',
};

// teardown tokens for the riff chrome (cards, labels) — kept in sync with DESIGN.md.
export const TD = {
  ground: '#FFFFFF',
  ink: '#2A1A0E',
  red: '#C8102E',
  gray: '#545454',
  hairline: '#D4D4D4',
  redwash: '#F6D8DC',
  display: 'Montserrat, "Helvetica Neue", Arial, sans-serif',
  serif: '"EB Garamond", Georgia, serif',
} as const;
