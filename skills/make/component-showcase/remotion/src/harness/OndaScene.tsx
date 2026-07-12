import React from 'react';
import { AbsoluteFill } from 'remotion';
import { ONDA_DATA_MAP } from './registry';
import { DATA_FIXTURES } from '../fixtures/data';
import { ONDA_VARS, TD } from '../teardown';

// Renders-what-renders: a scene that throws at render time shows a FAIL card instead of
// crashing the whole reel, and logs the slug + reason to the console. (v1 logging is the
// console; a render-log.json wrapper is a later Generate unit.)
class SceneBoundary extends React.Component<
  { slug: string; children: React.ReactNode },
  { failed: boolean }
> {
  state = { failed: false };
  static getDerivedStateFromError() {
    return { failed: true };
  }
  componentDidCatch(err: unknown) {
    // eslint-disable-next-line no-console
    console.error(`[riff] scene FAILED to render: ${this.props.slug}`, err);
  }
  render() {
    if (this.state.failed) {
      return (
        <div style={{ textAlign: 'center', fontFamily: TD.display, color: TD.red }}>
          <div style={{ fontSize: 40, fontWeight: 700 }}>render failed</div>
          <div style={{ fontSize: 26, color: TD.gray, marginTop: 10 }}>{this.props.slug}</div>
        </div>
      );
    }
    return this.props.children as React.ReactElement;
  }
}

export const OndaScene: React.FC<{ slug: string; propsOverride?: Record<string, unknown> }> = ({
  slug,
  propsOverride,
}) => {
  const entry = ONDA_DATA_MAP[slug];
  if (!entry) {
    return (
      <AbsoluteFill style={{ background: TD.ground, alignItems: 'center', justifyContent: 'center' }}>
        <div style={{ fontFamily: TD.display, color: TD.red, fontSize: 32 }}>unknown slug: {slug}</div>
      </AbsoluteFill>
    );
  }
  // Merge the themed fixture with any per-segment override (the tour passes conform timing +
  // content per template); override wins. Non-schema keys (e.g. `note`) are dropped by parse.
  const props = entry.schema.parse({ ...(DATA_FIXTURES[slug] ?? {}), ...(propsOverride ?? {}) });
  const Comp = entry.Component;
  return (
    <AbsoluteFill
      style={{
        ...ONDA_VARS,
        background: 'var(--onda-bg)',
        alignItems: 'center',
        justifyContent: 'center',
        padding: 80,
      }}
    >
      <SceneBoundary slug={slug}>
        <Comp {...props} />
      </SceneBoundary>
    </AbsoluteFill>
  );
};
