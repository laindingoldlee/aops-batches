# AoPS batch 222 processing report

**70 question records** prepared from the 100 topics screened in batch 222.

Claude did all of the work in this batch, with no DeepSeek or other external model. It screened every topic, solved each problem in full before choosing tags and a difficulty, checked every computable answer with exact or brute-force code (`chk_p222_01.py` to `chk_p222_03.py`), and checked every diagram by eye on contact sheets. The builders are `p222_01.py` to `p222_03.py`.

## IDs and duplicates

- IDs have the form `aops-topic-<AoPS topic id>-q<original part number>`. Multi-problem posts:
  - 1776535 (factorisation thread, P1 and P2): q01, q02.
  - 1784280 (alternating sum example; Math Is Cool 2018 sum): q01, q02.
  - 1772864 (two Korean problems, P1 and P2): q01, q02.
  - 1782611 (2017 MATHCOUNTS State: Sprint #14, #26, #29, #30 and Target #8): q26, q29, q30 and q08 (Target #8; no clash with the Sprint numbers). #14 is dropped (figure missing). q29, q30 and q08 are aliases; q26 is exported.
  - 1782185 (PROBLEM 1 and PROBLEM 2): q01 (alias), q02 (exported).
  - 1635242 (Q1, Q2): q01, q02.
  - 1780203 (discarded mock problems 1-4): q01-q04.
  - 1781571 keeps the main question and the "challenge" as parts (a) and (b) of one record.
- 7 repeats are aliased instead of exported:
  - `aops-topic-1784100-q01` -> `aops-topic-1945887-q01` (least Heronian triangle area with longest side 17, 36; same wording)
  - `aops-topic-1783256-q01` -> `aops-topic-498536-q05` (even three-digit numbers with h + t = u, 20)
  - `aops-topic-1782611-q29` -> `aops-topic-2493474-q01` (2017 State Sprint #29, AP/BP = 2/3)
  - `aops-topic-1782611-q30` -> `aops-topic-1810662-q01` (2017 State Sprint #30, product 32)
  - `aops-topic-1782611-q08` -> `aops-topic-1812483-q01` (2017 State Target #8, M-shaped curve, 2 sqrt 5 / 5)
  - `aops-topic-1782185-q01` -> `aops-topic-3200999-q04` (sum of y over integer solutions of 1/x + 1/y = 1/7, 42)
  - `aops-topic-1781399-q01` -> `aops-topic-2398382-q01` (2014 Chapter Target #7, cubes with two faces of each of three colours, 6)
- Duplicate only: 1784100, 1783256, 1781399.
- Cross-batch notes (appended to `work/xnotes.md`): b222 `1777432-q01` (cube colourings with 6 colours, 230) repeats the b223 draft `1777424-q01`, so b223 should alias to b222; and the b225 draft `1765675-q01` (Heronian, 17) repeats the prior record `aops-topic-1945887-q01`, to which b222 also aliases. Nothing in xnotes.md was addressed to batch 222.
- Near misses kept (same idea, different numbers or target):
  - `1780934-q01` (20 board members, 6 enemies each, 360 monochromatic triples) vs `aops-topic-1845402-q04` (30 members, 6 friends each).
  - `1782537-q01` (integer right triangle with leg 11, perimeter 132) vs the b224 draft `1770602-q01` (leg 2017).
  - `1746417-q01` (insphere of the regular tetrahedron with edge 1) vs `aops-topic-2285970-q01` (corner tetrahedron with vertices at the unit points).
  - `1772864-q01` (a^3(b-c)^3 + ... ) vs `aops-topic-2652492-q01` (a(b-c)^3 + ...) and `aops-topic-2925646-q01` ((a-b)^3 + ...).
- `deduplication_registry.json` is cumulative; batches 76-80 are still missing.

## Screening

Statuses: included 62, partial 1, excluded 34, duplicate 3.

Partial:
- 1782611: Sprint #14 (Mario's bricks) is dropped because the brick figure is missing; the other four problems are used.

Excluded as not usable (beyond non-maths posts):

- No problem text, or the problem is only in a missing image or attachment:
  - 1780987 (inequality word problem only in an attachment)
  - 1782884 ("Geometry Question:" with nothing else)
  - 1753288 (marathon Problem #1 only in an image)
  - 1423788 (2017 State Sprint #14; the brick layout is only in the figure, and the counts in the post do not determine it)
  - 1780828, 1781505, 1781375 (problems only in attachments or images)
  - 1781026 (no problem text)
  - 1783883 (Desmos graph of x! for negative x; picture missing, no problem posed)
- Ill-posed, or the only solution is a computer search:
  - 1783971 ("GISE 2009" squares landing on circles; no probability model can be recovered)
  - 1777131 (marbles with P(aaaa) = P(bbb) = P(cc) = P(d)): impossible with replacement, and no bag exists without replacement in a search up to several thousand marbles
  - 1779795 (n = product of digits times sum of digits; the full answer 1, 135, 144 needs a computer search)
- Games and rules without a usable problem:
  - 1782494 ("24" marathon; the puzzle 27, 97, 92, 23 cannot be done with + - x / and depends on the game's extra operations)
  - 1603794 ("21 game", rules only)
- 1781953 (what "arbitrary number" means; vocabulary only)

The other 19 excluded topics were non-mathematical:
- AMC 10 polls, score worries, test-day tips, address and CEEB-code questions, the graph-paper complaint, a good-luck post
- MATHCOUNTS study advice, team and individual registration rules, the school-round discussion question
- sign-ups for a preparation forum and a Countdown tournament
- requests for TI-84 programs and for where to find problems

## Editorial changes

**Wrong posted answers, ill-posed problems and repairs:**

- `aops-topic-1782319-q01` (BdMO 2014 Dhaka #4): the posted equation has no solution in positive integers, so "the minimum of pq" does not exist. The record asks for a proof that there are no solutions (via gcd(p^2+1, p(p^6-8)) = 1); checked for p < 5000.
- `aops-topic-1782697-q01` (BdMO 2014 Dhaka #6): the posted radii 18, 6, 9 force CA = 0, so no such triangle exists (the intended answer was presumably 6). The radii were changed to 66, 55, 60, which give an acute 13:9:11 triangle with inradius 40; the solution explains why the original data fail.
- `aops-topic-1781234-q01` (water tanks): "7/3 as much" is impossible, since the first tank always holds less than the second. With 7/8 the answer is choice (a), 5 minutes, so the record uses 7/8.
- `aops-topic-1783346-q01`: "AB parallel to BC" is a typo for AB parallel to CD. The other reading (BC parallel to DA) is impossible; the answer is 66/5.
- `aops-topic-1782694-q01` (BdMO 2014 Dhaka #3): because the post allows the extensions of the sides, there are two squares, with perimeters 6 and 12. The record asks for both.
- `aops-topic-1783551-q01`: there is no maximum degree, and the degree must be even (10, 12, 14, ...).
- `aops-topic-1781575-q01`: the poster's 42 is the number of houses visited on the first two days; the ice-cream answer is 98.
- `aops-topic-1780414-q01` (magic box): the poster's p-1 is wrong. With the last single ball allowed the answer is p+1 (p if it is not allowed).
- `aops-topic-1782185-q02`: the poster's (m-7.5)(n-7.5) = 56.25 is completed with integer factors, (2m-15)(2n-15) = 225, giving m+n = 32.
- `aops-topic-1783275-q01`: n! in the statement is a typo for k!. The composite case is answered with a counterexample, C(4,2) = 6.
- `aops-topic-1780203-q01`: "2m divides 12!" read as 2^m (exponents lost in the post).

**Interpretations made explicit:**
- 1783820-q01 (Harry vs Voldemort): the four numbers are a uniformly random 4-subset of 1 to 9; "spared" means some two of them have a square sum (97/126).
- 1726380-q01 (chocolate bars): "length 6" is the longer side, the cuts go through the whole thickness, and Kyle and RJ keep their full bars (420; the other orientation would give 3780).
- 1784532-q01: the missing figure is determined by the text (five equal strips folded onto each other), 5625.
- 1784477-q01: the temperature scales are linear.
- 1783710-q01: the domain is -2 <= a <= 2; the post's confusion about AM-GM is addressed.
- 1746417-q01: "regular triangular pyramid with base 1" read as the regular tetrahedron with edge 1 (sqrt 6 / 12).
- 1782143-q01: "1/4 higher" means a quarter of A's height higher (99/16 m).
- 1638802-q01: a student may stand and read at once, and every student talks, stands or reads; the minimum is 10 (11 if the two non-talkers must differ).
- 1781688-q01: n real (-4 <= n <= 4).
- 1780203-q04: total surface areas; the ratio 1:5 gives a unique plane.
- 1782031-q01 (2015 National Countdown): the attachment is missing, but the text determines the configuration (40).
- 1783141-q01: the second differences are constant.
- 1781845-q01: the term rule (digits k and k-1 in base k+1) is stated.

**Posts turned into questions:**
- 1783316-q01: "can ax+by=1 have more than one solution" became: describe all solutions (infinitely many).
- 1781263-q01: "what is the pattern" became: state and prove the cube-sum pattern 166...6, 50...0, 33...3.
- 1777432-q01: "why 6!/4!" became the full count (230) with that explanation.
- 1782703-q01: "solve if possible" became a proof that there is no solution.
- 1776535-q02: the side lengths of a rectangle with area x^2 - y^2 ("square" in the post means the rectangle).

## Diagrams

There are 18 Asymptote diagrams in the exported records, all in solutions (1782694-q01 has two, one for each square). Each has an SVG preview and alt text. Every geometry-tagged record has a solution sketch. Records with no geometry tag and no figure include the clock problem 1781693-q01, the cube colourings 1777432-q01 and the geometric probabilities 1779767-q01 and 1780203-q02.

Fixes after viewing the contact sheets:
- 1784164-q01: the diagonal-length labels collided with the sides, so they were moved beside the figure. The altitude was moved to the left of A so that its label is clear.
- 1783549-q01: the legend was too large for the cube, so it was shortened and placed below.
- 1782694-q01: the first version (obtuse triangle) had overlapping H and G labels. It was redrawn with an acute triangle and a dimension arrow for the height, and the A label in figure (ii) was moved off the dashed extensions.
- 1782611-q26: the -2/3 label was moved off the y-axis and away from the (-4,0) label.
- 1780203-q04: the cone's sides are now tangent to the base ellipse, and the 3 and 5 labels were moved off the ellipse and the dotted guide line.
- 1782611-q08 (now an alias): the spline overshoot at the corners of the M curve was removed, and the B and C labels were moved inside the cup.

## Validation

- `chk.py`: `chk OK` (3 check files).
- `precheck.py 222`: `PRECHECK OK`. 70 records exported, 7 aliases, 100 topics accounted for, 18 diagrams.
- `finalize.py 222` (pre-check mode): 70 question records, 18 previews (0 missing, all compiled), 229 ZIP members, `checks_passed: true`. The slash review list is empty and there are no "GEOMETRY WITHOUT SKETCH" lines.
- `pdfcheck.py`: `records=70 asy_files=18 asy_failures=0 pages=70`, `warnings: 0`, no colour leak, `OK`.
