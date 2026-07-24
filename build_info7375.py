#!/usr/bin/env python3
"""
build_info7375.py — Resumable batch build for all INFO 7375 how-to reels.

Run from books/:
  python3 brutalist-art/build_info7375.py              # build all unbuilt
  python3 brutalist-art/build_info7375.py --dry-run    # preview what would run
  python3 brutalist-art/build_info7375.py --from claude-liam-a6-03-name-generation
  python3 brutalist-art/build_info7375.py --only a9    # build only a9-* series
  python3 brutalist-art/build_info7375.py --force      # rebuild even if mp4 exists

A build is considered done when mp4/ contains any .mp4 file.
Individual failures are recorded and the batch continues so every renderable reel
is attempted in a single run.
"""

import subprocess, os, sys, argparse

# (book_subpath_from_books, slug)
REELS = [
    # A2 — Plan It Like a PM
    ("brutalist-art/youtube", "claude-liam-a2-01-pick-a-lane"),
    ("brutalist-art/youtube", "claude-liam-a2-02-gap-analysis"),
    ("brutalist-art/youtube", "claude-liam-a2-03-prd-problem-solution"),
    ("brutalist-art/youtube", "claude-liam-a2-04-prd-stories-metrics"),
    ("brutalist-art/youtube", "claude-liam-a2-05-agent-design"),
    ("brutalist-art/youtube", "claude-liam-a2-06-n8n-mvp"),
    ("brutalist-art/youtube", "claude-liam-a2-07-submit"),
    # A3 — Shop for Ingredients
    ("brutalist-art/youtube", "claude-liam-a3-01-pick-sources"),
    ("brutalist-art/youtube", "claude-liam-a3-02-install-n8n"),
    ("brutalist-art/youtube", "claude-liam-a3-03-wire-sources"),
    ("brutalist-art/youtube", "claude-liam-a3-04-clean-save-export"),
    ("brutalist-art/youtube", "claude-liam-a3-05-quality-and-craft"),
    ("brutalist-art/youtube", "claude-liam-a3-06-documentation"),
    ("brutalist-art/youtube", "claude-liam-a3-07-demo-and-submit"),
    # A4 — Make It Smart
    ("brutalist-art/youtube", "claude-liam-a4-01-add-intelligence"),
    ("brutalist-art/youtube", "claude-liam-a4-02-error-handling"),
    ("brutalist-art/youtube", "claude-liam-a4-03-real-output"),
    ("brutalist-art/youtube", "claude-liam-a4-04-output-gallery"),
    ("brutalist-art/youtube", "claude-liam-a4-05-scale-test"),
    ("brutalist-art/youtube", "claude-liam-a4-06-professional-package"),
    ("brutalist-art/youtube", "claude-liam-a4-07-demo-and-submit"),
    # A5 — Say What It Is
    ("brutalist-art/youtube", "claude-liam-a5-01-one-sentence"),
    ("brutalist-art/youtube", "claude-liam-a5-02-user-and-stories"),
    ("brutalist-art/youtube", "claude-liam-a5-03-data-contract"),
    ("brutalist-art/youtube", "claude-liam-a5-04-good-looks-like"),
    ("brutalist-art/youtube", "claude-liam-a5-05-bad-looks-like"),
    ("brutalist-art/youtube", "claude-liam-a5-06-the-one-thing"),
    ("brutalist-art/youtube", "claude-liam-a5-07-assemble-submit"),
    # A5B — Build the Recipe
    ("brutalist-art/youtube", "claude-liam-a5b-01-brand-config"),
    ("brutalist-art/youtube", "claude-liam-a5b-02-verified-folder"),
    ("brutalist-art/youtube", "claude-liam-a5b-03-framework-primer"),
    ("brutalist-art/youtube", "claude-liam-a5b-04-write-recipe"),
    ("brutalist-art/youtube", "claude-liam-a5b-05-snickerdoodle"),
    ("brutalist-art/youtube", "claude-liam-a5b-06-assemble-submit"),
    # A6 — Name It & Brand It
    ("brutalist-art/youtube", "claude-liam-a6-01-brand-foundation"),
    ("brutalist-art/youtube", "claude-liam-a6-02-positioning-pillars"),
    ("brutalist-art/youtube", "claude-liam-a6-03-name-generation"),
    ("brutalist-art/youtube", "claude-liam-a6-04-trademark-search"),
    ("brutalist-art/youtube", "claude-liam-a6-05-url-and-final-name"),
    ("brutalist-art/youtube", "claude-liam-a6-06-portfolio-analysis"),
    ("brutalist-art/youtube", "claude-liam-a6-07-plus-one-and-submit"),
    # A7 — Sell the Vision
    ("brutalist-art/youtube", "claude-liam-a7-01-the-pitch-arc"),
    ("brutalist-art/youtube", "claude-liam-a7-02-title-and-problem"),
    ("brutalist-art/youtube", "claude-liam-a7-03-solution-and-magic"),
    ("brutalist-art/youtube", "claude-liam-a7-04-business-case"),
    ("brutalist-art/youtube", "claude-liam-a7-05-proof-of-concept"),
    ("brutalist-art/youtube", "claude-liam-a7-06-record-it"),
    ("brutalist-art/youtube", "claude-liam-a7-07-ship-the-pitch"),
    # A7v — Make It Visible
    ("brutalist-art/youtube", "claude-liam-a7v-01-creative-brief"),
    ("brutalist-art/youtube", "claude-liam-a7v-02-logo"),
    ("brutalist-art/youtube", "claude-liam-a7v-03-mood-and-styleguide"),
    ("brutalist-art/youtube", "claude-liam-a7v-04-wireframes-pages"),
    ("brutalist-art/youtube", "claude-liam-a7v-05-mobile-and-platform"),
    ("brutalist-art/youtube", "claude-liam-a7v-06-plus-one-and-submit"),
    # A8 — Ship It
    ("brutalist-art/youtube", "claude-liam-a8-00-the-map"),
    ("brutalist-art/youtube", "claude-liam-a8-01-website-draft"),
    ("brutalist-art/youtube", "claude-liam-a8-02-website-responsive"),
    ("brutalist-art/youtube", "claude-liam-a8-03-accessibility-check"),
    ("brutalist-art/youtube", "claude-liam-a8-04-linkedin-header"),
    ("brutalist-art/youtube", "claude-liam-a8-05-brand-visuals"),
    ("brutalist-art/youtube", "claude-liam-a8-06-ats-resume"),
    ("brutalist-art/youtube", "claude-liam-a8-07-visual-resume"),
    ("brutalist-art/youtube", "claude-liam-a8-08-bonus-touchpoint"),
    # A9 — Make Them Remember
    ("brutalist-art/youtube", "claude-liam-a9-01-why-stories"),
    ("brutalist-art/youtube", "claude-liam-a9-02-three-arcs"),
    ("brutalist-art/youtube", "claude-liam-a9-03-expanded-story"),
    ("brutalist-art/youtube", "claude-liam-a9-04-the-article"),
    ("brutalist-art/youtube", "claude-liam-a9-05-graphic-publish-promote"),
    ("brutalist-art/youtube", "claude-liam-a9-06-assemble-submit"),
    # A10 — Build a Home
    ("brutalist-art/youtube", "claude-liam-a10-01-launch-substack"),
    ("brutalist-art/youtube", "claude-liam-a10-02-brand-audit"),
    ("brutalist-art/youtube", "claude-liam-a10-03-write-thought-leadership"),
    ("brutalist-art/youtube", "claude-liam-a10-04-headline-visual-publish"),
    ("brutalist-art/youtube", "claude-liam-a10-05-promote-reflect-ship"),
    # REM — Design a Mode (25 pts)
    ("the-reallocation-engine/youtube", "claude-liam-rem-01-engine-and-situation"),
    ("the-reallocation-engine/youtube", "claude-liam-rem-02-write-the-mode"),
    ("the-reallocation-engine/youtube", "claude-liam-rem-03-domain-justification"),
    ("the-reallocation-engine/youtube", "claude-liam-rem-04-worked-example-and-present"),
    # MB — Make It Run (100 pts)
    ("the-reallocation-engine/youtube", "claude-liam-mb-01-get-it-running"),
    ("the-reallocation-engine/youtube", "claude-liam-mb-02-design-the-mode"),
    ("the-reallocation-engine/youtube", "claude-liam-mb-03-domain-justification"),
    ("the-reallocation-engine/youtube", "claude-liam-mb-04-worked-run"),
    ("the-reallocation-engine/youtube", "claude-liam-mb-05-ship-and-present"),
    # MB25 — Make It Run Lite (25 pts)
    ("brutalist-art/youtube", "claude-liam-mb25-01-run-and-design"),
    ("brutalist-art/youtube", "claude-liam-mb25-02-domain-justification"),
    ("brutalist-art/youtube", "claude-liam-mb25-03-worked-run"),
    ("brutalist-art/youtube", "claude-liam-mb25-04-ship-and-record"),
    # RE — Build It, Then Doubt It (100 pts)
    ("brutalist-art/youtube", "claude-liam-re-01-the-premise"),
    ("brutalist-art/youtube", "claude-liam-re-02-build-the-tool"),
    ("brutalist-art/youtube", "claude-liam-re-03-gigo-gate"),
    ("brutalist-art/youtube", "claude-liam-re-04-bias-audit"),
    ("brutalist-art/youtube", "claude-liam-re-05-explainability-critique"),
    ("brutalist-art/youtube", "claude-liam-re-06-pearls-ladder"),
    ("brutalist-art/youtube", "claude-liam-re-07-adversarial"),
    ("brutalist-art/youtube", "claude-liam-re-08-delegation-hard-stop"),
    ("brutalist-art/youtube", "claude-liam-re-09-communicate-and-ship"),
    # Capstone — Make It Count (200 pts)
    ("brutalist-art/youtube", "claude-liam-cap-01-the-map"),
    ("brutalist-art/youtube", "claude-liam-cap-02-make-it-live"),
    ("brutalist-art/youtube", "claude-liam-cap-03-assemble-and-audit"),
    ("brutalist-art/youtube", "claude-liam-cap-04-build-the-deck"),
    ("brutalist-art/youtube", "claude-liam-cap-05-rehearse-and-demo"),
    ("brutalist-art/youtube", "claude-liam-cap-06-submit"),
]


