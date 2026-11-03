# Worker brief: one AoPS batch -> question-bank batch (Claude only)

You process ONE batch of 100 scraped AoPS middle-school forum topics into question-bank records, end to end. Several workers (one per batch of the run in `run.json`) run in parallel. The orchestrator later re-checks all batches together, reviews every figure at full size, rebuilds the registry chain in order and merges everything into one package. This is the same workflow that produced batches 191-220.

Paths below are relative to the repo root (call it `REPO`; the orchestrator gives you its absolute path). Your batch number is NNN and your file prefix is `pNNN_` (e.g. batch 221 -> `p221_01.py`, `chk_p221_01.py`).

Do not use DeepSeek or any other external model or API. Only write inside your own folder `REPO/work/bNNN`, plus appending to `REPO/work/xnotes.md`. Other batches' folders and everything else in the repo are read-only for you. Do not run git commands (the orchestrator commits).

## Inputs

- Source: `REPO/source/batch_0NNN.json` (keys `topics`, each with `topic_id`, `title`, `text`, `url`, ...). Read ALL 100 topics in full.
- Spec (authority on format: controlled tag vocabulary, difficulty rubric, LaTeX and diagram rules): `REPO/ref/spec.md`. Read it before writing records.
- Your folder `REPO/work/bNNN` already has the tools: `qbpaths.py, qb.py, compile.py, sheet.py, figsheets.py, dup.py, findprior.py, showprior.py, assemble.py, finalize.py, precheck.py, pdfcheck.py`, an empty `rec/`, `aliases.json` = `{}` and `chk.py` (runs every `chk_pNNN_KK.py`). Run every tool from inside your folder.
- Worked examples from batch 220 (read them first, match their style and quality): `REPO/examples/en01.py` (builder), `chk_en01.py` (answer checks), `screen.py`, `alts.py`, `aliases.json`, `report_batch_0220.md` (a finished report). Your files use the prefix `pNNN_` instead of `en`.
- `REPO/ref/prior.json`: every earlier exported record, for duplicate screens (use dup.py / findprior.py / showprior.py, don't load it by hand). `REPO/ref/base_registry.json`: cumulative registry through the batch before this run.

## Content rules (the user's, important)

- IDs: `aops-topic-<topic_id>-q<part:02>`; the part number follows the problem's position or label in the post (a post with problems numbered 2, 4, 8 keeps q02, q04, q08). Never reuse an ID from the registry.
- Maths questions only. Exclude non-maths posts (advice, polls, flexing, adverts, resource requests, jokes, contest logistics). Where possible turn a conceptual or non-maths post into a proper maths question ("find the error in this argument", "prove X", "give a counterexample").
- Fix bad content instead of copying it: correct wrong reasoning and wrong posted answers, handle multiple answers, repair inconsistent or impossible conditions and typos, so every item is a well-posed question with a single verified answer (or a proof). Record every change in the record's `note` and in the report.
- Solve first, then tag. Write the full solution before choosing tags and difficulty. Tags only from the controlled vocabulary (qb.py rejects others and suggests close matches). Difficulty integer 1-7 (rubric in qb.py; pass `rat=` for an explicit rationale if needed).
- Exclude topics whose essential data is only in a missing image/attachment, or with no problem text, or hopelessly ill-posed, or whose only solution is a computer search / research paper. Rebuild a missing figure from the text only when the text determines it (check against an official answer when the problem is a known contest problem).
- LaTeX: `\dfrac` for every fraction (no `\frac`, `\tfrac`, `\cfrac`, `\over`); no slash fractions in maths and no slashed fractional exponents (`^{\dfrac23}`, not `^{2/3}`); ASCII only; balanced braces and `$`; no `%` (write `\%`); `\[ \]` for displays.
- Source metadata: `source=src(comp, year, division, qn, paper=None, rnd=None)` when the post names a contest (e.g. `src('AMC 10',2018,'B',6)`, `src('MATHCOUNTS',2019,'State',25,rnd='Sprint')`); omit otherwise.

## Diagrams (the user wants them perfect)

- Asymptote only, via `asy(body, size)` from qb.py. It appends a black empty label so a coloured last label cannot leak its colour into the following text; never remove that and never bypass `asy()`.
- Every record with a geometry-type tag (any tag under "### Geometry" in the spec: Triangles, Circles, Coordinate geometry, Lengths, perimeter, and area, ...) must have an Asymptote sketch in its solution (assemble.py flags missing ones). If a sketch would not make sense, drop the geometry tag instead.
- Draw from computed coordinates so proportions are true (or say "not to scale" and label lengths when true proportions would be unreadable). A question figure shows only what the question gives, never solution content.
- Labels must not touch or overlap other labels, lines, ticks or arcs; place them outside the figure or clearly inside a region, readable size. Tick, angle and right-angle marks only on the right segments/angles. Given objects solid, auxiliary constructions dashed or coloured. Consistent style.
- Quirks in this environment: `rightanglemark`, `circumcenter`, `incenter`, `foot` are unavailable (compute: incentre `(a*A+b*B+c*C)/(a+b+c)`, foot by projection with `dot`; draw right-angle marks as a small square path); `import graph;` is needed for `graph(...)`; no 3D (`unitcylinder` fails; use 2D oblique projections and ellipses); no `UnFill` (renders as black boxes); do not name variables `S`, `E`, `N`, `W`. In Python raw strings use a single backslash in labels (`"$\sqrt{2}$"`).
- Faults the orchestrator had to fix last run (check for them): a length label placed beside one half of a segment whose midpoint is labelled (reads as the half's length); an angle label far from its arc (put it just beyond the arc, inside the angle); a label sitting on a dashed or auxiliary line; an arc or construction running outside the figure for no reason; a redundant side label next to a sub-length label.
- Every diagram needs alt text in `alts.py` (`A` for solution figures, `Q` for question figures; key `<topic>-qNN`; a list if a body has several figures, in order). The alt text must describe the figure as drawn.
- Look at every figure: `python3 figsheets.py` renders all figures of non-aliased records at 640 px, four per sheet, into `figs/sheet_NN.png` with `figs/index.txt` (record and question per panel); `python3 figsheets.py ID ...` renders only those records into `figs/only_NN.png`. Read every sheet with the Read tool and fix anything not perfect, then look again.

## Verification

- Verify every computable answer by brute force, exact arithmetic or coordinates in `chk_pNNN_KK.py` (one per builder, same style as the example: plain asserts, comment line `# <topic_id> ...` before each block). `python3 chk.py` must print `chk OK`. Proofs: check the claim numerically where possible.
- Known contest problems: make sure the answer matches the official answer.

## Duplicates

- `python3 dup.py` (Jaccard > 0.45) screens your `rec/` against all prior releases and against the other workers' current drafts. Also run keyword searches for well-known problems with `python3 findprior.py 'regex' ['regex' ...]` and inspect with `python3 showprior.py aops-topic-...`. Run dup.py again at the end (other workers' drafts grow).
- A true repeat (same task, same data, possibly reworded, or entirely contained in the old one) is not exported: put it in `aliases.json` as `{"aops-topic-<new>-qNN": "aops-topic-<canonical>-qNN"}` and keep its record in your builder (assemble filters aliases out). The canonical must be an exported record (if it is itself an alias in the registry, follow the chain).
- Repeats inside this run: alias only to an EARLIER batch of the run (lower batch number, e.g. 225 -> 223). If the other copy is in a LATER batch, keep yours exported and append one line to `REPO/work/xnotes.md` (e.g. `- b223 1951192-q01 repeats b227 draft 1938065-q01: b227 should alias to b223`). Also check xnotes.md at the end for lines addressed to your batch and act on them. Two copies of the same problem inside your own batch: alias the later topic to the earlier one.
- Near misses (same idea, different numbers or target) are kept; mention notable ones in the report.

## Files you produce (prefix `pNNN_`)

- Builders `pNNN_01.py`, `pNNN_02.py`, ... (about 25-40 records each, source order), each `from qb import *`, `b=Bank('pNNN_01')`, `b.add(topic_id, part, question, solution, 'Tag|Tag', difficulty, source=src(...), note='...')`, `b.save()`. Run each builder to write `rec/pNNN_KK.json`.
- `chk_pNNN_KK.py`, `screen.py` (`NONMATH`, `EXCL` topic->reason for every excluded topic, `PARTIAL` topic->what was dropped; topics fully aliased are recorded as duplicates automatically, not in EXCL), `alts.py`, `aliases.json`.
- `processing_report.md` in the style of the example (sections: IDs and duplicates incl. multi-part mappings and every alias with a reason; Screening with statuses and lists of partial and excluded topics with reasons; Editorial changes - every wrong posted answer corrected, every ill-posed/impossible condition fixed, every reading chosen for ambiguous wording; Diagrams; Validation). Mention that batches 76-80 are still missing from the registry.

## Steps

1. Read the spec, the examples and all 100 topics. Decide include / partial / exclude for each.
2. Solve and verify each problem; write builders in source order and run them; write chk files; `python3 chk.py`.
3. Write `screen.py` and `alts.py`; run `python3 figsheets.py`, Read every sheet, fix and re-check figures.
4. Duplicate screen (dup.py + keyword searches); write `aliases.json`.
5. `python3 precheck.py NNN` must end PRECHECK OK. Then `rm -rf out && python3 finalize.py NNN` (pre-check mode: it validates tags, fractions, braces, ASCII, slashes, geometry sketches, builds the ZIP and verifies hashes; read the "review:" lines it prints - slash hits inside maths must be fixed, text slashes like "and/or" are fine). Then `python3 pdfcheck.py` must end `OK` (0 LaTeX errors, 0 Asymptote failures, 0 figures whose last label colour is not black).
6. Write `processing_report.md`.
7. Final dup.py re-run and xnotes.md check; if anything changed, re-run step 5.

## What to send back (your final message, under 300 words)

Records exported, aliases, diagrams, screening statuses (included / partial / excluded / duplicate); the notable corrections (wrong posted answers, ill-posed problems fixed or excluded); cross-batch repeat notes; anything you are unsure about. Confirm chk OK, PRECHECK OK, finalize and pdfcheck OK.
