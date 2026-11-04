# AoPS batch 229 processing report

**81 question records** prepared from the 100 topics screened in batch 229 (12 further items are aliased to earlier records).

Claude did all of the work in this batch, with no DeepSeek or other external model. It screened every topic, solved each problem in full before choosing tags and a difficulty, checked every computable answer with exact or brute-force code (`chk_p229_01.py` to `chk_p229_03.py`), and checked every diagram by eye on contact sheets. The builders are `p229_01.py` to `p229_03.py`.

## IDs and duplicates

- IDs have the form `aops-topic-<AoPS topic id>-q<original part number>`. Multi-problem posts:
  - 1742979 (2017 MATHCOUNTS State #16, #17, #21): q16, q17, q21, numbered as in the post (q16 and q17 are aliases, q21 is exported).
  - 1745992 (six circles; area = perimeter): q01 (alias), q02.
  - 1745976 (sum of coefficients; multinomial coefficient): q01, q02.
  - 1745621 (three handbook problems): q01, q02 (aliases), q03.
  - 1743083 (five variations of 2018 AMC 8 problems): q01-q05.
  - 1742992 (pig pen, two questions): q01, q02.
  - 1742540 (five "easy problems"): q01-q05; q01, q04, q05 are aliases.
  - 1742279 (three "400th post" problems): q01-q03.
  - 1740608 (three Math Arcade problems): q01-q03.
  - 1730513 (two problems): q01, q02.
  - 1744022 (two geometry questions): q01, q02.
- 12 repeats are aliased instead of exported:
  - `aops-topic-1742979-q16` -> `aops-topic-2757304-q01` (integer points on (x-3)^2+(y+4)^2=25, max x^2+y^2 = 100; the old record also asks why)
  - `aops-topic-1742979-q17` -> `aops-topic-2006341-q01` (prime times square = other prime times cube, 432)
  - `aops-topic-1745992-q01` -> `aops-topic-1964750-q02` (six circles, 30 intersections; the old record also asks for n circles)
  - `aops-topic-1745621-q01` -> `aops-topic-1755042-q118` (b227 draft of this run: Alvin's mini-golf scores, 27; b227 flagged it in xnotes.md)
  - `aops-topic-1745621-q02` -> `aops-topic-1755042-q119` (b227 draft: die -2,-1,0,0,1,2 rolled three times, sum 0, 19/108)
  - `aops-topic-1574955-q01` -> `aops-topic-1927278-q01` (pentagon with AB = BC, CD = DE, angles 120 and 60, BD = 2, area sqrt 3; same wording)
  - `aops-topic-1741712-q01` -> `aops-topic-2085723-q01` (positive solutions of 9x+17y = 541; the old record has x and y swapped)
  - `aops-topic-1742873-q01` -> `aops-topic-3205072-q01` (2013 AMC 8 #25, ball on three semicircular arcs, 238 pi)
  - `aops-topic-1742540-q01` -> `aops-topic-2154139-q01` (bisector of y = 4x/3 and y = 12x/5, slope 7/4)
  - `aops-topic-1742540-q04` -> `aops-topic-1834078-q01` (n^2 divides n! for 50 <= n <= 99, 40)
  - `aops-topic-1742540-q05` -> `aops-topic-1797123-q01` (pairwise sums 27, 41, 44, 47, 61, smallest 12)
  - `aops-topic-1738754-q01` -> `aops-topic-3223951-q01` (four-letter strings from MATHCOUNTS, 3360)
- Duplicate only: 1574955, 1741712, 1742873, 1738754.
- Cross-batch note written to `work/xnotes.md`: `1743778-q01` (2015 MATHCOUNTS Chapter Sprint #24, overlap of a triangle and its reflection, 1.5) is repeated by the b230 draft `1736178-q01`; b230 should alias to b229. Both lines in xnotes.md addressed to b229 (from b227) have been acted on.
- Near misses kept (same idea, different numbers or target):
  - `1731039-q01` (Dulce eats 10 mints every 11 days, so she never finishes) vs `aops-topic-2953609-q02` (11 mints every 10 days, a weekday answer).
  - `1743083-q04` (area of triangle BFC, 18) vs `aops-topic-1945365-q01` (area of the square, 108).
  - `1743083-q02` (powers of 4 between 2^8+1 and 2^18+1) vs `aops-topic-2959613-q01` (perfect cubes).
  - `1742279-q02`, `1745976-q02`, `1742540-q02`, `1741935-q01` resemble earlier records only in form.
- Several posts titled "Problem N -- ..." (1743700, 1743708, 1744310, 1743694, 1744133, 1743701, 1743705, 1743710, 1743711) appear to be from the 2006 iTest, but the posts do not name the contest, so no source is recorded; this is said in each note.
- `deduplication_registry.json` is cumulative; batches 76-80 are still missing from the registry.

## Screening

Statuses: included 67, partial 1, excluded 28, duplicate 4.

Partial:
- 1731039: Problem 2 (lanterns lit at 60 and 200 per hour) has the non-integer answer 7000/13 for a number of lanterns, and Problem 3 (choose n to "maximise the probability of being as close as possible" to a random mean) is ill-posed; only Problem 1 is used.

Excluded as not usable (beyond non-maths posts):
- Problem only in a missing attachment, figure or linked PDF:
  - 1746248 (two attached geometry questions)
  - 1745055 (net of two squares and six triangles with fold lines; the polyhedron is not fixed by the text)
  - 1740579 (2009 Vestavia Hills Geometry questions in a linked PDF)
  - 1741036 (2007 Vestavia Hills Geometry questions in a linked PDF)
- Ill-posed, or needing a computer search:
  - 1731400 (four-way nerf battle: the turn order omits a player and the other players' strategies are not given)
  - 1743564 (counting distinct sums over all signed factorisations of 69^69 into four factors; computer search)
  - 1741441 (odd functions with a non-standard definition; both questions are vague)
- Marathon opening post with no problem: 1745317 ("Use the Term" marathon).
- Requests to explain a general method with no specific problem: 1742883 (rationalising denominators), 1742661 (Euler's totient), 1744041 (linear vs exponential), 1742097 (Euclidean algorithm), 1740620 (number of factors).

The other 15 excluded topics were non-mathematical: AMC 8 score, honour-roll, release, solution-compilation and discussion threads, course and book questions, app and contest advertisements, scoring rules, "bring back the old AoPS".

## Editorial changes

**Wrong posted answers, ill-posed problems and repairs:**
- `aops-topic-1731039-q01` (Dulce's mints): with 10 mints eaten every 11 days and one mint added daily, the supply grows, so she never finishes; the record keeps the data and gives this answer (no answer was posted).
- `aops-topic-1742264-q01` (roots of -7x^2+3x+1): the poster's answers 0.65 and -0.22 are correct roots with the labels x+ and x- swapped (2a = -14 is negative, so the + sign gives the smaller root); the record asks for the roots and the error. For y = -7, x+ is about -0.88, not 1.3.
- `aops-topic-1745554-q01` (x^6+y^6 = 6969, x^9+y^9 = 69): stated for real x, y; the answer is a count, 2, not an expression in 6969 and 69 as the post suggests.
- `aops-topic-1741603-q01` (triangle in a circle of radius 5 with sides 5 and 6): there are two triangles; the third side is 3 sqrt 3 + 4 or 3 sqrt 3 - 4, both given, with a sketch of each.
- `aops-topic-1741490-q01` (three circles in a rectangle): the figure is missing and the text allows two placements; the placement matching the poster's 0.69 (small circles along the left side) is stated and drawn.
- `aops-topic-1743083-q03`: the post asks for "the volume of EFGHICJ" with no edge length and no figure; the cube labelling is stated and the record asks for the fraction of the cube (1/2).
- `aops-topic-1741984-q01`: "ab = bc = cd" with a(1,3), c(5,1) does not determine b and d; ABCD is taken to be a square.
- `aops-topic-1740548-q01`: the poster thinks the manual's answer 2x^2yz^4 is wrong; it equals x^2yz^4 times the fourth root of 16. The absolute value |y| is added for real y.
- `aops-topic-1745630-q01`: "-13^{n+1} = -13^n + -13^{n-1} mod 181" is read as powers of (-13), the only reading for which it is true.
- `aops-topic-1744972-q01` (107 pigs, two odd pens): a lateral-thinking riddle turned into the parity proof that disjoint pens cannot both be odd.
- `aops-topic-1740624-q01` ("maximise 2x+3y"): the record asks for the proof that there is no maximum.

**Interpretations made explicit:**
- `1746368-q01`: "120 plants could be less planted in 1/3 of the planned time" read as 120 fewer trees in total over the first third (answer 100, as posted).
- `1742456-q01`: the bridge "70 m from the foot of both towers" read as a horizontal bridge at height 70 m.
- `1742842-q01`: "Chip's 4th house is 16 of Dale's house" read as Dale's 16th house.
- `1741190-q01`: "finished in 7 months" read as 7 months in total; both builders take 13 months.
- `1740608-q02`: "how many results" read as distinct total scores (16).
- `1730513-q02`: choosing 8 donuts from 4 kinds with at least one of each (35).
- `1742279-q01`: change given in blops (280) and glops (233 1/3), since it is not a whole number of glops; `q02` "between" read as strictly between; `q03` proportionality stated.
- `1745417-q01`: the box's walls (the material) have the ellipsoid's volume.
- `1734050-q01`: letters counted regardless of case; the solution (six, five, eight) is unique.
- `1745976-q02`, `1742862-q01`, `1741722-q01`, `1742467-q01` and `1743013-q01` give organised or shorter methods, as the posters asked.

## Diagrams

24 Asymptote diagrams (1 question figure, 23 solution figures), all drawn from computed coordinates; every geometry-tagged record has a sketch. Rendered and inspected on contact sheets; fixes made during review: the pentagon of 1574955 redrawn as a convex pentagon (the first choice of C gave a non-convex one; that record is now an alias), the coordinate labels of 1743708, the chord-end labels of 1745435, the mass-point labels of 1744764, the cube view of 1743083-q03, the tower dimension labels of 1742456 and the circle labels of 1741490 and 1741603 moved off lines. Alt text for every figure is in `alts.py`.

## Validation

- `python3 chk.py`: chk OK (exact or brute-force checks for every computable answer, including the Burnside count checked against brute force on small necklaces, the 72 painted cubes, the 277 Connex arrangements, the 8 convex permutations and the unique self-counting sentence).
- `python3 precheck.py 229`: PRECHECK OK.
- `python3 finalize.py 229`: 81 records, 24 previews, checks passed; no slash hits left.
- `python3 pdfcheck.py`: OK (0 LaTeX errors, 0 Asymptote failures, 0 figures whose last label colour is not black).
- Batches 76-80 are still missing from the registry.
