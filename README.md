# AoPS question bank: batches

Everything a Claude Code cloud session needs to turn AoPS source batches into question-bank packages: the spec, the source batches still to do, all earlier records (for duplicate checks), the registry, the tools and worked examples. The instructions Claude follows are in `CLAUDE.md`.

## How to run a batch set

1. Open Claude Code on the web (claude.ai/code), pick this repo, and start a session.
2. Type: **do batches 221-230** (or whichever ten come next; `ref/progress.json` says where the last run stopped).
3. When it finishes, it pushes the package and opens a pull request. **Merge the pull request** on GitHub. The next run needs that merge, because it updates the registry and the duplicate list.
4. The finished package is in `output/processed_batches_0221_0230/`. To get it onto your computer, either download it from GitHub (Code -> Download ZIP), or ask a Claude chat that's linked to your computer to "copy the latest output from my GitHub batches repo into my batches folder".

If a session stops part-way, start a new one and type **continue batches 221-230**.

Source batches in `source/` currently run up to batch 328.