def is_built(books_dir, book, slug):
    mp4_dir = os.path.join(books_dir, book, slug, "mp4")
    if os.path.isdir(mp4_dir):
        return any(f.endswith(".mp4") for f in os.listdir(mp4_dir))
    return False


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="Print what would run, don't build")
    parser.add_argument("--from", dest="from_slug", metavar="SLUG", default=None, help="Resume from this slug (inclusive)")
    parser.add_argument("--only", metavar="PREFIX", default=None, help="Build only slugs matching claude-liam-PREFIX, e.g. a9 or re")
    parser.add_argument("--force", action="store_true", help="Rebuild even if mp4 already exists")
    args = parser.parse_args()

    # Resolve paths
    script_dir = os.path.dirname(os.path.abspath(__file__))  # brutalist-art/
    books_dir = os.path.dirname(script_dir)                   # books/
    art = os.path.join(script_dir, "art")

    if not os.path.isfile(art):
        print(f"ERROR: art script not found at {art}")
        sys.exit(1)

    started = args.from_slug is None
    built = skipped = failed = 0
    failures = []

    for book, slug in REELS:
        # --from resume gate
        if not started:
            if slug == args.from_slug:
                started = True
            else:
                continue

        # --only filter
        if args.only and not slug.startswith(f"claude-liam-{args.only}"):
            continue

        # skip check
        if not args.force and is_built(books_dir, book, slug):
            print(f"  SKIP   {slug}")
            skipped += 1
            continue

        reel_path = f"{book}/{slug}"
        print(f"  BUILD  {slug}")
        if args.dry_run:
            built += 1
            continue

        result = subprocess.run([art, "run", reel_path], cwd=books_dir)
        if result.returncode != 0:
            print(f"\n  FAIL   {slug} — exit {result.returncode}")
            failed += 1
            failures.append((slug, result.returncode))
            continue
        built += 1

    tag = " (dry run)" if args.dry_run else ""
    print(f"\nDone{tag}. Built: {built}  Skipped: {skipped}  Failed: {failed}")
    if failures:
        print("\nFailed reels:")
        for slug, returncode in failures:
            print(f"  {slug} — exit {returncode}")
        sys.exit(1)


if __name__ == "__main__":
    main()
