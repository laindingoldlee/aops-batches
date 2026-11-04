# AoPS batch 232 processing report

**73 question records** prepared from the 100 topics screened in batch 232.

Claude did all of the work in this run, with no DeepSeek or other external model. It screened every topic and solved each problem in full before choosing tags and a difficulty. Every computable answer was checked with exact or brute-force code (`chk_p232_01.py` to `chk_p232_03.py`), and every diagram was checked by eye on contact sheets. The builders are `p232_01.py` to `p232_03.py`.

## IDs and duplicates

- IDs have the form `aops-topic-<AoPS topic id>-q<original part number>`. Multi-problem posts:
  - 1726281 (four geometry problems): q01-q04.
  - 1723237 (2019 MATHCOUNTS Handbook stretch, problems 1-4): q01-q04.
  - 1725606 (Texas A&M problems 1, 2): q01, q02.
  - 1726370 (MATHCOUNTS School problems 24 and 27): q24, q27. q27 is an alias.
  - 1721070 (MATHCOUNTS warm-up problems 75 and 79): q75, q79.
  - 1724486 (problems 1-3): q01 and q03 are exported; q02 is an alias.
  - 1724620: q01 is the pentagon problem; q02 (cyclic hexagon, no data) is dropped; q03 and q04 are aliases.
  - 1721154 (D&D questions 1-5, one setup): kept together as one record, q01.
