# Processing report: batches 221-230

Ten batches (1000 AoPS middle-school topics) processed by one worker per batch, then reviewed, cross-checked, rebuilt in order and merged by the orchestrator. Claude only; no external models or APIs.

## Totals

- **804 question records** exported, **101 aliases** (repeats not exported), **205 Asymptote diagrams** (all with SVG previews and alt text).
- Screening of 1000 topics: **625 included, 11 partial, 296 excluded, 68 duplicate**.
- Merged ZIP: 2618 members, `checks_passed: true`, sha256 `ac554516365d3f7ec63237d95be4244cd08c917e261349b13f284cd42c4da1ca`.

| Batch | Records | Aliases | Diagrams | Included | Partial | Excluded | Duplicate |
|---|---|---|---|---|---|---|---|
| 221 | 63 | 18 | 16 | 54 | 2 | 29 | 15 |
| 222 | 70 | 7 | 18 | 62 | 1 | 34 | 3 |
| 223 | 73 | 10 | 13 | 54 | 1 | 36 | 9 |
| 224 | 81 | 10 | 23 | 68 | 2 | 21 | 9 |
| 225 | 93 | 10 | 22 | 68 | 0 | 25 | 7 |
| 226 | 80 | 8 | 20 | 58 | 1 | 34 | 7 |
| 227 | 80 | 5 | 15 | 61 | 1 | 36 | 2 |
| 228 | 86 | 14 | 18 | 69 | 0 | 23 | 8 |
| 229 | 81 | 12 | 24 | 67 | 1 | 28 | 4 |
| 230 | 97 | 7 | 36 | 64 | 2 | 30 | 4 |

## Cross-batch repeats (aliased in the later batch to the earlier batch's record)

- b223 1777424-q01 -> b222 1777432-q01 (cube colourings, 230)
- b224 1768268-q01 -> b223 1605801-q01 (2018 MATHCOUNTS School Sprint #22)
- b225 1765713-q01 -> b222 1777350-q01 (Yu's 12 coins)
- b227 1757353-q01 -> b226 1759713-q03 (five-term AP, 28); b227 1757353-q02 -> b225 1762366-q149 (Vida's guppies, 48)
- b229 1745621-q01/q02 -> b227 1755042-q118/q119 (mini-golf; Cayley's die)
- b230 1736178-q01 -> b229 1743778-q01; b230 1735148-q01 -> b227 1757367-q01

The cross-batch scan (266 pairs with Jaccard > 0.35) found no other repeats; the closest pairs are near misses with different data (e.g. x+1/x=5, find x^4+1/x^4 vs x+1/x=4, find x^5+1/x^5) and are kept.

## Notable corrections (details in each batch report)

- **Wrong posted answers corrected:** 1785367 (2100, not 2720), 1781575 (98), 1780414 (p+1), 1747860 (305/1001), 1754336 (1.5), 1753532 (3 triangles, not 4), 1775342 (90 min; the key says 120), 1770709 (3/95), 1767069 (28√29/3), 1771791 (3√3+π, not 3√7), 1750568-q03 (3187.5 miles), 1747922 (C(11,4)·7!), 1748211 (98 lattice points), 1739370 (necklaces: 3, not 24), 1762366 #148/#149, 1766133 (exact sum 8748 − 4/3^17).
- **Impossible or ill-posed data repaired:** 1787416 (right-angled → acute-angled, 84), 1782697 (radii changed to 66, 55, 60), 1762096 (3-13-16 is degenerate; uses √41-13-16), 1766250 (53 bars impossible; 117 used), 1769594 (factor 2 restored), 1782319 (proves no solution), 1765813 (proves never divisible by 49), 1747574 (false cases corrected), 1747797 and 1765152 (extremum did not exist; positivity or maximum added), 1760131 (identity corrected), 1786041 (no constants exist, proved).
- **Multiple answers given where the post assumed one:** 1752547, 1758037, 1776515, 1776388, 1782694, 1741603, 1734465, 1770315.
- **Excluded as ill-posed or not solvable by hand:** among others 1782881, 1772906, 1772749, 1777131, 1779795, 1751576, 1748405, 1744964, 1743564, 1739994, 1762188.

## Diagram fixes made in the orchestrator review

All 205 figures were viewed at full size. Fixes (all re-rendered and re-checked):

- **Geometry:** 1736373 (b230) cone sides redrawn tangent to the base ellipse, because the back rim showed outside the silhouette. 1753987 (b227) cone ellipses flattened so the cut circle no longer touches the base.
- **Misleading length labels:** 1782694-q01 (b222, both figures): the base length "6" sat beside one short segment; it is now a dimension arrow under BC. 1748217-q01 (b228): half-chord labels moved to the halves used in the right triangles. 1734443-q01 (b230): 4√10 moved onto median BK.
- **Labels touching lines, arcs or axes, moved clear:**
  - b221: 1787556, 1787424, 1785634-q05, 1785275
  - b222: 1780203-q04
  - b223: 1772259-q03
  - b225: 1763561
  - b226: 1762490, 1761304, 1762011, 1759331, 1759220
  - b227: 1756275, 1756743
  - b228: 1748211, 1749331, 1746837
  - b229: 1743708, 1745435, 1743083-q03, 1743013, 1741984
  - b230: 1735512-q82, 1734443-q06, 1734443-q09, 1734740

## Validation

- Every batch passed `chk.py` (chk OK), `precheck.py` (PRECHECK OK) and finalize in registry-chained order 221 → 230.
- `pdfcheck.py` in every batch: OK (0 LaTeX errors, 0 Asymptote failures, 0 figures whose last label colour is not black).
- `merge.py` validated the merged ZIP independently: 804 records, 205 previews, 0 missing previews, `checks_passed: true`.

## Note

Batches 76-80 are still missing from the deduplication registry.
