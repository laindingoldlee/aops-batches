# AoPS batch 228 processing report

**86 question records** prepared from the 100 topics screened in batch 228.

Claude did all of the work in this batch, with no DeepSeek or other external model. It read every topic and solved each problem in full before choosing tags and a difficulty. Every computable answer is checked with exact or brute-force code (`chk_p228_01.py` to `chk_p228_03.py`), and every diagram was checked by eye on contact sheets. The builders are `p228_01.py` to `p228_03.py`.

## IDs and duplicates

- IDs have the form `aops-topic-<AoPS topic id>-q<original part number>`. Multi-problem posts:
  - 1751255 (dice L+G; triangle area): q01, q02.
  - 1752100 (Burton 1-3): q01-q03; q01 is an alias.
  - 1750969 (three mock problems): q01-q03.
  - 1750568 (Q1-Q3): q01-q03; q02 is an alias.
  - 1750107 (Burton 1-3): q01-q03; q02 is an alias.
  - 1748599 (four Handbook problems): q01-q04.
  - 1749683 (5^2012 mod 7; units digit of 13^2012): q01, q02; q02 is an alias.
  - 1749176 (Handbook Warm-Up 7 #92, #97, #99): q92, q97, q99, numbered as in the post.
  - 1748217 (parallel chords; walking polygons): q01, q02.
  - 1747731 (four discarded mock problems): q01-q04.
  - 1738203 (problems 1, 2a, 2b): q01 is problem 1, and q02 keeps 2a and 2b together.
  - 1746203 (Burton 1-4): q01-q04; q01 and q04 are aliases.
  - 1749896 (continued fraction; nested radical): q01 is an alias and problem 2 is dropped.
- 14 repeats are aliased instead of exported:
  - `aops-topic-1752607-q01` -> `aops-topic-2039398-q01` (mean of three-digit numbers with digits in {2,0,1,9}, 433)
  - `aops-topic-1752245-q01` -> `aops-topic-2121575-q01` (Mandelbrot: (sqrt2-1)^(1-sqrt3)/(sqrt2+1)^(1+sqrt3) = 3-2sqrt2)
  - `aops-topic-1752100-q01` -> `aops-topic-2191161-q01` (Burton: a = qb + r with 2b <= r < 3b)
  - `aops-topic-1750568-q02` -> `aops-topic-2302477-q01` (arithmetic/geometric four integers with ratio 5/4, 73)
  - `aops-topic-1750107-q02` -> `aops-topic-3084312-q14` (product of four consecutive integers plus 1 is a square)
  - `aops-topic-1749896-q01` -> `aops-topic-2142056-q01` (continued fraction 1/(2+3/(4+5/(6+...))))
  - `aops-topic-1749903-q01` -> `aops-topic-1978274-q01` (Pascal's identity)
  - `aops-topic-1749553-q01` -> `aops-topic-2792017-q01` (six gifts to five children, 1800)
  - `aops-topic-1749683-q02` -> `aops-topic-2296137-q01` (units digit of 13^2012, 1)
  - `aops-topic-1747690-q01` -> `aops-topic-1961160-q01` (2006 AMC 10A #13, fair game, $60)
  - `aops-topic-1747361-q01` -> `aops-topic-2668968-q06` (the five Platonic solids)
  - `aops-topic-1741498-q01` -> `aops-topic-1962686-q01` (Clark and Chloe, fruit chew, 2/5)
  - `aops-topic-1746203-q01` -> `aops-topic-2623567-q01` (odd a gives a^2 = 1 mod 8)
  - `aops-topic-1746203-q04` -> `aops-topic-2749876-q01` (a coprime to 6 gives a^2 = 1 mod 24)
- Duplicate only: 1752607, 1752245, 1749896, 1749903, 1749553, 1747690, 1747361, 1741498.
- Near misses kept (same idea, different numbers or target):
  - `1706241-q01` (x + 1/x = 4, find x^5 + 1/x^5) vs b223 draft `1778686-q01` (x + 1/x = 5, x^4 + 1/x^4) and older x^4 records.
  - `1750107-q01` (two odd squares never sum to a square) vs `aops-topic-2478804-q01` (the sum is not divisible by 4).
  - `1749683-q01` (5^2012 mod 7) and `1750115-q01` (units digit of 13^2003) are near the aliased 13^2012 record.
- No repeat across the other drafts of this run was found. Nothing in `work/xnotes.md` is addressed to batch 228, and this batch added no line to it.
- `deduplication_registry.json` is cumulative; batches 76-80 are still missing from the registry.

## Screening

Statuses: included 69, partial 0, duplicate 8, excluded 23.

One topic, 1749896, had a part dropped: problem 2 (the nested radical sqrt(1+sqrt(2+sqrt(3+...)))) has no known closed form. Its problem 1 is aliased, so the topic counts as a duplicate.

Excluded as not usable (beyond non-maths posts):
- No problem text:
  - 1751755 (Introduction to Algebra 6.20 not stated)
  - 1751354 (Introduction to Algebra 6.7 and 6.2.6 not stated)
  - 587127 (2013 MATHCOUNTS National Target #8 not stated)
  - 1746850 (diagram only in a missing image)
- Ill-posed:
  - 1751576 (a square is "randomly divided into 5 triangles", with no distribution given)
  - 1748405 (card packs: the grey and yellow probabilities are missing and the constraints contradict independent draws)
  - 1746868 (pattern puzzle 2*6=20, 3*9=51, 7*5=27 with no rule; many rules fit)
  - 1744964 (the degree-12 "challenge" polynomial does not factor over Q(pi), and its real zeros have no hand closed form; probably mistyped)
- Open-ended: 1749961 (find patterns in Pascal's triangle).

The other 14 excluded topics were non-mathematical:
- Arete Labs, AMC 8 scores and difficulty, the 2018 AMC 8 answer key
- a combinatorics handout, "is there an LCM trick", "a problem that uses the Chicken McNugget theorem", "what is casework"
- book and preparation advice (AoPS Volume 1, algebra 2 or geometry, how to prepare for AMC 8)
- past MATHCOUNTS champions
- calculator and linear-form polls

## Editorial changes

**Wrong posted answers, false claims and repairs:**
- `1750568-q03` (jet between two cities): the poster's 399.3 is wrong. The distance is 3187.5 miles.
- `1747574-q01`: the claim "if n is triangular then so are 9n+1, 25n+1, 49n+1" is false for 25 and 49 (n = 1 gives 26 and 50). The record proves the 9n+1 case and asks for the correct constants, 25n+3 and 49n+6 (in general (2m+1)^2 n + T_m).
- `1747797-q01`: as posted, the "maximum" of (x-y+1)(y-z+2)(z-x+3) does not exist, because the product is unbounded. The record shows this in part (a) and adds the condition that all factors are positive (maximum 8) in part (b).
- `1748824-q01` (n^2+4 prime conjecture): false (n = 2, and 23^2+4 = 533 = 13*41). The record also explains why primes ending in 1 or 9 always fail (n^2+4 is divisible by 5).
- `1684977-q01` (C(n,6) = C(n,3)): the poster's n = 0, 1, 2, 9 is correct over the nonnegative integers. The key's n = 9 is the only solution with a positive number of ways, and the record explains both.
- `1747922-q01`: the poster's C(11,5)*7! is corrected to C(11,4)*7! = 1663200 queue arrangements (330 solutions).
- `1746979-q01` (Introduction to Algebra 5.3.4): the manual is right that the system has exactly one solution; the record proves it.
- `1748211-q01`: 98 lattice points (the friend's answer), not 32.
- Confirmed posted answers: 85 (2014 School Sprint #24), 25, 87 and 28 (Warm-Up 7), 10 for the two circles and an ellipse (with an explicit configuration), 2/5 and $60 (aliased records).

**Interpretations made explicit:**
- 1752850-q01: products written as juxtaposition; the value 78 is forced, so "maximum" is kept.
- 1752843-q01: the customer pays the least possible amount, and free bars count toward the limit of 8. The domain is {0,...,8}.
- 1751545-q01: natural numbers read as positive integers.
- 1751518-q01: "find M >= ?" read as the best lower bound (5).
- 1750909-q01: "two distinct circles and ellipses" read as two circles and one ellipse.
- 1750969-q01: the two actors are unordered. 1750969-q03: the hemisphere's cube stands on the flat face.
- 1750568-q01: P lies on line AB beyond A.
- 1748217-q02: the walkers keep repeating the pattern. The solution proves that they can meet only at the start (LCM 1440).
- 1747745-q01: phi is iterated from every n >= 10 (answer 3, S = {4,6,8}). With one-digit n included unchanged, S would trivially be {1,...,9}.
- 1747731-q02: arrivals are uniform and independent, and "all see each other" means every pair overlaps (2/27). The usernames are replaced by names.
- 1747731-q04: the points m, l, c are renamed O, H, G.
- 1706241-q01: "(x^5)/1+x^5" read as x^5 + 1/x^5 (724).
- 1738203-q02: a new arrangement every 4 weeks over a 36-week year gives 9 independent arrangements.
- 1742452-q01: the two selections are independent.
- 1749150-q01: "how many times greater" read as "how many times as large" (8).

**Posts turned into questions:**
- 1738877-q01: "is a Casio-able cycling function possible" became a proof by Lagrange interpolation.
- 1745114-q01: the divisibility-by-4 congruence chain became an explanation plus the general rule.
- 1749804-q01: "is the cube root the double square root" became a counterexample and the correct rule.
- 1749458-q01: formulas for strictly increasing (C(9,n)) and decreasing (C(10,n)) n-digit numbers.
- 1747765-q01: the zeta(-1) = 1+2+3+... "identity" became "find the error".
- 1747120-q01: (-2)(3) = -6 and (-2)(-3) = 6 derived from the distributive law.
- 1746837-q01: true or false on constructing a parallelogram from its diagonals and the angle between them (true, with construction and SAS uniqueness).
- 1749495-q01: the space diagonal of a box.
- 1746517-q01 (pairwise sums are squares): the poster's open parts (b) and (c) both have examples. The four-number sets come from a three-way sum-of-two-squares construction, and the five-number set {7442, 28658, 148583, 177458, 763442} is a known example; all sums were verified.

## Diagrams

The exported records contain 18 Asymptote diagrams, all in solutions. Each has an SVG preview and alt text, and every geometry-tagged record has a solution sketch. The finalize check first flagged 1748211-q01 (Hyperbolas, Lattice points) as a geometry record without a sketch, so a hyperbola sketch with sample lattice points was added.

Fixes after viewing the contact sheets:
- 1751902-q01: labels moved off line g, and the (-3,-10) label moved into the gap between the lines.
- 1751211-q01: the C label moved off side BC (coordinates kept in the text).
- 1751050-q01: the M label moved off the axis and diagonal, and the (1,-6) label moved off the y-axis.
- 1750969-q03: the x label moved off the dashed radius.
- 1749495-q01: the long face-diagonal label, which crossed an edge, replaced by e, with e defined in the text.
- 1749331-q01: the second strip line extended so that the width arrow ends on it, and the width and angle labels moved clear.
- 1748217-q02: polygon captions moved inside the polygons, so the polygons are no longer shrunk by wide labels.
- 1747731-q04: a different triangle chosen so that O, G and H are spread out and their labels clear the Euler line.
- 1746837-q01: the angle mark and half-diagonal labels rearranged so that none touches a side.
- 1746950-q01: the base label moved off the foot of the altitude.

## Validation

- `chk.py`: `chk OK` (3 check files).
- `precheck.py 228`: `PRECHECK OK`. 86 records exported, 14 aliases, 100 topics accounted for, 18 diagrams.
- `finalize.py 228` (pre-check mode): 86 question records and 18 previews (0 missing, all compiled), with `checks_passed: true`. The review list is empty: no slash hits and no "GEOMETRY WITHOUT SKETCH" lines.
- `pdfcheck.py`: `records=86 asy_files=18 asy_failures=0 pages=86`, `warnings: 0`, 0 figures whose last label colour is not black, `OK`.
