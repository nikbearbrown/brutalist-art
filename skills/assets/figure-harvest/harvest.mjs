#!/usr/bin/env node
// harvest.mjs — figure-harvest classifier.
// Mines a facts/<topic> knowledge slice for figures WORTH REDRAWING.
// Core idea: a Wikipedia editor including an image is a usefulness signal.
// We keep the *redrawable concept figures* (diagrams/charts/schematics) and
// drop logos (trademark) and photographs (can't be redrawn as a diagram).
// Deterministic. No AI, no network.
//
//   node figure-harvest/harvest.mjs --topic physics [--book books/neu-physics] [--top 60]
//
// Outputs (next to this script):
//   figure-harvest/out/<topic>-figures.json   ranked doable candidates
//   figure-harvest/out/<topic>-figures.md      human plan + stats

import { readFileSync, writeFileSync, mkdirSync, existsSync, readdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = join(HERE, '..');                 // bear-textbooks/
const arg = (k, d) => { const i = process.argv.indexOf(k); return i > -1 ? process.argv[i + 1] : d; };
const TOPIC = arg('--topic', null);
const BOOK = arg('--book', null);              // optional, relative to ROOT
const TOP = parseInt(arg('--top', '60'), 10);
if (!TOPIC) { console.error('usage: harvest.mjs --topic <name> [--book <path>] [--top N]'); process.exit(1); }

const FACTS = join(ROOT, 'facts', TOPIC);
if (!existsSync(join(FACTS, 'terms.json'))) { console.error(`no facts/${TOPIC}/terms.json`); process.exit(1); }
const terms = JSON.parse(readFileSync(join(FACTS, 'terms.json'), 'utf8'));
const graph = existsSync(join(FACTS, 'graph.json')) ? JSON.parse(readFileSync(join(FACTS, 'graph.json'), 'utf8')) : { nodes: [] };

// foundational-ness: in_degree by normalized term
const norm = (s) => (s || '').toLowerCase().replace(/\([^)]*\)/g, ' ').replace(/[^a-z0-9 ]/g, ' ').replace(/\s+/g, ' ').trim();
const deg = new Map(); for (const n of graph.nodes || []) deg.set(norm(n.term), n.in_degree || 0);

// optional book vocabulary for relevance
let bookVocab = null;
if (BOOK) {
  const chDir = join(ROOT, BOOK, 'chapters');
  if (existsSync(chDir)) {
    bookVocab = readdirSync(chDir).filter(f => f.endsWith('.md'))
      .map(f => readFileSync(join(chDir, f), 'utf8').toLowerCase()).join('\n');
  }
}

// --- classifiers ---
const LOGO = /logo|wordmark|brandmark|\bseal\b|emblem|coat[ _-]of[ _-]arms|prize medal|\bflag\b|\bbadge\b|\bEPJ\b|journal/i;
const VIDEO_EXT = /\.(webm|ogv|ogg|mp4|mov|gif)$/i;
const PHOTO_EXT = /\.(jpe?g|webp|tiff?)$/i;
const DIAGRAM_HINT = /diagram|chart|graph|plot|schematic|figure|curve|wave|circuit|field lines?|ray|force|free.body|vector|orbit|spectr|model|cycle|geometr|trajector|pendulum|lens|prism|grid|sine|cosine|\bgraph\b|feynman|band structure|phase|potential|distribution|histogram|hierarch|flow|tree|map\b|matrix|continuum|timeline/i;

const out = [];
let nLogo = 0, nPhoto = 0, nDoable = 0, nOther = 0;
const seen = new Set();
for (const t of terms) {
  for (const m of t.get_media ? [] : (t.media || [])) {
    const file = m.file || '', ty = m.type || '', st = m.strategy || '', url = m.commons_url || '';
    const term = t.term || '';
    const n = file.toLowerCase();
    if (LOGO.test(n) || LOGO.test(term)) { nLogo++; continue; }
    if (VIDEO_EXT.test(n)) { nOther++; continue; }
    if (PHOTO_EXT.test(n) || ty === 'photo') { nPhoto++; continue; }
    const isSvg = n.endsWith('.svg');
    const looksDiagram = isSvg || ty === 'diagram' || st === 'redraw-svg' || DIAGRAM_HINT.test(file) || DIAGRAM_HINT.test(term);
    if (!looksDiagram) { nOther++; continue; }
    nDoable++;
    const key = norm(term) + '|' + n;
    if (seen.has(key)) continue; seen.add(key);
    const rank = deg.get(norm(term)) || 0;
    const relevant = bookVocab ? bookVocab.includes(norm(term)) && norm(term).length > 3 : null;
    out.push({ term, file, type: ty, strategy: st, commons_url: url, foundational: rank, in_book: relevant });
  }
}

out.sort((a, b) => (b.in_book === true) - (a.in_book === true) || b.foundational - a.foundational || a.term.localeCompare(b.term));

const OUT = join(HERE, 'out'); mkdirSync(OUT, { recursive: true });
writeFileSync(join(OUT, `${TOPIC}-figures.json`), JSON.stringify(out, null, 2));

// markdown plan
const total = nLogo + nPhoto + nDoable + nOther;
let md = `# Figure Harvest — ${TOPIC}\n\n`;
md += `Source: \`facts/${TOPIC}/\` · ${total} media references found.\n\n`;
md += `| class | count | action |\n|---|--:|---|\n`;
md += `| **doable diagrams** | ${nDoable} | redraw in house style |\n`;
md += `| logos / marks | ${nLogo} | skip — trademark |\n`;
md += `| photographs | ${nPhoto} | skip — can't redraw a photo as a diagram |\n`;
md += `| other / uncertain | ${nOther} | review |\n\n`;
if (BOOK) md += `Book relevance filter: \`${BOOK}\` — ${out.filter(o => o.in_book).length} candidates appear in the book.\n\n`;
md += `---\n\n## Top ${Math.min(TOP, out.length)} candidates to redraw${BOOK ? ' (book-relevant first, then most foundational)' : ' (most foundational first)'}\n\n`;
md += `| # | concept | foundational | in book | reference (Commons) |\n|--:|---|--:|:--:|---|\n`;
out.slice(0, TOP).forEach((o, i) => {
  md += `| ${i + 1} | ${o.term} | ${o.foundational} | ${o.in_book === true ? '✓' : ''} | [${o.file}](${o.commons_url}) |\n`;
});
md += `\n> "Foundational" = how many other ${TOPIC} pages link this concept (from graph.json) — a proxy for usefulness. The Commons link is a visual reference only; the figure is redrawn fresh in the book's house style, never copied.\n`;
writeFileSync(join(OUT, `${TOPIC}-figures.md`), md);

console.log(`${TOPIC}: ${total} refs → doable ${nDoable} | logos ${nLogo} | photos ${nPhoto} | other ${nOther}`);
if (BOOK) console.log(`book-relevant doable: ${out.filter(o => o.in_book).length}`);
console.log(`-> figure-harvest/out/${TOPIC}-figures.json`);
console.log(`-> figure-harvest/out/${TOPIC}-figures.md`);
