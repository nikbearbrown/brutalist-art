import { Config } from '@remotion/cli/config';
import path from 'path';

Config.setVideoImageFormat('jpeg');
Config.setOverwriteOutput(true);

// The onda bench lives OUTSIDE this project (../../vox/remotion/_bench/onda), so onda's
// bare imports (@remotion/paths, @remotion/motion-blur, react, remotion, zod, ...) resolve
// relative to onda's own folder and walk up to ~/ — never seeing THIS project's
// node_modules. Force webpack to resolve every bare module from here, and pin the
// singletons (react/react-dom/remotion) so there is exactly one copy of each — which also
// clears the "React context/hooks not working" version-mismatch warning.
//
// The project root is PINNED as an absolute path, deliberately. Neither of the obvious
// alternatives works here:
//   • process.cwd()  → only correct when remotion is launched FROM the project dir; run it
//     with an absolute path from anywhere else and the aliases point at nothing.
//   • __dirname      → Remotion evaluates this config from inside node_modules/@remotion/
//     cli/dist, so __dirname resolves THERE, aliasing 'remotion' to a path that doesn't
//     exist → "Field 'browser' doesn't contain a valid alias configuration".
// Pinning the absolute root makes the render cwd-independent (run it from any directory).
// Override with RIFF_PROJECT if the repo ever moves.
const PROJECT = process.env.RIFF_PROJECT ||
  '$ART_HOME/skills/make/component-showcase/remotion';
const NM = path.join(PROJECT, 'node_modules');

Config.overrideWebpackConfig((current) => ({
  ...current,
  resolve: {
    ...current.resolve,
    modules: [NM, 'node_modules', ...((current.resolve && current.resolve.modules) || [])],
    alias: {
      ...((current.resolve && current.resolve.alias) || {}),
      react: path.join(NM, 'react'),
      'react-dom': path.join(NM, 'react-dom'),
      remotion: path.join(NM, 'remotion'),
      zod: path.join(NM, 'zod'),
      // Explicit aliases for all @remotion/* used by onda components imported from vox/.
      // Without these, webpack walks up from vox/'s dir and misses this project's node_modules.
      '@remotion/motion-blur': path.join(NM, '@remotion/motion-blur'),
      '@remotion/paths': path.join(NM, '@remotion/paths'),
      '@remotion/media-utils': path.join(NM, '@remotion/media-utils'),
      '@remotion/player': path.join(NM, '@remotion/player'),
    },
  },
}));
