# AoPS batch 234 processing report

**78 question records** prepared from the 100 topics screened in batch 234.

Claude did all of the work for this batch, with no DeepSeek or other external model. It screened every topic and solved each problem in full before choosing tags and a difficulty. Every computable answer was checked with exact or brute-force code (`chk_p234_01.py` to `chk_p234_03.py`), and every diagram was checked by eye on contact sheets. The builders are `p234_01.py` to `p234_03.py`.

## IDs and duplicates

- IDs have the form `aops-topic-<AoPS topic id>-q<original part number>`. Multi-problem posts:
  - 1715695 (three MATHCOUNTS questions: course schedules, n + 18/n, 4-cubes in a 10-box): q01-q03.
  - 1713845 (three variation problems): q01-q03.
  - 1715264 (three problems with posted answers 2, 5, 84, all correct): q01-q03.
  - 1711916 (five practice problems: double cone, power of 2, coin flips, consecutive sums, parallel chords): q01-q05.
  - 1715432 (12 students, parts (i)-(iii)) and 1715917 (FBH parts a, b) are each kept as one record with all of their parts.
  - Marathon 1716692: only P1 is in the post, so q01.
- 6 repeats are aliased instead of exported:
  - `aops-topic-1714665-q01` -> `aops-topic-2556748-q01` (8 people at a square table, rotations identified, 10080)
  - `aops-topic-1713999-q01` -> `aops-topic-1877656-q01` (glide reflection of the 3-4-5 triangle, ratio 5/11; same MATHCOUNTS wording)
  - `aops-topic-1712753-q01` -> `aops-topic-2796071-q14` (11-12-13 triangle, AK:KN = 3:1)
  - `aops-topic-1714043-q01` -> `aops-topic-2788839-q03` (mutilated chessboard; the old record asks "can it be covered?", same task)
  - `aops-topic-1715047-q01` -> `aops-topic-2787008-q03` (FBH 2016 Grade 7 #3: the remainder of a prime on division by 30 is not composite; the old record says "is 1 or a prime")
  - `aops-topic-1713859-q01` -> `aops-topic-1715130-q01` (repeat inside this batch: the sequence telescoping problem. 1713859 writes the sequence as 1, 1, 4, 8, ..., and that first term breaks the stated rule. The poster reposted it with first term -1 as 1715130, which is the exported copy.)
- Duplicate only: 1714665, 1713999, 1712753, 1714043, 1715047, 1713859.
- Near misses kept (same idea, but different numbers or a different target):
  - `1712750-q01` (2^200 mod 13) vs `aops-topic-2796272-q10` and the b231 draft `1731478-q01` (2^2000 mod 13).
  - `1711204-q01` (zeros at the end of (zeros of 420!)!) vs `aops-topic-1872176-q01` (zeros of 420! only).
  - `1690790-q01` (last three digits of 1^300 ... 5^300) vs `aops-topic-1787633-q01` (last two nonzero digits of 1^100 2^200 ... 5^500).
  - `1715264-q03` ((a+b+c+d)^6) vs `aops-topic-1759128-q04` (a different coefficient pattern, same count 84). Kept because the wording and the expression differ; borderline.
- Cross-batch note: the b232 draft `1725534-q01` is the same glide-reflection problem as the prior record `aops-topic-1877656-q01`. A line was added to `work/xnotes.md`. Nothing in xnotes.md is addressed to batch 234.
- `deduplication_registry.json` is cumulative; batches 76-80 are still missing from the registry.

## Screening

Statuses: included 68, partial 0, excluded 26, duplicate 6.

Excluded as not usable (beyond non-maths posts):
- Open problems or results that rest only on a computer search:
  - 1716731 (infinitely many numbers m^k - m in two ways? An open question)
  - 1716432 (largest non-pandigital power of 2: a conjecture from a search)
  - 1696906 (domino tilings of 6 by 10 "with proof": the count 4213133 needs a transfer-matrix computation)
- The data are only in a missing image, attachment or figure:
  - 1715053 (FBH 2016 Grade 7 #5, table shown as IMAGE)
  - 1714653 (AMC 8 problem with the equal perimeters, figure missing)
  - 203522 (mock MATHCOUNTS in attachments; the post holds only the errata)
- No problem text:
  - 1714324, 1714252, 1712208
  - 1713244 (opening post of a marathon: rules only)

The other 16 excluded topics are non-mathematical:
- class clubs and MATHCOUNTS prep forums (1703916, 1714978, 1715054)
- AMC 8 and MATHCOUNTS advice and resources (1715076, 1715242, 1693908, 1711562, 1711885, 1711539, 1711302)
- "uses of prime factorization" (1714807) and a coordinate-bash poll and resource request (1714470, 1714333)
- a teaching-advice post (1714393)
- a request for 2017 State solutions (1422872)
- a request for angle-bisector problems (1711905)

## Editorial changes

**Wrong posted answers, false claims and ill-posed problems:**
- `1712630-q01` (AB = 23, AC = 10, BC = 25, area of DEF): none of the five posted choices is correct. They are about 15.77, 20.74, 22.31, 32.86 and 35.27. The area is 103 sqrt(3306)/350 (about 16.92), checked exactly. The record is free-response.
- `1713423-q01`: the claim "if a^5 is natural then a is natural" is false (a = 2^(1/5)). The record asks for the counterexample and proves the claim for rational a.
- `1713859` (aliased): the first term 1 of "1, 1, 4, 8, ..." contradicts the rule; the corrected repost 1715130 is used.
- `1715910-q01` (FBH 2015 G7 #4): the condition "at least one of each kind" was added. Without it, (39, 200, 0) also fits. The answer is 39 watermelons, 60 melons and 140 cobs; the second buyer bought 46.
- `1715902-q01` (FBH 2015 G6 #4): the number x is required to be a whole number. Otherwise every digit a works. The answer is a = 1, x = 571.
- `1715033-q01` (FBH 2016 G6 #4): the order of the rays (OA, OC, OD, OB) is stated. The other order would give 60 degrees instead of 28, and the solution mentions this.
- `1715914-q01` (FBH 2015 G8 #2): the condition that a, b, c are pairwise distinct was added, and the constant value -3 is asked for.
- `1715915-q01` (FBH 2015 G8 #3): E and F are taken strictly inside the sides; if E = B the inequality becomes an equality.
- `1713845-q01`: "by what factor does x decrease" (a deliberate trick in the post). The record asks for the factor and the direction: x is multiplied by 4.
- `1710875-q01`: the post's second formula has the typo "x^3 + y^3 = (x - y)(...)"; it is corrected to x^3 - y^3.

**Interpretations made explicit:**
- 1715695-q01: "each of the four days" was read as "on four of the five days" (answer 16).
- 1715695-q02: n + 18/n and (n+18)/n give the same answer, 39.
- 1715695-q03: the cubes are placed with faces parallel to the box, and a proof that at most 8 fit was added (51.2%).
- 1715038-q01 (FBH 2016 G6 #5): "double pages" means sheets carrying pages 2k-1 and 2k, and 4949 is the sum of the torn pages, as written (answer 47). If 4949 were the sum of the remaining pages, the answer would be 3.
- 1715429-q01: the "upper tip" is the apex of one base and the point is the midpoint of the side of length 6 of the other base, in a right prism of height 1 (answer 2 sqrt 23).
- 1715918-q01 (FBH 2015 G8 #5): the three elements are taken to be distinct. A remark shows that 9 cannot be lowered to 8.
- 1715911-q01: "the same 2015 numbers" means the same multiset.
- 1715908-q01: the right angles are at A and C, AB = AD, and BC + CD = 10 (area 25).
- 1712340-q01: the ten integers are distinct (sum 131).
- 1713347-q01 (RMO mock): either intersection point may be chosen on each line, and the proof covers both.
- 1711916-q05: the missing picture is described in the post (all chords on one side of the centre, k in the middle); answer 6 sqrt 6.
- 1711366-q01: "a mile race, opposite directions" was read as a one-mile circular track with a common start; they meet after 1/34 hour = 30/17 min.
- 1714787-q01: both 55, 56 and -56, -55 are given.
- 1648327-q01: the self-similar nested radical is assumed to have a positive value, which gives 1.

**Posts turned into questions:**
- `1716751-q01`: "is there a law against raising both sides to the power 0?" became: find the error (t -> t^0 is not one-to-one).
- `1715644-q01`: estimating pi^7 within 5% mentally. 1000 pi is within 4.0%, and a refinement gives about 3020.
- `1713845-q02`: describing K = m v^2 / 2 in words, with two concrete follow-up questions added.
- `1711919-q01`: "what is the difference between centroids, incenters and orthocenters?" became definitions plus G, I, H for the obtuse triangle A(6,8), B(0,0), C(21,0).
- `1712010-q01`: "how to shift an ellipse" became the translation rule plus completing the square for 4x^2+9y^2-16x+54y+61=0.
- `1710875-q01`: how to discover the sum and difference of cubes formulas (factor theorem).
- `1713813-q01`: the trivial "y = x^2 + 1 >= 0" was kept, with the sharper bound y >= 1.

## Diagrams

There are 19 Asymptote diagrams in the exported records, all in solutions. Each has an SVG preview and alt text. Every geometry-tagged record has a solution sketch. The aliased records have no figures.

Fixes after viewing the contact sheets:
- 1716645-q01: the viewing direction was changed because one hexagon was nearly edge-on and showed as a sliver.
- 1715695-q03: the hidden box edges are now drawn under the block. The box width label moved to the back top edge, where it had collided with a "4".
- 1715429-q01: the depth vector was enlarged so that M' lies outside the front face. M' is now labelled clear of an edge, and the sqrt 91 label was moved off a hidden edge.
- 1711485-q01: the fence arcs at B and C had been drawn the long way round (reversed angles), and the vertex labels were moved off the radii.
- 1712630-q01: the dashed altitude BE, which nearly coincides with side AB, was removed, and the A and E labels were separated.
- 1715264-q01: the 6 and 60% labels were moved off the dashed leg and the x-axis.
- 1715061-q01: the MN length label was moved off the midline EF.
- 1713347-q01: the H, D and A1 labels were moved off the lines FD, FQ and BQ.
- 1712621-q01: an angle arc was added at K, and the 105 degree label was moved off the altitude.
- 1698023-q01: the O label was moved off the dashed radii.
- 1711916-q01: the radius label was shortened to r, which had overlapped the ellipse.
- 1711916-q05: the d label was moved off a dashed radius.
- 1711919-q01: the A, G and I labels were moved off the medians and the altitude.
- 1712010-q01: the 2 and (2,-3) labels were moved off the arrow and the y-axis.
- 1715908-q01: the a labels were moved clear of the tick marks.

## Validation

- `chk.py`: `chk OK` (3 check files).
- `precheck.py 234`: `PRECHECK OK`. It reports 78 records exported, 6 aliases, 100 topics accounted for and 19 diagrams.
- `finalize.py 234` (pre-check mode): 78 question records, 19 previews (0 missing, all compiled), 254 ZIP members, `checks_passed: true`. The slash review list is empty and there are no "GEOMETRY WITHOUT SKETCH" lines.
- `pdfcheck.py`: `records=78 asy_files=19 asy_failures=0 pages=78`, `warnings: 0`, no colour leak, `OK`.
