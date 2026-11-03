# AoPS batch 225 processing report

**93 question records** prepared from the 100 topics screened in batch 225.

Claude did all of the work, with no DeepSeek or other external model. It screened every topic, solved each problem in full before choosing tags and a difficulty, checked every computable answer with exact, brute-force or numerical code (`chk_p225_01.py` to `chk_p225_03.py`), and checked every diagram by eye on contact sheets. The builders are `p225_01.py` to `p225_03.py`.

## IDs and duplicates

- IDs have the form `aops-topic-<AoPS topic id>-q<original part number>`. Multi-problem posts:
  - 1763568 (cube ending in ddd; power of 2 in a factorial quotient): q01, q02.
  - 1764048 (factorization match P1-P13): q01-q13 (q08 and q13 are aliases).
  - 1760189 (stars and bars P1-P3): q01-q03.
  - 1763566 (coin game; Heron rationality): q01 exported, q02 alias.
  - 1763571 (units digit; system): q01, q02.
  - 1763561 (circles in perpendicular planes; bananas): q01, q02.
  - 1763250 (units digit problems 1-6): q01-q06.
  - 1762366 (MATHCOUNTS Handbook #148, #149): q148, q149, numbered as in the post.
  - 1757873 (Problems 1-5): q01-q05.
- 10 repeats are aliased instead of exported:
  - `aops-topic-1765675-q01` -> `aops-topic-1945887-q01` (least Heronian area with longest side 17, 36)
  - `aops-topic-1765713-q01` -> `aops-topic-1777350-q01` (b222 draft of this run: Yu's 12 coins, heads worth 30 cents, 23/2048; this post also asks why 5/120 is wrong)
  - `aops-topic-1765571-q01` -> `aops-topic-1915002-q01` (Max's 8 cups of 45 cents, at least 3 dimes, 1/4)
  - `aops-topic-1764048-q08` -> `aops-topic-1981454-q01` (product of 1 - 1/k^2 for k = 2..10, 11/20)
  - `aops-topic-1764048-q13` -> `aops-topic-2653511-q01` (110n^3 has 110 divisors, 81n^4 has 325)
  - `aops-topic-1764520-q01` -> `aops-topic-1904234-q01` (Legendre's formula, posed as a proof)
  - `aops-topic-1763566-q02` -> `aops-topic-2494180-q01` (Heron's expression with rational coordinates is rational)
  - `aops-topic-1763217-q01` -> `aops-topic-1763215-q01` (same batch: isosceles trapezoid whose shorter base is not determined)
  - `aops-topic-1762832-q01` -> `aops-topic-3134177-q09` (clock hands perpendicular 44 times in 24 hours)
  - `aops-topic-1762708-q01` -> `aops-topic-2959613-q01` (AMC 8 2018 #25, cubes between 2^8+1 and 2^18+1, 58)
- Duplicate only: 1765675, 1765713, 1765571, 1764520, 1763217, 1762832, 1762708.
- Cross-batch note written to `work/xnotes.md`: b225 `1762366-q149` (Vida's guppies, 48) repeats the b227 draft `1757353-q02`, so b227 should alias to b225. The xnotes line for this batch (Heronian triangle -> 1945887-q01) was already acted on.
- Near misses kept:
  - `1764048-q12` (2013 AIME I #5: a+b+c = 98) vs `aops-topic-3079410-q01` (same cubic, asks only for the real root).
  - `1763250-q01` (units digit of the sum of n^(n+1)) vs `aops-topic-2496003-q01` (sum of n^n).
  - `1764786-q01` (largest impossible score with 7 and 3) vs earlier two-coin Frobenius records with other numbers.
  - `1763339-q01` ((a+b+c+d+e)^19) vs `aops-topic-2386383-q01` and the b226 draft `1759128-q04` (other exponents and variables).
- `deduplication_registry.json` is cumulative; batches 76-80 are still missing from it.

## Screening

Statuses: included 68, partial 0, excluded 25, duplicate 7.

Excluded as not usable (beyond non-maths posts):

- The problem is only in a link, a PDF, a book or a missing figure:
  - 1765557 (2015 MATHCOUNTS State Sprint #26, #28-30)
  - 1764680 (2018 MATHCOUNTS Chapter Sprint #23, #30)
  - 1764807 (Introduction to Algebra p. 477)
  - 1718807 (2005 MATHCOUNTS State #29)
  - 1762747 (2017 MATHCOUNTS National Sprint #28)
  - 1762514 (circles-in-rectangle figure and statement missing; only the poster's working is given)
- Missing figure that the text does not determine: 1762562 (three semicircles "all with the same radius" on a rectangle).
- Ill-posed joke puzzles: 1763559 ("pounded snowflakes" trades), 1763556 ("mudkips and blueberries").
- No concrete exercise: 1762552 (does a McNugget formula exist for three or more numbers; there is no closed formula).

The other 15 excluded topics were non-mathematical:
- terminology questions (factors versus divisors, the meaning of "common fraction") and a request for an explanation of Vieta's formulas
- calculator rules, MATHCOUNTS and AMC preparation and score advice, book recommendations
- advertisements (a Google classroom, a prep-game forum), hardest Chapter years, competition eligibility, unit-conversion rules for a mock test

## Editorial changes

**Wrong posted answers, ill-posed problems and repairs:**

- `1766133-q01` (24 terms of 5832 + 1944 + 648 + ...): neither the key's 8747 nor the poster's 8748 is exact; the sum is 8748 - 4/3^17.
- `1765813-q01`: "prove that n^2+5n+1 is divisible by 49" is false; the record proves it is never divisible by 49.
- `1765152-q01`: the "minimum" of x^3y^2z with 3x+2y+z = 12 does not exist; changed to the maximum for positive x, y, z (64).
- `1765863-q01`: the poster's -15/16 is the value at x = -5/2 (a local maximum); the minimum is -1.
- `1762366-q148`: the poster's 10 is wrong (W and Y are opposite vertices); the answer is 18. `q149`: the poster's n = 24 fails; the values are 13 and 35 (sum 48).
- `1762187-q01` (CMIMC 2018): the post's angle ABP = 2 degrees is a typo for 20 degrees; answer 35.
- `1763566-q01`: the probability that Albert wins round 2018 has no useful closed form (a fraction with denominator 7^2018), so the record asks for round 3 (100/343) and a proof that the round-2018 probability is within 10^-300 of 1/3.
- `1763571-q02`: the system has several real solutions, so a, b, c are taken to be positive integers (unique solution 9, 10, 21; sum 40).
- `1763710-q01`: "non-negative digits" with repeats would make the set of two-digit numbers ambiguous; the record takes nonzero digits and the nine ordered choices counted with repetition (S = 33(a+b+c); answers 113, 131, 311, 122, 212, 221).
- `1757873-q02`: the garbled condition "AD=DE=?EC=DC?" is read as the standard AD = DE = EC = CB (angle 180/7 degrees); the literal reading would not use AB = AC.
- `1764326-q01`: "all the blue balls are drawn before all of the green or yellow balls" is read as "blue is the first colour used up", the only reading matching a choice (153/455, B).
- `1763215-q01`: the shorter base of the trapezoid is not determined; the record shows this and finds the error in the "three equilateral triangles" argument (the poster of 1763217 had the same question).
- Posts asking why an argument fails (the record gives the answer and the error): `1763749-q01` (why 4*3*2*1*4*4 overcounts the donuts, answer 10), `1763513-q01` (Descartes' rule allows 2 or 0 negative zeros), `1766239-q01` (|5-12i| = 13, not 5 + sqrt 12), `1765191-q01` (the "sum is 0" argument rearranges a conditionally convergent series).

**Interpretations made explicit:**
- 1766101-q01: "perfect factors" read as perfect square factors (12; the poster's list was complete).
- 1765846-q01: "5exp(x)" read as 5^x (x = 0 or 2); the literal 5e^x has no solution.
- 1754151-q01: improper divisors of m are 1 and m.
- 1765742-q01: letters may repeat and A-M is inclusive (13^4 = 28561; distinct letters would give 17160).
- 1764818-q01: base-10 logarithm.
- 1764798-q01: ages are whole numbers (23).
- 1760189-q01: x_i in N read as positive integers (1330).
- 1764009-q01: the missing figure is rebuilt from the text (G on BC, A between E and F); DE = 16/5 by areas, suitable for a 4th grader as asked.
- 1765109-q01: the missing figure is rebuilt from the description; 55 isosceles triangles.
- 1763561-q01: the perpendicular planes play no role; minimum sqrt 7.
- 1763561-q02: bananas treated as divisible (275/8).

**Posts turned into questions:** 1766350 (formula for 1, 5, 21, 85, ...), 1765746 (base x and x+1), 1765494 (interval notation), 1765502 (sign pyramid with an explanation of XOR), 1764218 (5P2 and whether order matters), 1764107 (all a, b with a, a^2, ..., a^b a complete residue system mod b: only b = 1), 1763339 (number of terms with the general formula).

**Unsolved posts solved:** 1763286-q01 (leash around a hexagonal barn) has no posted answer; the exact area 381600 pi - 129600 arctan(sqrt 11) + 10800 sqrt 11 - 3600 sqrt 3 accounts for the overlap behind the far vertex, and was checked by Monte Carlo and numerical integration.

## Diagrams

There are 22 Asymptote diagrams in the exported records: 20 in solutions and 2 in questions (1764009-q01, 1765109-q01). Each has an SVG preview and alt text. Every geometry-tagged record has a solution sketch (sketches were added to 1763579-q01 and 1763222-q01 after finalize flagged them). No geometry tags were used for 1762815-q01 (square counting) or 1762832 (clock; aliased).

Fixes after viewing the contact sheets:
- 1762944-q01: the tangent points were wrong (angle AOB is 30 degrees, not 60), so the tangents crossed the circle; recomputed. The 120 degree label did not fit inside the narrow angle and is now a caption; A and C labels moved off the circle.
- 1763286-q01: sector angles corrected, vertex labels moved outside the hexagon, radius labels moved onto dashed radii.
- 1764322-q01: side labels moved off the medians; G and D labels moved off lines.
- 1764207-q01: a "1 - y" label sitting on segment FB was removed.
- 1763215-q01: base labels moved below AB.
- 1763615-q01: the dashed diagonals and labels touching the axes were removed or moved.
- 1763561-q01: labels O1, O2, T2, sqrt 7 and 30 degrees moved off lines and circles.
- 1762366-q148: a variable named W redirected the label of Z (the W-alignment quirk); renamed, and labels moved off the axes and diagonals.
- 1762187-q01: angle labels moved off the rays.
- 1757873-q02: figure enlarged (it was drawn too small).
- 1763222-q01, 1763579-q01: labels moved off rays and tick marks.

## Validation

- `chk.py`: `chk OK` (3 check files).
- `precheck.py 225`: `PRECHECK OK`. 93 records exported, 10 aliases, 100 topics accounted for, 22 diagrams.
- `finalize.py 225` (pre-check mode): 93 question records, 22 previews (0 missing, all compiled), 302 ZIP members, `checks_passed: true`. The review list contains only text slashes ("yes/no", "ft/s" in prose) and no "GEOMETRY WITHOUT SKETCH" lines.
- `pdfcheck.py`: `records=93 asy_files=22 asy_failures=0 pages=94`, `warnings: 0`, no colour leak, `OK`.
