# Processing report: batches 231-235

Five batches (500 AoPS middle-school topics). One worker per batch processed the topics; the orchestrator then reviewed and cross-checked them, rebuilt them in order and merged them. Only Claude was used: no external models or APIs.

## Totals

- **378 question records** exported, **60 aliases** (repeats not exported), **94 Asymptote diagrams** (all with SVG previews and alt text).
- Screening of 500 topics: **311 included, 9 partial, 136 excluded, 44 duplicate**.
- Merged ZIP: 1229 members, `checks_passed: true`, sha256 `c48e93d7bb8c183ea8b125567c42808ebf249edf7ea4a39b90ea764121a675ef`.

| Batch | Records | Aliases | Diagrams | Included | Partial | Excluded | Duplicate |
|---|---|---|---|---|---|---|---|
| 231 | 79 | 17 | 15 | 58 | 0 | 29 | 13 |
| 232 | 73 | 17 | 20 | 60 | 4 | 23 | 13 |
| 233 | 73 | 9 | 21 | 62 | 3 | 29 | 6 |
| 234 | 78 | 6 | 19 | 68 | 0 | 26 | 6 |
| 235 | 75 | 11 | 19 | 63 | 2 | 29 | 6 |

## Repeats

- **Within this run:** b233 1717359-q01/q02/q04 (KEP round 8) are aliased to b232 1724486-q03, 1723304-q01 and 1724486-q01.
- **Earlier records:**
  - b232 1725534-q01 is aliased to prior 1877656-q01 (the glide-reflection problem; b234 1713999 points to the same record).
  - Several aliases point to records from run 221-230, e.g. b231 1731843 -> 1749176-q92 and b235 1707222-q04 -> 1757353-q03.
- **Cross-batch scan:** 61 pairs with Jaccard > 0.35, and no further repeats. The closest pairs are the same kind of problem with different data.
- **Near misses kept:**
  - b234 1715264-q03 ((a+b+c+d)^6) vs prior 1759128-q04 ((3a+4b+6c+12d)^6).
  - b232 1726527 (original "reveal" wording) vs prior 2953609-q04.

## Notable corrections (details in each batch report)

- **Wrong posted answers corrected:**
  - b231: 1734624-q02 (119 diagonals), 1147571 (560).
  - b232: 1724568 (4.92 mph).
  - b233: 1719574 (2017 AMC 10A #17: 7, not 5√2), 1720835 (C = (−6,0), perimeter 16).
  - b235: 1704033 (216), 1706974 (b ≡ 5 mod 20), 1710592 (corrected split, minimum 6).
- **Impossible or false statements turned into proofs:**
  - b231: 1657695 #11 (the prism cannot exist).
  - b232: 1724972 (the triangle cannot exist), 1724982 (the formula holds with the inradius, not the circumradius), 1722309 (the 1/5 ratio holds only for parallelograms), 1723548 (5.5.12 does not fit at a vertex; corrected to 5.5.10).
  - b234: 1713423 (counterexample to "a^5 natural ⇒ a natural").
  - b235: 1705943 (not a power of 2).
- **Contradictory data repaired:** 1715535, 1724486-q03 / 1717359-q01, 1657695 #5 and #6, 1710811.
- **None of the multiple-choice options is correct:** 1712630 (area ≈ 16.92); the record is free-response.
- **Multiple answers given:** 1732087-q01, 1710140, 1709513-q10, 11090.

## Diagram fixes made in the orchestrator review

All 94 figures were viewed at full size.

- **Misleading length labels:**
  - 1728894-q01 (PQ = 10), 1726281-q04 (AB = 8): each label sat under one part of the segment; both are now dimension arrows.
  - 1720835: the base label was moved to the centre of CA.
- **Labels touching lines, curves or axes, moved:** 1715264-q01, 1698023, 1711919, 1717359-q05.
- Batch 235 needed no changes.

## Validation

- Every batch passed chk, PRECHECK and finalize, in registry-chained order 231 -> 235. The chain starts from the registry through batch 230 (run 221-230).
- `pdfcheck.py` in every batch: OK (0 LaTeX errors, 0 Asymptote failures, 0 colour leaks).
- `merge.py` validated the merged ZIP independently: 378 records, 94 previews, 0 missing, `checks_passed: true`.

## Note

Batches 76-80 are still missing from the deduplication registry.
