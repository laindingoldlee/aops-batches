# AoPS batch 226 processing report

**80 question records** prepared from the 100 topics screened in batch 226.

Claude did all of the work for this batch, with no DeepSeek or other external model. It screened every topic and solved each problem in full before choosing tags and a difficulty. Every computable answer was checked with exact or brute-force code (`chk_p226_01.py` to `chk_p226_03.py`), and every diagram was checked by eye on contact sheets. The builders are `p226_01.py` to `p226_03.py`.

## IDs and duplicates

- IDs have the form `aops-topic-<AoPS topic id>-q<original part number>`. Multi-problem posts:
  - 1760257 (AIME marathon P1-P3: AIME 1983 #3, 1983 #1, 1987 #5): q01-q03.
  - 1761574 (New Year's Problems II, problems 1-5): q01-q05.
  - 1761505 (three 2019 problems): q01 (aliased), q02, q03.
  - 1759713 (MATHCOUNTS handbook Warm-Up 12, problems 1-5): q01-q05.
  - 1759128 (local contest, problems 1-5): q01-q05.
  - 1758725 (Xmas problems 1-6, chained answers substituted): q01-q06.
  - 1759676 (handbook #136 and #137): q136, q137, keeping the handbook numbers.
  - 1759881 (competition P1-P3): only q03 is used.
  - Marathon threads 1761985, 1761969, 1759738, 1705149, 1760139: only P1 is in the post, so q01.
- 8 repeats are aliased instead of exported:
  - `aops-topic-1761505-q01` -> `aops-topic-3165911-q04` (units digit of 2019^2019, 9)
  - `aops-topic-1761688-q01` -> `aops-topic-2025281-q01` (2012 MATHCOUNTS National Target #6, 560 interior lattice points, n = 162)
  - `aops-topic-1761528-q01` -> `aops-topic-2335774-q03` (angle bisectors of a triangle are concurrent)
  - `aops-topic-1761162-q01` -> `aops-topic-2424034-q01` (7^2010 mod 100 = 49; the earlier record asks for the last two digits)
  - `aops-topic-1760928-q01` -> `aops-topic-2013012-q01` (2011 MATHCOUNTS National Sprint #19, 3/5)
  - `aops-topic-1760552-q01` -> `aops-topic-1850375-q01` (2^(16^x) = 16^(2^x), x = 2/3)
  - `aops-topic-1759297-q01` -> `aops-topic-3501674-q01` (minimum of 8x^3+36x+54/x+27/x^3, 48 sqrt 6)
  - `aops-topic-1759180-q01` -> `aops-topic-1962685-q01` (2018 MATHCOUNTS School Target #5, the dog-park logic puzzle, 252)
- Duplicate only: 1761688, 1761528, 1761162, 1760928, 1760552, 1759297, 1759180.
- Cross-batch: `1759713-q03` (five-term AP, mean 18, mean of squares 374, answer 28) repeats b227 draft `1757353-q01`. b227 is later, so this record stays exported and a line was added to `work/xnotes.md` saying b227 should alias to b226. dup.py also shows the b221 draft `1784461-q01` equal to the prior record that 1760552 is aliased to, and the b221 draft `1695399-q06` equal to the prior record behind 1761688. Those are b221's own matches with prior records. No line in xnotes.md is addressed to batch 226.
- Near misses kept (same idea, different numbers or target):
  - `1762011-q01` (four quarter circles in a unit square) vs `aops-topic-1984367-q01` (side 12).
  - `1759282-q01` (odd number of factors up to 2000, 44) vs `aops-topic-2266939-q01` (below 1000) and `aops-topic-2022850-q01` (first 2018).
  - `1761513-q01` (x^y = y^(x-y)) vs `aops-topic-2491990-q01` (x^y = y^x).
  - `1760131-q01` (combinatorial proof of the sum of cubes) vs other combinatorial-proof records (`2307270`, `1975067`, `2582295`), which are different identities.
- `deduplication_registry.json` is cumulative; batches 76-80 are still missing from the registry.

## Screening

Statuses: included 58, partial 1, excluded 34, duplicate 7.

Partial:
- 1759881: P1 (trapezoid perimeter) and P2 (shaded midpoint triangles) depend on missing figures; only P3 (cookie recipes) is used.

Excluded as not usable (beyond non-maths posts):
- No problem text, or the problem is only in a missing image, attachment or link:
  - 1762472 (two Sprint questions not stated)
  - 1760771 (2012 State Sprint #25 missing)
  - 1761103 (attached Introduction to Number Theory problem)
  - 1760101 (Kangaroo problem only in a PDF link)
  - 1759335 (redacted)
  - 1760862 (six squares in an 11 by 13 rectangle)
  - 1760519 (semicircles of radius 6 and 4 and a circle of radius r; the configuration is not determined by the text)
  - 1759511 (circle with tangent points and 3EC = 2BC)
  - 1758950 (UKMT IMC 2005 Q25, shaded region)
- Ill-posed or not a problem:
  - 1762188 (garbled AMC 10 guessing question whose choices fit no reading)
  - 1762182 (writing a base-10 number "algebraically" in base 3)
  - 1761673 (general factoring method)
  - 1760965 (definition of "equally likely")
  - 1759329 (is 1/0 = 1/0?)
  - 1760826 ("get i" marathon with no stated rules)

The other 19 excluded topics were non-mathematical: MATHCOUNTS cutoffs, difficulty and trainer questions, book, Alcumus, Oplet, FTW and resource advice, olympiad prep, the AMC 8 statistics post and a test-difficulty rating thread.

## Editorial changes

**Wrong posted data or answers, ill-posed problems and repairs:**
- `aops-topic-1762096-q01`: a "3-13-16 triangle of area 40" cannot exist, since 3 + 13 = 16. The record asks why, and then uses the genuine triangle sqrt(41)-13-16, which has area 40 and altitude 5 to the longest side (the intended answer).
- `aops-topic-1761574-q01`: the summand C(n,3) does not depend on i. It is corrected to C(i,3), giving n = 16; the literal reading would give 12, and both are mentioned.
- `aops-topic-1760131-q01`: the posted identity C(n,2)^2 = 1^3+...+n^3 is false. It is corrected to C(n+1,2)^2, and the record asks for a combinatorial proof (counting pairs of 2-subsets by their largest element).
- `aops-topic-1759128-q05`: asks for the second-lap speed that makes the average 2x. No finite speed works, and the solution shows this.
- `aops-topic-1758550-q01`: "difference between the square and the cube" has no positive solution as square minus cube, so the record uses cube minus square (the golden ratio).
- `aops-topic-1759193-q01`: the poster's 130 is not the maximum. The stated 142 is proved by bounding the Fridays in each month and confirmed on real calendars.
- `aops-topic-1754925-q01`: the poster's cubic x^3+35x^2-50x+24 has no rational roots, so the record asks to show that it cannot be factored over the integers, and to expand (x+2)(x-3)(x+5)(x+6).

**Interpretations made explicit:**
- 1762370-q01: "the other digits ... contained at least once" read as each of 1-9 appearing. The answer is 1022345678 followed by 220 nines.
- 1762011-q01: the missing figure is the standard quarter circles of radius 1 centred at the corners (confirmed by the text).
- 1761577-q01: ordered pairs (A, B).
- 1761611-q01: you, Billy and the wall lie on one perpendicular line.
- 1761574-q03: "sit together" read as adjacent chairs; "three chairs away" as the post's example says; the adults' clockwise order is a cyclic order.
- 1760139-q01: seeds of a kind are identical and pots may be empty (answer 512).
- 1760928 (aliased): sets rather than ordered lists.
- 1760574-q01: the cars are distinct, with sizes 3, 3 and 4.
- 1759713-q04: "expected number" read as the capture-recapture estimate.
- 1759128-q01: the water surface is 2 inches above the clarinet's lowest line, and the clarinet is a solid cylinder.
- 1758725-q04 to q06: the chained answers are substituted, so each record stands alone. q04 counts all days including days 1 and 2 (16). q06 asks for the N < 1000 with the most divisors (840).
- 1761483-q01: the conditions m, n nonzero, m^2 not n^2 and x nonzero are stated.
- 1759213-q01: "x/1-x^3 - x/1+x+x^2" read as x/(1-x^3) - x/(1+x+x^2).

**Posts turned into questions:**
- 1762377-q01: "write 2019^2019 as a sum of squares" became: use the fewest squares, three, since two are impossible because 2019^2019 is 3 mod 4.
- 1762194-q01: making 243, 248 and 371 from six listed numbers. All three are possible, and each representation is unique.
- 1761309-q01: all integer solutions of 17m + 3n = 1.
- 1761719-q01: proof of the gcd + 1 formula for lattice points on a segment, with an example.
- 1761230-q01: find the error in the "1/8" argument (the answer is 5/16).
- 1761117-q01: the exponent of 5 in 201! (49), and why the extra Legendre terms are needed.
- 1760770-q01: the statement of the Chinese remainder theorem, plus Sunzi's example (23).
- 1760504-q01: "how many equilateral triangles on a parabola": infinitely many, proved by rotating the parabola 60 degrees about any of its points and using the intermediate value theorem.
- 1762175-q01: the example from an advice post (x^2 - 6 = 1/4).

## Diagrams

The exported records have 20 Asymptote diagrams: 19 in solutions and 1 in a question (1762011-q01). Each has an SVG preview and alt text. Every geometry-tagged record has a solution sketch. Geometry tags were removed from 1760858-q01 (lattice-point parity, now Probability, Parity and Matrices and determinants) and from 1759128-q03 (radian conversion), so they need no sketch.

Fixes after viewing the contact sheets:
- 1762570-q01: the equal half-angles at P are marked with single ticked arcs (the double arcs merged into one), and the Q, Q0 and Q1 labels no longer crowd.
- 1761304-q01: the x-axis was extended so its label no longer collides with C(8,0), and the P and Q labels were moved off the lines.
- 1761688 (now aliased): the "not to scale" text, which crossed the hypotenuse, was moved into the solution text.
- 1761528 (now aliased): the I label was moved off the dashed perpendicular.
- 1761197-q01: the fill is drawn first so the front arc of the top ellipse stays visible, and the axis label is clear of the ellipse.
- 1759713-q05: the 10 label was moved inside the triangle, away from the circle.
- 1759128-q01: the crowded 120-degree mark was removed; the depth 2 is shown with a double arrow outside the circle.
- 1759331-q01: the line label was moved away from the y-axis label.

## Validation

- `chk.py`: `chk OK` (3 check files).
- `precheck.py 226`: `PRECHECK OK`. 80 records exported, 8 aliases, 100 topics accounted for, 20 diagrams.
- `finalize.py 226` (pre-check mode): 80 question records, 20 previews (0 missing, all compiled), 261 ZIP members, `checks_passed: true`. The slash review list is empty and there are no "GEOMETRY WITHOUT SKETCH" lines.
- `pdfcheck.py`: `records=80 asy_files=20 asy_failures=0 pages=80`, `warnings: 0`, 0 figures whose last label colour is not black, `OK`.
