# Illustrae icon conversion and provenance

Illustrae exports are a version-chained, cross-project image history. They must
not be treated as 570 independent figures.

The reproducible indexing script now lives in the repository:

```bash
python3 illustrae-pipeline/build_icon_source_index.py
```

It produces:

- `illustrae-pipeline/icon-pipeline/source-index.jsonl`: all source records
- `illustrae-pipeline/icon-pipeline/conversion-candidates.jsonl`: unique records
  classified as likely original figures
- `illustrae-pipeline/icon-pipeline/summary.json`: audit totals

Each record retains the immutable Illustrae sidecar, SHA-256 identity, measured
dimensions and byte count, relative paths, kind classification, lineage fields,
destination fields, and derivative fields.

## Conversion gate

Only a reviewed `kind: "figure"` and its selected
`kind: "text_free_derivative"` may enter icon conversion. Before conversion:

1. Cluster visually and by prompt similarity.
2. Identify edit ancestry and select the final source for each real figure.
3. Populate `parent_id`, `root_id`, `is_final`, and `dedup_cluster`.
4. Reconcile the figure with its book, chapter, slug, and destinations.
5. Mark the selected source `review_status: "approved-for-conversion"`.

The converter then creates a text-free, medium-rough, transparent SVG and PNG
preview. The derivative joins to its source using both Illustrae element ID and
SHA-256; filenames are display values only.
