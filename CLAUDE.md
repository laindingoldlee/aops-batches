# AoPS -> question bank: cloud run instructions

This repo holds everything needed to turn batches of scraped AoPS middle-school forum topics into question-bank packages. You (Claude, in a cloud session) are the **orchestrator** of a run. The user will usually start you with one line such as:

> do batches 221-230

That means: process those batches end to end, following this file, and push the finished package. Do not ask clarifying questions for a routine run; make sensible editorial decisions and document them. Work autonomously until the package is pushed.

Never use DeepSeek or any other external model or API. Claude only.

## Repo layout

| Path | What it is |
|---|---|
| `setup.sh` | Installs Asymptote, pdflatex + asymptote.sty, cairosvg/pillow/sympy/numpy. Run first. |
| `ref/spec.md` | The import specification: schema, controlled tag vocabulary, difficulty rubric, LaTeX, diagram and ZIP rules. **Authority on format.** |
| `ref/prior.json` | Every earlier exported record (id, src, tags, question, solution, note) for duplicate screens. |
| `ref/base_registry.json` | Cumulative deduplication registry through `ref/progress.json` -> `registry_through`. |
| `ref/progress.json` | Which batch the registry covers up to. The next run must start at `registry_through + 1`. |
| `source/batch_NNNN.json` | Source batches (keys `topics`, each with `topic_id`, `title`, `text`, `url`, ...). 100 topics each. |
| `tools/` | The pipeline. `qbpaths.py` holds all paths; `setup_run.py`, `runall.sh`, `xdup.py`, `merge.py`, `advance.py` are run-level; the rest are per-batch tools copied into each work folder. |
| `examples/` | Worked examples from batch 220: builders `en01.py`-`en03.py`, checks `chk_en01.py`-`chk_en03.py`, `screen.py`, `alts.py`, `aliases.json`, `report_batch_0220.md`, and the orchestrator notes from run 212-220. In your run the files are named `p<batch>_KK.py` / `chk_p<batch>_KK.py` instead of `enKK.py`. |
| `WORKER_BRIEF.md` | The brief each per-batch worker follows. Read it fully; it has the content rules. |
| `work/bNNN/` | Working folder per batch (created by `setup_run.py`). |
| `output/processed_batches_FFFF_LLLL/` | The merged package of a finished run. This is the deliverable. |

## Steps for a run FIRST-LAST

1. `bash setup.sh` (must print `SETUP OK`).
2. `python3 tools/setup_run.py FIRST LAST`. It refuses if FIRST is not `registry_through + 1`; if the user asked for a range that does not follow on, tell them and use the correct start only if the user is not reachable (say so in the report).
3. Read `WORKER_BRIEF.md`, `ref/spec.md` and the examples yourself, so you can review the workers' output.
4. **Workers.** Spawn one subagent per batch, all in parallel, with the Agent tool (general-purpose). Each prompt: "Read /ABS/PATH/TO/REPO/WORKER_BRIEF.md and follow it for batch NNN. Your folder is /ABS/PATH/TO/REPO/work/bNNN; your file prefix is pNNN_." (use the real absolute repo path). If the session limits how many agents run at once, run them in waves. Keep `work/notes.md` with one line per batch as results come in (records, aliases, diagrams, statuses, anything to check), like `examples/merge_212_220/orch_notes.md`.
5. **Commit as you go.** After each worker finishes, `git add -A && git commit -m "batch NNN draft" && git push` so nothing is lost if the session ends. (The `.gitignore` keeps renders and build output out.)
6. **Review every batch** when its worker reports:
   - `cd work/bNNN && python3 figsheets.py`, then Read every `figs/sheet_NN.png` at full size. The user wants the diagrams perfect: labels not touching lines or other labels, correct configuration and proportions, marks on the right segments, nothing from the solution in a question figure, alt text matching the figure. Fix anything that is not perfect yourself (edit the builder, re-run it, re-render with `python3 figsheets.py ID`), and note each fix in `work/notes.md`.
   - Spot-check corrections the worker flagged as unsure; skim `processing_report.md`.
7. **Cross-batch duplicates.** `python3 tools/xdup.py` lists pairs across batches of this run with Jaccard > 0.35. A true repeat must be an alias in the LATER batch pointing at the earlier batch's record. Also act on every line in `work/xnotes.md`.
8. **Final build, in order.** `bash tools/runall.sh` rebuilds, checks and finalizes every batch in order so each batch's registry chains from the previous one. Every batch must pass chk, PRECHECK OK and finalize. Then in each `work/bNNN`: `python3 pdfcheck.py` must end `OK` (0 LaTeX errors, 0 Asymptote failures, 0 figures whose last label colour is not black).
9. **Merge.** `python3 tools/merge.py` writes `output/processed_batches_FFFF_LLLL/` (one ZIP + all JSON files + `review_logs/batch_NNNN/` with builders and per-batch reports) and validates the merged ZIP independently.
10. **Merged report.** Write `output/processed_batches_FFFF_LLLL/processing_report.md`: totals (records, aliases, diagrams, screening statuses) and a per-batch table; cross-batch repeats; the notable corrections (wrong posted answers, ill-posed problems fixed or excluded); the diagram fixes you made in review; validation results; and the note that batches 76-80 are still missing from the registry. Keep it short; the per-batch reports carry the detail.
11. **Advance the reference data.** `python3 tools/advance.py` folds this run into `ref/` (registry, prior records, progress) so the next run continues from it.
12. **Deliver.** `git add -A && git commit -m "batches FFFF-LLLL" && git push`. If you are working on a branch, open a pull request into `main` titled `Batches FFFF-LLLL` whose description is the short summary below. The user must merge it before the next run, because the next run needs the advanced `ref/`.
13. **Final message** (short): record, alias and diagram counts; screening statuses; the notable corrections; any diagram fixes; anything you were unsure about; and remind the user to merge the PR.

## Format rules that the tools enforce (details in WORKER_BRIEF.md and ref/spec.md)

- IDs `aops-topic-<topic_id>-q<part:02>`, never reused.
- `\dfrac` only; no slash fractions in maths; ASCII only; balanced braces and `$`; `\%`.
- Asymptote only, always through `asy()` in `qb.py` (it appends the black label that stops the inline-Asymptote colour leak; never bypass it). Every geometry-tagged record has a sketch.
- Tags only from the controlled vocabulary; difficulty 1-7 with a rationale.

## Known Asymptote quirks

`rightanglemark`, `circumcenter`, `incenter`, `foot` are unavailable (compute them); `import graph;` for `graph(...)`; no 3D (`unitcylinder` fails; use 2D oblique projections); no `UnFill`; don't name variables `S`, `E`, `N`, `W`.

## If the session stops part-way

Everything committed is safe. A new session told "continue batches FFFF-LLLL" should: run `bash setup.sh`, run `python3 tools/setup_run.py FFFF LLLL` (it keeps existing work folders and only refreshes tools), read `work/notes.md`, check which `work/bNNN` folders have a `processing_report.md`, and restart workers only for the unfinished batches (a worker may continue from the files already in its folder).