- 17 repeats are aliased instead of exported:
  - `aops-topic-419795-q01` -> `aops-topic-2331237-q01` (2003 AMC 8 #17, Jim's siblings)
  - `aops-topic-1726572-q01` -> `aops-topic-3437845-q01` (triangles on a 5 by 5 array of points, 2148)
  - `aops-topic-1727994-q01` -> `aops-topic-3579886-q01` (sum of 1/odd^2 = pi^2/8)
  - `aops-topic-1721571-q01` -> `aops-topic-2968475-q01` (lattice points inside x^2+y^2=8, 124/133)
  - `aops-topic-1726537-q01` -> `aops-topic-2953609-q05` (candies with remainders mod 11, 100, 101; 697 bags)
  - `aops-topic-1727051-q01` -> `aops-topic-2449983-q01` (USAMO 1972 #1 gcd/lcm identity, part (c) of the old record)
  - `aops-topic-1726538-q01` -> `aops-topic-2431035-q08` (2015 AMC 8 #15, 99)
  - `aops-topic-1726370-q27` -> `aops-topic-1962602-q01` (seven jars, 36)
  - `aops-topic-1726419-q01` -> `aops-topic-1788416-q01` (11^12 mod 13)
  - `aops-topic-1724620-q03` -> `aops-topic-1726281-q01` (LMNO about a circle, 60; same poster, repeated in this batch)
  - `aops-topic-1724620-q04` -> `aops-topic-1726281-q02` (box with surface area 14 and diagonal 8, 78; same)
  - `aops-topic-1724486-q02` -> `aops-topic-1723304-q01` (minimum of sqrt(2x^2-3)+sqrt(3x+5), 16; repeated in this batch)
  - `aops-topic-1723431-q01` -> `aops-topic-2844439-q01` (sum of F_n/10^n = 10/89)
  - `aops-topic-1723636-q01` -> `aops-topic-2565823-q01` (digit sums divisible by 7 from 24 to 125, 14)
  - `aops-topic-1723135-q01` -> `aops-topic-2268306-q01` (sum of four-digit palindromes, 495000)
  - `aops-topic-1725534-q01` -> `aops-topic-1877656-q01` (2018 MATHCOUNTS National Sprint #30, glide reflection, 5/11)
  - `aops-topic-1725061-q01` -> `aops-topic-1735512-q85` (median of numbers below 2000 with digit sum 24, 1878)
- Within the batch, repeats are aliased to the topic that comes first in the source file (1726281 before 1724620, 1723304 before 1724486).
- Duplicate only (13 topics): 419795, 1726572, 1727994, 1721571, 1726537, 1727051, 1726538, 1726419, 1723431, 1723636, 1723135, 1725534, 1725061.
- Cross-batch notes written to `work/xnotes.md`. Three b233 draft records (1717359-q01, q02, q04) repeat this batch's 1724486-q03, 1723304-q01 and 1724486-q01, so b233 should alias to b232. The line addressed to b232 (1725534 -> 1877656-q01) was acted on.
- Near misses kept (same idea, different numbers or target):
  - `1726527-q01` (Halloween logic, "reveal" a funny costume) vs `aops-topic-2953609-q04`. The old record changed "reveal" to "wear" and gets answer (e); this record keeps the original wording, where none of (a)-(e) must hold.
  - `1727026-q01` (5^n with leading digit 1 for n <= 2018, 607) vs `aops-topic-2752973-q01` (n < 2019 with 5^2019 given).
  - `1724261-q01` (x^4 + 2^(4n+2) prime) vs `aops-topic-1972985-q01` (n^4 + 4).
  - `1722616-q01` (sqrt(2x+7) = x+2, plus cubing) vs `aops-topic-3361787-q01` (sqrt(x+2) = x).
  - `1726968-q01` (self-inverse linear functions) vs `aops-topic-1953987-q01` (a self-inverse rational function).
  - `1726398-q01` (inverse of x^2 restricted) vs `aops-topic-3293110-q01` (a different quadratic).
- `deduplication_registry.json` is cumulative; batches 76-80 are still missing from the registry.

## Screening

Statuses: included 60, partial 4, excluded 23, duplicate 13.

Partial:
- 1727026: problems 2 and 3 (general formulas for 1^k + ... + n^k, integer and rational k) have no definite answer; only problem 1 is used.
- 1724620: "how do you find the circumradius of a cyclic hexagon" has no data and is dropped. Its two other questions are aliases.
- 1724204: the exact largest N for 3, 4 and 5 colours (weak Schur numbers) needs a computer search and is dropped. The record proves that the process always stops.
- 1723583: questions 2-4 (optimal algorithm, graphing 4-variable systems, dimensions of the universe) are not definite maths questions.

Excluded as not usable (beyond non-maths posts):
- 1728291: numbers that appear inside their cubes; it asks whether there are infinitely many, which is open-ended and computer-search only.
- 1727565: the figure ("in the diagram") is missing.
- 1702796: no problem text.
- 1712857: Five 5s; an open-ended search with no definite question.
- 1726063: garbled, vague prime-power question.
- 1725379: "fair-and-square" sets up to 1000; needs computer enumeration.
- 1724305: points I, G, P are defined only in the attachment.
- 1724593: asks for the statement of Casey's theorem.
- 1720939: estimate of the number of chess positions; no definite answer.
- 1723315: no 6-digit factorion; the proof needs a computer search. The related 1721400 is used instead.
- 1719309: asks only how to compute cube roots.

The other 12 excluded topics are non-mathematical: AMC 8 versus a math-team meeting, the AMC 8 wiki solution, mock AMC logistics, MATHCOUNTS posting guidelines, a MATHCOUNTS poll, MathWorks advice, AMC 8 materials, a difficulty scale, "why contests use advanced topics", Vietnamese spam, min notation, and a general question about modular inverses.

## Editorial changes

**Wrong posted answers, ill-posed problems and repairs:**
- `1724972-q01`: the posted triangle (AB = 15, semiperimeter 24, cos C = 13/27) does not exist. With a + b = 33 and c = 15, cos C >= 71/121 > 13/27. The record asks for a proof of impossibility instead of the circumradius.
- `1724982-q01`: (s - c)/R = cot C + csc C is false with R the circumradius (the equilateral triangle is a counterexample). It is true with the inradius r. The record asks for both.
- `1722309-q01`: the claim that the inner quadrilateral is always 1/5 of the quadrilateral is false (151/756 for the right trapezoid (0,0), (2,0), (2,2), (0,4)). It is proved for parallelograms.
- `1724486-q03`: AE = 9 contradicts CD = 5 and DE = 1 (the angle bisector theorem would give AC = 45 > AE + EC). CD and DE alone force AE = sqrt(5)/2, so AE = 9 is dropped and the answer is AC = 5 sqrt(5)/2.
- `1723548-q01`: 5, 5, 12 do not fit at a vertex (108 + 108 + 150 = 366). The configuration is corrected to 5.5.10, which does fit, and the record proves it cannot tile the plane.
- `1726492-q01`: the requested "simplest radical form" is impossible; the answer is the rational 9/13.
- `1726581-q01`: the post's hint suggests a hidden division by zero. The real flaw is that the hypotheses are inconsistent (n = 0 gives f = 0).
- `1724568-q01`: the poster's 5 mph is wrong; the time-weighted average is 4.92 mph.
- `11090-q01`: both answers are given: 65 for positive squares, 25 when 0 is allowed.

**Interpretations made explicit:**
- 1728070-q01: D on AC and E on AB (no figure was given).
- 1727959-q01: each of 1-16 used exactly once. There are exactly two completions.
- 1727026-q01: the digit count (1411) and leading digit (3) of 5^2018 are supplied.
- 1727049-q01: "within one" means distance less than 1.
- 1727169-q01: squares of nonnegative integers (43); for positive squares the answer is 35.
- 1726274-q01: the garbled locus question is restated. The answer is the ellipse y^2 = 4kx - 4x^2 without (k, 0).
- 1726281-q03: the circle passes through Z and G and touches EN at its midpoint (the post says "tangent to Z, and G").
- 1725452-q01: a square with a side on a side of the triangle (the largest inscribed square).
- 1725457-q01: real a with a possibly complex common root; the answer is still a = -2.
- 1725566-q01: the summation index typo is corrected.
- 1725606-q01: the lost exponents are restored.
- 1724486-q01: the coefficients have gcd 1, which makes 13 unique.
- 1724261-q01: n = 0 is allowed; the only solution is x = 1, n = 0.
- 1722852-q01: a 6 by 6 array of points (11/63). For 7 by 7 points the answer would be 13/98.
- 1722825-q01: "domain" means the x values for which some y exists.
- 1722491-q01: "does not diverge" is read as bounded, giving [-2, 1/4].
- 1724204-q01: a < b distinct, as the poster's colouring implies.
- 1723400-q01: the hexagon is named, and its area is found in terms of T, a, b, c and x.
- 1724416-q01: convex polygons.

**Posts turned into questions:**
- 1726968: classify the self-inverse linear functions.
- 1726398: no inverse of x^2 on all reals; the restriction to x >= 0 has inverse sqrt(x).
- 1726675: why a tetrahedron has 6 edges.
- 1726526: prove that the Fibonacci units digits have period 60.
- 1726318: proof of the odd-divisor count of consecutive sums.
- 1725176: a 2^a = 3 has exactly one real root, between 1 and 3/2.
- 1723583: false for nonlinear equations, true for linear systems.
- 1724204: Schur-type finiteness via a Ramsey argument.
- 1721400: verify 40585 and prove that a factorion has at most 7 digits.
- 1722616: an extraneous root from squaring, and why cubing is safe.
- 1724087: find the lost root (-1).
- 1723123: the general term 2n^2 - 3n + 6.

## Diagrams

There are 20 Asymptote diagrams in the exported records, 19 in solutions and 1 in a question. Each has an SVG preview and alt text. The question figure (1725534) is now in an aliased record, so the exported records' only question figure is gone. All exported figures are solution sketches: every geometry-tagged exported record has one. Proportions are true, except two figures that are marked "not to scale" (1726281-q01 and q02).

Fixes after viewing the contact sheets:
- 1728070-q01: the angle arcs at C were shrunk so the tick mark on CD no longer touches them. Confusing double ticks on AB and AC (overlapping the single tick on CD) were removed.
- 1726274-q01: the two k labels were moved apart from the crossing of the focal segments. The a = 3 label was moved next to its curve.
- 1725794-q01: the y = x/4 label was moved off the dashed line.
- 1726281-q04: the height label was moved inside the trapezoid, clear of the leg label 6.
- 1725821-q01: the line labels were moved off the square's border, and the axis labels off the tick numbers.
- 1723237-q01/q02: the figures were enlarged, and the R label was moved off the y-axis.
- 1725534: the C, P and K labels were moved off lines (now aliased).
- 1724620-q01: the O label was moved off the red radius.
- 1724972-q01: the a + b = 33 label was moved off the ellipse, and the a label off the blue dashed line.
- 1724982-q01: the triangle was made taller so the C/2 label fits inside the angle without touching the incircle or the r label.
- 1724486-q03: the E and D labels were separated from the "1" label.
- 1723400-q01: the vertex labels were moved into the triangle, off the sides.
- 1724416-q01: the exterior angles are now drawn at the correct sides (extensions of DA and BC), and the A and C labels were moved off the lines.
- 1723548-q01: the polygon names and angle labels were moved off the edges, and the unused V label was removed.

## Validation

- `chk.py`: `chk OK` (3 check files). They include exhaustive checks of the grid puzzle, D&D distribution, factorions up to 2540160, prime pairs and polynomial coefficients.
- `precheck.py 232`: `PRECHECK OK`. 73 records exported, 17 aliases, 100 topics accounted for, 20 diagrams.
- `finalize.py 232` (pre-check mode, registry chained from b231's draft output): 73 question records, 20 previews (0 missing, all compiled), 240 ZIP members, `checks_passed: true`. There are no slash hits and no "GEOMETRY WITHOUT SKETCH" lines.
- `pdfcheck.py`: `records=73 asy_files=20 asy_failures=0 pages=73`, `warnings: 0`, no colour leak, `OK`.
