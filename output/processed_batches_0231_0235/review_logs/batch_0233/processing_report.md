# AoPS batch 233 processing report

**73 question records** prepared from the 100 topics screened in batch 233.

Claude did all of the work, with no DeepSeek or other external model. It screened every topic, solved each problem in full before choosing tags and a difficulty, checked every computable answer with exact or brute-force code (`chk_p233_01.py` to `chk_p233_03.py`), and looked at every diagram on contact sheets. The builders are `p233_01.py` to `p233_03.py`.

## IDs and duplicates

- IDs have the form `aops-topic-<AoPS topic id>-q<original part number>`. Multi-problem posts:
  - 1721820 (Modular Arithmetic Bonanza, round 1, problems 1-4): q01-q04.
  - 1720756 (two problems): only problem 2 is used, so q02.
  - 1640117 (parts a and b): q01, q02.
  - 1717359 (KEP round 8, problems 1-6): q01-q05; problem 6 is dropped. q01, q02 and q04 are aliases.
  - 1710109 (KEP round 7, problems 1-6): q01, q02, q03, q05; problems 4 and 6 are dropped.
  - 1603119 (counting marathon): only P1 is in the post, so q01.
- 9 repeats are aliased instead of exported:
  - `aops-topic-1722254-q01` -> `aops-topic-2796248-q12` (2015 MMC #12, integer roots with b+c=298, answer 10).
  - `aops-topic-1720977-q01` -> `aops-topic-2796294-q12` (jars A and B, 321/530). Our record also asks for the error in the poster's attempt. That is a minor addition to the same task.
  - `aops-topic-1720979-q01` -> `aops-topic-2796272-q11` (three integers from 1-12, sum divisible by 3, 19/55).
  - `aops-topic-1720901-q01` -> `aops-topic-2638705-q47` (row sums of Pascal's triangle are 2^n). The earlier record asks for two proofs of the same identity, so ours is contained in it.
  - `aops-topic-1719786-q01` -> `aops-topic-1778662-q01` (2018 MATHCOUNTS School Sprint #25, fewer than eight coins, 69).
  - `aops-topic-1719597-q01` -> `aops-topic-2796272-q08` (product of digits even, 67/72).
  - `aops-topic-1717359-q01` -> `aops-topic-1724486-q03` (b232 draft: the same KEP trisector problem, with the same repair: AE = 9 dropped, AC = 5 sqrt5/2).
  - `aops-topic-1717359-q02` -> `aops-topic-1723304-q01` (b232 draft: minimum of sqrt(2x^2-3)+sqrt(3x+5), 16).
  - `aops-topic-1717359-q04` -> `aops-topic-1724486-q01` (b232 draft: asymptotes x=-4 and y=2x-2, 13, with the same gcd repair).
- Duplicate only: 1722254, 1720977, 1720979, 1720901, 1719786, 1719597.
- `xnotes.md`: the three lines addressed to b233 (from b232) are acted on above. No b233 record was flagged against a later batch.
- Near misses kept (same idea, different data or target):
  - `1716960-q01` (1980 AHSME #21, the ratio [BDF]:[FDCE]) vs `aops-topic-3312652-q01`. Same configuration, but the earlier record asks for [ABD] given [DCEF] = 60.
  - `1717720-q01` (three dice, sum prime or even) vs `aops-topic-3156797-q105` (sum prime).
  - `1715535-q01` vs other right-triangle altitude problems, which have different data.
- `deduplication_registry.json` is cumulative. Batches 76-80 are still missing from the registry.

## Screening

Statuses: included 62, partial 3, excluded 29, duplicate 6.

Partial:
- 1720756: problem 1 is dropped. It asks for an ellipse with foci (0,0) and (-8,8) through (3,4), "ratio of the y-intercepts m/n, |m+n| = 8". With these data the y-intercepts are about -3.057 and 8.676, whose ratio is irrational. The data or the key are wrong and cannot be recovered.
- 1717359: problem 6 is dropped. Its removal conditions ("n (mod 3)", "2n (mod 7)", "3n (mod 11)") are garbled.
- 1710109: two problems are dropped.
  - Problem 4 (circumradius of a regular 5-simplex) is five-dimensional geometry outside the bank's scope, and no sketch is possible.
  - Problem 6 (donuts) only works by assuming an unstated Poisson model.

Excluded as not usable (beyond the 15 non-maths posts):
- No problem text, or the problem only in a missing image, link or screenshot: 1721631, 1720678 (2018 MATHCOUNTS School Team #9 in a PDF link), 1720445, 1720332 (economics), 1717997 (1993 AHSME #13 link; the poster solved it), 1718128 (2016 AMC 10A #11 shaded region), 1718146 (screenshots), 1363136 (MATHCOUNTS State surface area), 1717277 (dartboard values).
- Ill-posed:
  - 1721514: a quintic with no closed-form roots.
  - 1717989: the "expected value" of (2+3x)/(4-7x) on [0,10] does not exist, because there is a pole at x = 4/7 and no distribution is given.
  - 1717642: "next number" puzzles with no rule.
  - 1716396: an average rate of change with no interval.
- 1716792 (largest square in a 5 by 5 square with 1 by 1 corners cut off): a numerical search gives side sqrt 15 (a tilted square whose edges pass through the reflex corners). A sound self-contained proof that this is optimal would need a long case analysis, so the topic is excluded instead of being given an unproved answer.

The 15 non-mathematical posts were:
- requests for programmes, books, LaTeX help, polls and scores
- the meaning of "integer", Euclid's axioms and "choice function"
- spam and an ABMC advert
- the PTA complaint and the Mock AMC 8 sign-up

## Editorial changes

**Wrong posted answers, wrong reasoning and inconsistent data:**
- `1717359-q01` (alias): AE = 9 contradicts CD = 5 and DE = 1, which force AE = sqrt5/2. AE = 9 and the irrelevant points F, G are dropped, and the order B, E, D, C is stated. The answer is AC = 5 sqrt5/2 (same repair as b232).
- `1715535-q01`: the data AB = 3, CD = sqrt2, AD = BC are inconsistent: AD = BC and AB = 3 force CD^2 = 9 sqrt5 - 18. The record drops CD = sqrt2, takes the right angle at C, and gives AC = 3 sqrt((sqrt5 - 1)/2). The solution explains the inconsistency.
- `1719574-q01` (2017 AMC 10A #17): the poster's "fix" (PQ = 10, answer 5 sqrt2) is wrong because PQ = 10 is rational. The record asks for the answer (D) 7 and for the error.
- `1720835-q01`: the poster's image point C = (0,-6) is wrong; C = (-6,0). The perimeter is 16, as keyed.
- `1720977-q01` (alias): the poster's case probabilities are wrong (denominators 100 and 103). The key 321/530 is correct.
- `1710109-q03`: the "minimum and maximum" of AE are not attained, since the posted solution uses 3 <= BC <= 15 but these are degenerate triangles. The record asks for the greatest lower bound and least upper bound, so the answer stays 47.
- `1717359-q04` (alias): a, b, d, e were determined only up to a common factor; gcd 1 is required.

**Interpretations made explicit:**
- 1722465: 15 dishes = 5 + 4 + 3 + 2 + 1 ice cream; Coke is a drink and Mentos a snack (answer 6991).
- 1722254 (alias): "(u-v)(u+v) = x^2+bx+c" read as (x-u)(x-v).
- 1721820-q04: Mock AMC 8 scores are integers 0-25 (one point per question).
- 1721580: "a multiple of 2,3,5" is ambiguous; both readings are asked (37/50 and 3/100).
- 1640117-q02: "with 0,1,...,6" is asked both with repetition (168) and without (105).
- 1716595: the man stands between the tree and the common tip of the two shadows (tree 9 m).
- 1719242: 0 < a < 180 degrees, and the claim is read as: one of the angles between l and l' is a.
- 1717359-q02: "simplest form" is made precise (c squarefree, b/d in lowest terms).
- 1717412: AB != CD is stated; for a rhombus, ac = bd.

**Posts turned into questions:**
- 1721702 (maximum product of positive reals with sum x): the general answer (x/k)^k with k near x/e, plus the case x = 10 (625/16).
- 1721676: are f(f(x)) and g(g(x)) the same function? No: the domains differ.
- 1721671 (1995 AIME #5, b = 51): also asks why the other product is exactly 13 - i.
- 1721792: finish the student's solution of 2/(x+1) > -1.
- 1720781: Ramsey number R(4,4) = 18, with the Paley colouring of 17 points for the lower bound.
- 1717974: proof that the Euclidean algorithm terminates and outputs the gcd.

## Diagrams

There are 21 Asymptote diagrams in the exported records: 19 in solutions and 2 in questions (1721378-q01 magic triangle, 1707844-q01 pentagon diagonals). Each has an SVG preview and alt text. Every geometry-tagged record has a solution sketch, drawn from computed coordinates. The flat isosceles triangle of 1717359-q01 (now an alias) is drawn to scale with height 1 on base 11.

Fixes after viewing the contact sheets:
- 1722305-q01: the X label was moved off diagonal BD.
- 1720835-q01: the x-axis label was moved off the A(0,0) label.
- 1720756-q02: the bisector now starts at (0,4), so it no longer runs through the (0,4) label. The (4,4) label was moved off the square's edge and the (3,1) label off the dashed line.
- 1716595-q01: the "tree", "man" and "tip" words collided with the ray and the 1.2 label. They were replaced by the tip label X.
- 1717404-q01: the equal-angle arcs were enlarged and given matching ticks.
- 1717359-q05: the D label was moved off the circle and segment AO.
- 1710109-q03: the side labels 6 and 9 were removed, because they read as sub-lengths. The P label was moved off line BE.
- 1715899-q01: the S label was moved off line CE.
- 1716607-q01: the coordinate labels were shortened to A, B, E, so they no longer cross the axes, and the equation label was moved off the dotted line.
- 1716960-q01: the 72 degree label was moved off BE, and the shading was lightened.

## Validation

- `chk.py`: `chk OK` (3 check files; brute force, exact fractions or coordinates for every answer). Two exhaustive checks were run: no monochromatic K4 in the Paley colouring of 17 points, and all 2^15 colourings of K6.
- `precheck.py 233`: `PRECHECK OK`. 73 records exported, 9 aliases, 100 topics accounted for, 21 diagrams.
- `finalize.py 233` (pre-check mode): 73 question records, 21 previews (0 missing, all compiled), 241 ZIP members, `checks_passed: true`. The slash fractions found in maths were rewritten with `\dfrac`. The only remaining review line is the text "red/blue".
- `pdfcheck.py`: `records=73 asy_files=21 asy_failures=0 pages=73`, `warnings: 0`, no figure whose last label colour is not black, `OK`.
