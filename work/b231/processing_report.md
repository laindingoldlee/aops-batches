# AoPS batch 231 processing report

**79 question records** prepared from the 100 topics screened in batch 231.

Claude did all of the work in this run, with no DeepSeek or other external model. It screened every topic and solved each problem in full before choosing tags and a difficulty. Every computable answer was checked with exact or brute-force code (`chk_p231_01.py` to `chk_p231_03.py`), and every diagram was checked by eye on contact sheets. The builders are `p231_01.py` to `p231_03.py`.

## IDs and duplicates

- IDs have the form `aops-topic-<AoPS topic id>-q<part number>`. Multi-problem posts:
  - 1734624 (Warm-Up 3 #8 bus, #10 diagonals): q01, q02.
  - 1732087 (two circles; equiangular hexagon): q01, q02.
  - 1731770 (problems 1 and 2): q01 exported, q02 aliased.
  - 1731843 (three MATHCOUNTS warm-up problems): q01 aliased, q02 and q03 exported.
  - 1657695 (2018 MS MTE Theme Round, problems 1-15): q01-q15, numbered as in the post.
  - 1729694 (Adam's number; the poster's example of the 7 and 11 problem): q01 exported, q02 aliased.
  - 1727717 (AoPS edition problems 1-6): q01 aliased, q02-q06 exported.
  - Marathon threads 1730463 (cows), 1268207 (logic), 1732030 (paradoxes): only P1 is in the post, so q01.
- 17 repeats are aliased instead of exported:
  - `aops-topic-1733681-q01` -> `aops-topic-2699084-q01` (prove the sum-of-squares formula)
  - `aops-topic-1731581-q01` -> `aops-topic-2796248-q15` (cookies in packs of 8, 12, 15; answer 49)
  - `aops-topic-1731770-q02` -> `aops-topic-2013862-q01` (three random reals with sum at most 1; answer 1/6)
  - `aops-topic-1732169-q01` -> `aops-topic-2741151-q01` (primes greater than 3 are 6n +/- 1)
  - `aops-topic-1731843-q01` -> `aops-topic-1749176-q92` (Ken and Gunther's 14-card deck; answer 25; same wording, from the previous run)
  - `aops-topic-1731473-q01` -> `aops-topic-2796272-q12` (least divisorous number; answer 270)
  - `aops-topic-1731478-q01` -> `aops-topic-2796272-q10` (2^2000 mod 13; answer 9)
  - `aops-topic-1731491-q01` -> `aops-topic-2796079-q07` (11^2014 mod 1000; answer 241; the poster dropped the binomial coefficients)
  - `aops-topic-1730716-q01` -> `aops-topic-2795007-q13` (integer x with sqrt(x + sqrt2011/2) - sqrt(x - sqrt2011/2) an integer; answer 503)
  - `aops-topic-1730856-q01` -> `aops-topic-3525656-q01` (divisibility rule for 11; contained in the earlier record)
  - `aops-topic-1730652-q01` -> `aops-topic-2796070-q14` (rectangle with DF = FE = EC; XY/BD = 3/20)
  - `aops-topic-1268207-q01` -> `aops-topic-2503978-q01` (100 lockers; the perfect squares stay open)
  - `aops-topic-1729694-q02` -> `aops-topic-2527370-q14` (largest number not a sum of 7s and 11s; answer 59)
  - `aops-topic-1726545-q01` -> `aops-topic-2953609-q06` (random walk of me and the spider on a tetrahedron; answer 9/2)
  - `aops-topic-1635216-q01` -> `aops-topic-3109577-q01` (prove the Pythagorean theorem)
  - `aops-topic-1726530-q01` -> `aops-topic-2953609-q03` (death eater on Cherrison Street; answer 467/480)
  - `aops-topic-1727717-q01` -> `aops-topic-3112371-q04` (permutations of AOPS; answer 24)
- Duplicate only (every part aliased): 1733681, 1731581, 1732169, 1731473, 1731478, 1731491, 1730716, 1730856, 1730652, 1268207, 1726545, 1635216, 1726530.
- Near misses kept (same idea, different numbers or target):
  - `1076780-q01` (max + min of a rational function) vs `aops-topic-2842564-q01` (a different function).
  - `1727878-q01` (BF:FG with E, D, F given) vs `aops-topic-3174817-q08` (different data, G given).
  - `1732087-q01` (circles with common chord, general a, b, c) vs `aops-topic-3236990-q01` (numbers 18, 52, 15).
  - `1732087-q02` (equiangular hexagon 4, 2, 7, 1) vs `aops-topic-2766239-q07` (different sides).
  - `1729010-q01` (digit sum of 10^1000 - 7982) vs `aops-topic-3164334-q03` (10^2016 - 2016).
- Other drafts of this run: dup.py flagged only lookalikes (b234 1712750 is 2^200 mod 13, not 2^2000). No lines in `xnotes.md` are addressed to batch 231, and none were added.
- `deduplication_registry.json` is cumulative; batches 76-80 are still missing from it.

## Screening

Statuses: included 58, partial 0, excluded 29, duplicate 13.

Excluded as not usable (other than non-maths posts):
- Problem only in a missing image, video or link:
  - 613694 (2011 AMC 8 #19: rectangles in a figure)
  - 1732690 (square with three vertex-to-midpoint segments; which segments are drawn is not stated)
  - 1730333 (RECTANGLE letter grid)
  - 1728493 (AB + BC + AC > 2 OC; configuration missing)
  - 1729813 (1995 AJHSME #25, not stated)
  - 1728120 (MATHCOUNTS Handbook #187, link only)
- No problem text: 1731672.
- Notation, terminology or calculator-use questions with nothing to pose:
  - 1690773 (2^n/4 = 2^(n-2))
  - 1730004 (meaning of y mod m)
  - 1726279 (is it a polynomial; "leading term" of a two-variable polynomial)
  - 1728227 (logarithms on a calculator)
- Open-ended or ill-defined:
  - 1732223 (rearrange the symbols to make pi; the rules are not well defined)
  - 1730955 (fewest-2s game)
  - 1730437 (asks for middle-school proofs of the isoperimetric theorems for polygons)

The other 15 excluded topics were non-mathematical: worksheet and advice requests, AMC 8 registration, AlphaStar questions, polls, a prime-number project, what to bring to contests, Pascal-triangle facts, the twin prime conjecture, MATHCOUNTS answer formatting, a digits-of-pi game, a spam post, a ZIML group, WWPMT tips, AMC 10 preparation and "should AoPS make an app".

## Editorial changes

**Wrong posted answers, ill-posed problems and repairs:**
- `1733566-q01` (1000 cups): the claim that one position in line has the highest expected payoff is false; every position has expected payoff 1 dollar. The record asks to show this. Using the post's extension, it adds a fee paid only by those who play; with that fee, the last position is best (1 - c/1000).
- `1734624-q02`: the poster's 14 diagonals is the count from one vertex; the answer is 119.
- `1147571-q01`: "ordered pairs" became ordered quadruples. The poster's 969 = C(19,3) is wrong; the answer is C(16,3) = 560.
- `1657695-q05` (MTE #5): the stated inverse g of f does not exist, since f = (x-3)(2x-9)^2 is not one-to-one. The condition g(0) = 3 was replaced by its content f(3) = 0; answer 15/2.
- `1657695-q06` (MTE #6): p(x) was determined only up to sign (23 or -23). The condition p(0) < 0 was added; answer 23.
- `1657695-q11` (MTE #11): the roots have sum -20, so they cannot be the edges of a prism. The record asks for the formal ratio 1009/18 and for a proof that the prism is impossible.
- `1657695-q10` (MTE #10): integer side lengths are assumed; otherwise there are infinitely many pairs. Answer 12.
- `1732087-q01` (two circles): the post asks for "the" radius, but two configurations fit, with the centres on opposite sides of the chord or on the same side. The record asks for all values and gives both, with a sketch of each case.
- `1732887-q01` (Mathalon 2, 9, 28, ...): the record proves the poster's point that the 12th term is not determined (a family of cubics through the data). It keeps n^3 + 1 = 1729 as the intended rule.
- `1727878-q01`: the poster suspected the problem was wrong because mass points gave EF:FD = 15:4. The problem is consistent: G is defined by F, so those masses do not apply. The answer is BF:FG = 17:7, and the error is explained.
- `1728999-q01`: 12(Y - 2018) = Y has no integer solution. The record asks for the year in which the count of completed months reaches the year number (start at the beginning of 2018); answer 2201.
- `1731212-q01`: x and y are assumed rational (otherwise x + y + xy is not determined); answer -1/4.
- `1111533-q01`: "solve for x" was posed with no equation and a broken \frac. It is now "simplify the continued fraction"; the answer is x - 1 (x not 1 or 2).

**Interpretations made explicit:**
- 1734077-q01: the figure was rebuilt from the poster's description (a plus of five squares, each cut by both diagonals); 56 triangles, confirmed by enumeration.
- 1728894-q01: the figure was rebuilt from the text, with L and M read as the points of tangency; answer 4 sqrt6.
- 1734032-q01: the condition is first met in 2019, after 1 year.
- 526580-q01: plays of 2, 3, 6 and 7 points, counted as unordered combinations per team; 18 x 10 = 180.
- 1701662-q01: "share with his two friends" means among three people; answer 1/3.
- 1657695-q07: three independent uniform choices from {-1, 0, 1}; answer 10/27.
- 1657695-q13: G(n) is written as G_n, and roots are counted with multiplicity; answer 6144.
- 1729780-q01: n is a positive integer and [x] is the nearest integer; 56 (57 if 0 counted).
- 1730054-q01: population standard deviation; answer 64, as in the key.
- 1729495-q01: "arrange 0-9 in groups of seven" covers both ordered arrangements (604800) and groups (120).
- 1732752-q01: "golden heptagon" is read as a regular heptagon.
- 1732639-q01: "difference by" is read as "divide by".

**Posts turned into questions:**
- 1734398-q01: area of a degenerate triangle from Heron's formula (0).
- 1732030-q01: find the error in S = 1 + 2 + 4 + ... = -1.
- 1627894-q01: the one-stroke puzzle became the identity x + 1 = 1/x for x = (sqrt5 - 1)/2.
- 1732647-q01: the 17 rule plus a general rule for any m coprime to 10.
- 1730101-q01: an example of a tilted parabola and a proof that every parabola has B^2 = 4AC.
- 1731288-q01: 2 scoops from 5 flavours with repetition (15), explaining why 5^2 counts ordered pairs.
- 1728427-q01: a^2 + ab + b^2 does not factor over the reals; its factorisation over C.
- 1731866-q01: the error in 3(n - 5) = 3n - 5.

## Diagrams

There are 15 Asymptote diagrams in the exported records: 13 in solutions and 2 in questions (1734077-q01, 1728894-q01). Each has an SVG preview and alt text. Every geometry-tagged record has a solution sketch; 1732087-q01 has one sketch for each of its two configurations. Geometry tags were not used for 1657695-q11 (the prism does not exist) or 1727717-q05 (cube rotations counted combinatorially), so these records have no sketch.

Fixes after viewing the contact sheets:
- 1734624-q01: the 8 and 17 labels were moved off the dashed straight path.
- 1733869-q01: the red face diagonals were moved to the right face and the oblique depth increased, because a blue space diagonal nearly overlapped a red face diagonal.
- 1732087-q01: the b label was moved off a circle, the a labels were moved off the arcs, P and Q were moved clear of the crossing arcs, and the figure was enlarged.
- 1657695-q06: the (1,2) label was moved off the y-axis.
- 1727878-q01: the F label was moved off segment ED.
- 1734624-q02: a sketch of the 14 diagonals from one vertex of a 17-gon was added, because the record carries polygon tags.

## Validation

- `chk.py`: `chk OK` (3 check files).
- `precheck.py 231`: `PRECHECK OK`. 79 records exported, 17 aliases, 100 topics accounted for, 15 diagrams.
- `finalize.py 231` (pre-check mode): 79 question records, 15 previews (0 missing, all compiled), 253 ZIP members, `checks_passed: true`. The review list is empty: no slash hits and no geometry record without a sketch.
- `pdfcheck.py`: `records=79 asy_files=15 asy_failures=0 pages=79`, `warnings: 0`, no colour leak, `OK`.
