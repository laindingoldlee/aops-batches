# AoPS batch 227 processing report

**82 question records** prepared from the 100 topics screened in batch 227.

Claude did all of the work, with no DeepSeek or other external model. Every topic was read in full; each problem was solved before tags and difficulty were chosen; every computable answer was checked with exact or brute-force code (`chk_p227_01.py` to `chk_p227_03.py`); every diagram was checked by eye on contact sheets. Builders: `p227_01.py` to `p227_03.py`.

## IDs and duplicates

- IDs have the form `aops-topic-<AoPS topic id>-q<part:02>`. Multi-problem posts:
  - 1758747 (vertex x-coordinate; vertex form with y-intercept): q01, q02.
  - 1758503 (hypotenuse problem; difference of squares): q01 (alias), q02.
  - 1758419 (x-intercepts; factor of 6x^2+5x-6): q01, q02.
  - 1757353 (three numbered problems): q01-q03.
  - 1757647 (two quadratic inequalities): q01, q02.
  - 1757367 (two numbered problems): q01, q02.
  - 1754235 (five numbered problems): q01-q05.
  - 1755042 (MATHCOUNTS handbook problems #114, #115, #118, #119): q114, q115, q118, q119, keeping the handbook numbers.
  - 1753565 (three divisibility proofs): q01-q03.
  - 1753684 (incircle angle; seating): q01, q02.
  - 1750843 (four numbered problems): q01-q04.
  - 1753103 (Q1, Q2): q01, q02.
  - 1758431: only part 1 is used, so q01.
  - 1754904 (MATHCOUNTS 2005 School Sprint #23): q23. 1754336 (2010 National Target #5): q05. 1753098 (Workout 8 #244): q244.
- 3 repeats are aliased instead of exported:
  - `aops-topic-1757851-q01` -> `aops-topic-2500776-q01` (six of seven phone digits noted, 64 numbers; same task).
  - `aops-topic-1758503-q01` -> `aops-topic-1758855-q01` (same MATHCOUNTS 2014 hypotenuse problem posted twice in this batch; the later topic in source order is aliased).
  - `aops-topic-1756531-q01` -> `aops-topic-2425960-q01` (product of the divisors of n is n^(d(n)/2); the post's question is entirely contained in the earlier record).
- Repeats in later batches of this run (noted in `work/xnotes.md`; the later batch should alias to b227): 1755042-q118 and q119 = b229 draft 1745621-q01, q02; 1757367-q01 = b230 draft 1735148-q01. No lines in `xnotes.md` were addressed to b227.
- Near misses kept: 1754045 (24 | a(a^2+23)) vs prior 2749876 and b228 draft 1746203-q04 (24 | a^2-1); 1754998 (general n: P(sum of n uniforms < 1) = 1/n!, proof) vs b221 draft 1786654 (n = 3 only); 1752848 (CRT with remainders -1) vs other CRT records with different data.

## Screening

Statuses: included 61, partial 1, excluded 36, duplicate 2 (topics fully aliased: 1757851, 1756531).

Partial:
- 1758431: part 2 (68% rule for the normal distribution, a recalled fact) dropped.

Excluded (36):
- 24 non-mathematical posts (AMC 8 opinions and results, MATHCOUNTS Trainer questions, holiday greetings, study advice, book and website requests, predictions, email of AoPS, etc.), plus 1754973 (pinball-machine slope, a design/physics question).
- 1757919: no problem text. 1758755, 1758772, 1757158, 1754638, 1514388: the problem or its essential data is only in a missing picture. 1758121: point values of the target only in the attachment.
- 1758011 (tournament wins): ill-posed; the format (repeated pairings, m <= 2n-1, scheduling) is not specified, and whether the counting bound is attained depends on it.
- 1757551: x+y+z+1/x+1/y+1/z = 8 does not determine x+y+z.
- 1741571 ("one challenge" game thread) and 1717387 (marathon post without problems).

## Editorial changes

- **Wrong posted answers or reasoning corrected:** 1758425 (dividing by i^2 is not allowed; the product is -24-36i); 1747860 (poster's 6/11 is only the two-player race; answer 305/1001); 1755042-q119 (poster's 11/108 misses the double-counted zero face and (0,0,0); answer 19/108); 1754336 (base of the right triangles is sqrt5, not 2sqrt5; answer 1.5); 1753103-q01 (23/90 forgets units digit 0; answer 16/45); 1753532 (non-congruent triangles: 3, not 4); 1754998 (1/(n(n-1)) is wrong for n >= 4; 1/n! proved); 1754302 (0 is a square but not a factor; answer 4).
- **Typos and ill-posed conditions repaired:** 1758744 (g(x) = x^3 = 2x^2 ... read as x^3 - 2x^2 - 16x + 32); 1758431 (y = x^2 cannot be a "vertical compression"; y = (1/8)x^2 used); 1754485 (comboity defined explicitly from the two examples; all 26^4 strings); 1753584 (missing figure; shaded region read as the circular segment); 1753196 (garbled wording read as "digit product even and nonzero").
- **Multiple answers given:** 1758037 (x^2-y^2 = +-80); 1752547 (BD/DA = 2 or 1/2, both configurations drawn); 1757353-q02 (n = 13, 35).
- **Readings chosen:** 1753724 (tower read top-down); 1753558 (overflowing water lost); 1753103-q02 (each chip independently into a random cookie, 51/64; the alternative 19/35 is mentioned in the note); 1753684-q02 (a row of five chairs); 1755042-q118 (integer scores); 1758669 (asks for Descartes' possibilities; the actual 3 positive and 2 negative roots are a remark); 1750843-q03 (straight-line asymptotes; the parabolic asymptote is mentioned).
- **Answer not a nice angle:** 1751624 (self-made problem): angle ACD = arctan((sqrt3 - 2 sin20)/(3 - 2 cos20)), about 43.08 degrees, derived with the law of sines.
- **Conceptual posts turned into exercises:** 1758208 (logarithms, with 2^x = 10 added), 1754490 (probability of a single point is 0), 1754002 (V = rS/3 proved, applied to a regular tetrahedron), 1756531 (aliased), 1754302.

## Diagrams

15 Asymptote figures (all in solutions), drawn from computed coordinates: 1757367-q01 and q02, 1754235-q03, 1756743, 1756275, 1753558, 1754002, 1754336, 1753987, 1751624, 1753684-q01, 1753584, 1753532, 1752547 (two configurations). Fixes made after viewing the sheets: axis labels clashing with tick values and the corner areas (49/2, not 49) in 1757367-q02; wrong slopes of the drawn lines and labels touching lines in 1756275; wrong half-diagonal labels in 1754336; a tetrahedron projection redrawn so that O and C are clear of the edges in 1754002; the radius label moved off the ellipse in 1753987; the angle labels in 1753684-q01 and 1753584 moved off the dashed bisectors (the 73-degree mark was removed because it could not be placed clear of the incircle); captions moved off the sides in 1752547; area captions moved off the hypotenuse in 1757367-q01. Alt text for every figure is in `alts.py`.

## Validation

- `python3 chk.py`: chk OK.
- `python3 precheck.py 227`: PRECHECK OK (82 records, 3 aliases, 15 diagrams).
- `python3 finalize.py 227`: checks passed, no review lines left (three geometry tags without sketches were removed or given a sketch).
- `python3 pdfcheck.py`: 0 LaTeX errors, 0 Asymptote failures, 0 figures whose last label colour is not black: OK.
- Batches 76-80 are still missing from the registry.
