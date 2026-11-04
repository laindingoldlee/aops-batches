# AoPS batch 224 processing report

**81 question records** prepared from the 100 topics screened in batch 224.

Claude did all of the work in this batch, with no DeepSeek or other external model. It screened every topic, solved each problem in full before choosing tags and a difficulty, checked every computable answer with exact or brute-force code (`chk_p224_01.py` to `chk_p224_03.py`), and checked every diagram by eye on contact sheets. The builders are `p224_01.py` to `p224_03.py`.

## IDs and duplicates

- IDs have the form `aops-topic-<AoPS topic id>-q<original part number>`. Multi-problem posts:
  - 1772698 (mini combinatorics collection, P1-P9): q01-q09.
  - 1771651 (translated absolute value graph; right triangle with hypotenuse 3): q01, q02.
  - 1769062 (prism; pyramid): q01, q02.
  - 1766655 (great rhombicuboctahedron; painted cube): q01 exported, q02 aliased.
  - 1766257 (Euler's formula; inradius of the 5-9-12 triangle): q01, q02.
  - 1752262 (game thread, P1-P3): only P3 is usable, kept as q03 (aliased).
  - 1767722 (2015 MATHCOUNTS School Sprint #26 and #30): only #30 is usable, kept as q30.
- 10 repeats are aliased instead of exported:
  - `aops-topic-1771928-q01` -> `aops-topic-2982658-q05` (Alfred and Brendan's token game, 4/7)
  - `aops-topic-1770041-q01` -> `aops-topic-1899710-q01` (Ansel's motorboat, current 5 mph)
  - `aops-topic-1768864-q01` -> `aops-topic-2236295-q01` (angle RQZ = 21 degrees)
  - `aops-topic-1665584-q01` -> `aops-topic-2805123-q05` (ax^2+bx+c with odd coefficients has no rational root)
  - `aops-topic-1767062-q01` -> `aops-topic-2723091-q01` (bread and bologna, 28)
  - `aops-topic-1766655-q02` -> `aops-topic-3579886-q02` (painted 3x3x3 cube rolled, 1/3)
  - `aops-topic-1768268-q01` -> `aops-topic-1605801-q01` (b223 draft of this run: 2018 MATHCOUNTS School Sprint #22, median of {1.7, 1.1, 1.4, 2.1, 2.3, s}, 0.35; requested in xnotes.md)
  - `aops-topic-1752262-q03` -> `aops-topic-2431035-q17` (2/5 gloves, 3/4 hats, minimum 3)
  - `aops-topic-1766818-q01` -> `aops-topic-2181477-q02` (AD^2 = AM AC when angle ADM = angle ACD)
  - `aops-topic-1768394-q01` -> `aops-topic-2529353-q01` (Chinese remainder theorem proof and Sunzi's example, 23; contained in the earlier general-CRT record)
- Duplicate only (all records aliased): 1771928, 1770041, 1768864, 1665584, 1767062, 1768268, 1752262, 1766818, 1768394.
- Near misses kept (same idea, different numbers or target):
  - `1772054-q01` (3x3 lattice triangles with a side sqrt 2, 44) vs `aops-topic-1959402-q01` (side of length 2).
  - `1772698-q01/q02/q03` (Kevin and Xiaomin/Anuj in a row) vs `aops-topic-1795314-q01` (at least two people between them).
  - `1772376-q01` (factorial representation with four digits, prove all 0-119) vs `aops-topic-2349790-q01` (five digits, sum with c = 0).
  - `1770602-q01` (Pythagorean triple with leg 2017) vs b222 draft `1782537-q01` (leg 11, perimeter) and `aops-topic-2256974-q01` (leg 20).
  - `1766257-q01` (56 faces, 114 edges) vs `aops-topic-3186725-q01` (305 faces, 678 edges).
- dup.py found no other repeat against prior releases or the other drafts of this run. The only xnotes.md line addressed to batch 224 (alias 1768268 to b223) has been acted on; batch 224 added no lines to xnotes.md.
- `deduplication_registry.json` is cumulative; batches 76-80 are still missing from the registry.

## Screening

Statuses: included 68, partial 2, excluded 21, duplicate 9.

Partial:
- 1772017: the bonus question (a general formula for the minimum keystrokes for every n) is open-ended and dropped.
- 1767722: problem #26 (congruent right triangles and three squares "in the figure") needs the missing figure and is dropped.

(1752262 is also a partial post, P1 and P2 needing missing images, but its only usable problem P3 is a repeat, so the topic counts as a duplicate.)

Excluded as not usable (beyond non-maths posts):
- No problem text, or the problem is only in a missing attachment, image or book:
  - 1772237 (mock Sprint #21 "attached")
  - 1772141 (problem only in an imgur image)
  - 1767121 (square and rectangle EFGH: positions only in the image)
  - 1768840 (asks about 2018 AMC 10A #24 without stating it)
  - 1768428, 1768445, 1768440 (titles only; problems in missing attachments)
  - 1766884 (AoPS Introduction to Geometry 2.50, figure and statement not given)
- 1672459: Mathleague marathon opening post (rules only).
- 1637888: "200 teachers and 150 students, teachers teaching 10 students" is hopelessly ill-posed.

The other 11 excluded topics were non-mathematical: AMC 10 class advice, factoring resources, calculator display settings, Intro series pacing, MATHCOUNTS team rules, AMC 10 preparation, MATHCOUNTS Trainer difficulty (two posts), MATHCOUNTS preparation, online maths games, and a question about what the "lighthouse theorem" is.

## Editorial changes

**Wrong posted answers, ill-posed problems and repairs:**
- `1769749-q01`: the post calls a, b, c real, but no real numbers satisfy a+b+c = 6, a^2+b^2+c^2 = 26, a^3+b^3+c^3 = 84 (t^3-6t^2+5t+14 has one real root). "Real" is dropped; P = 3799 is unaffected.
- `1769594-q01`: as posted, 3y + cbrt(4x^2) = sixth-root(108x^2y^3) has no solution (by AM-GM the left side always exceeds the right). The factor 2 on the right is restored, making it the AM-GM equality problem; x^2/y^3 = 27/4. The solution explains why the original fails.
- `1766250-q01` (chocolate bars): 18 days earn at least 90 bars, so the posted total 53 is impossible. The record asks to show this, lists the possible totals (multiples of 3 from 90 to 144) and uses 117 (answer: 9 days short).
- `1770315-q01`: "find x = n^2+2n mod 10" given 4 | n^2+2n has no unique answer; the record asks for all possible remainders (0, 4, 8).
- `1768345-q01`: as posted 3^20 > 53^3, so no n exists; the sum is 0, and the solution notes that the sum is 0 for any bounds of this form (pairs n, -n).
- `1770709-q01`: neither of the poster's candidates 6/95 and 12/95 is correct; the probability that both chosen numbers are multiples of 5 is 3/95.
- `1755096-q01`: the poster's 3b - 4 is wrong; Hannah picked 3b + 28.
- `1767069-q01`: the poster's 28 sqrt 22 / 3 treats the slant height 6 as a lateral edge; with slant height as the face height the volume is 28 sqrt 29 / 3. The record defines slant height.
- `1760794-q01`: the poster intersected the two cases of sqrt(5-2x) > x-1 instead of taking their union; the answer key's x < 2 is right. The record asks for the solution and the error.
- `1766118-q01`: the poster's 256 subsets is correct; the record adds proper subsets (255), the likely source of the confusion.
- `1772698-q06` (volcano): the joke post does not say how the 998 people are chosen; the record fixes the Monty Hall reading (a guard who knows spares the volcano-proof person), answer 999/1000, and notes that random selection gives 1/2.
- `1771791-q01` (ant on a frustum): the straight unrolled segment (3 sqrt 7) crosses the top base, which is forbidden; the shortest path is tangent plus rim arc, 3 sqrt 3 + pi.

**Interpretations made explicit:**
- 1772214-q01 (cheating shopkeeper): "cheats 10% while buying and selling" has two common readings; the record states the reading (receives 10% more when buying, charges for 10% more when selling), answer 21%, and gives 22 2/9% for the other.
- 1772698-q07/q09: "odd and even digits" means letters in odd and even positions; "contains bash" means four consecutive letters.
- 1772385-q01, 1769328-q01, 1769179-q01: the variables are real.
- 1771773-q01: the move probabilities apply at positions 1 to 4.
- 1770185-q01: "height of the pyramid" read as the height of the top above the table, (2 + sqrt 2) r; the height r sqrt 2 of the pyramid of centres is also given.
- 1771889-q01: players distinguishable, order within a hand irrelevant.
- 1771651-q01: the post's f'(x) is the translated graph, not a derivative.
- 1770283-q01: the eagle flies straight and both start at the same moment.
- 1772188-q01: each letter of ELECTRICITY used at most as often as it occurs.
- 1768599-q01: the tower is a^(b^c); 1767629-q01: 3^(3^(3^3)).
- 1766801-q01: AC is not equal to BD (otherwise the ratio is 0/0).
- 1766918-q01: "MATH can be found in one pile" means all four letters in the same pile.
- 1764346-q01: "x/y" is the poster's notation for "x divides y".
- 1769062-q01: the volume unit in^2 corrected to cubic inches.
- 1771314-q01: the usual map-colouring condition (regions sharing a boundary segment); the multiple-choice question also asks for a proof.

**Posts turned into questions:**
- 1771314-q01 (torus): "fewest colours" became a proof that 7 colours suffice (Euler's formula for the torus, average degree at most 6) and are needed (the seven-hexagon map).
- 1768109-q01: "the altitude of an orthodiagonal right trapezoid" became a proof that it equals sqrt(ab).
- 1766580-q01: "how many lattice points are in the triangle" became the boundary-gcd formula, the shoelace area and Pick's theorem, with a worked example (7 interior points).
- 1767337-q01: the four-bugs question also asks to explain the radial argument of the posted solution.
- 1772376-q01: the factorial-representation claim became find N = 119 and prove every 0 to 119 is representable (uniquely).
- 1767081-q01, 1771980-q01: proofs as posed.

**Checks of known contest answers:** 2017 MATHCOUNTS National Countdown #24 gives 600 (the poster's key); AIME 1988 #10 gives 840; MATHCOUNTS Handbook and Math Is Cool items agree with brute force.

## Diagrams

There are 23 Asymptote diagrams in the exported records: 22 in solutions and 1 in a question (1771791-q01, the frustum, redrawn from the text). Each has an SVG preview and alt text. Every geometry-tagged record has a solution sketch. No geometry tags are used for 1770602-q01 (Pythagorean triple, number theory only) or the counting and probability records.

Fixes after viewing the contact sheets:
- 1772054-q01: the colouring of the sqrt 2 segments was corrected (long diagonals blue, short ones red) and the figure enlarged.
- 1771914-q01: the centre label shortened to C so it no longer runs into the hexagon's side.
- 1771791-q01: the frustum's sides were redrawn as true common tangents of the two rim ellipses (removing stray dash ends), the top radius label moved off the rim, and the T label moved off the red arc.
- 1770185-q01: labels were taken out of the crowded cross-section and put on a separate triangle of centres.
- 1770260-q01: the P label moved off segment PC.
- 1770219-q01: the h label moved to a dimension arrow beside the cone; the hidden half of the base rim is dashed.
- 1769062-q02: the height label moved to a dimension arrow outside the pyramid.
- 1767722-q30: the 10 label moved off the blue segment AD.
- 1767337-q01: the O label moved off the dashed diagonals.
- 1767069-q01: M moved to the right-hand base edge so the labels 6 and sqrt 7 no longer touch other edges.
- 1766655-q01: face labels centred in the faces; the V label and a gap label that touched edges were removed.

## Validation

- `chk.py`: `chk OK` (3 check files).
- `precheck.py 224`: `PRECHECK OK`. 81 records exported, 10 aliases, 100 topics accounted for, 23 diagrams.
- `finalize.py 224` (pre-check mode): 81 question records, 23 previews (0 missing, all compiled), 267 ZIP members, `checks_passed: true`. The review list contains only the text dates m/d/yy, 8/14/18 and 8/1/18 in 1769951-q01 (not maths slashes); there are no "GEOMETRY WITHOUT SKETCH" lines.
- `pdfcheck.py`: `records=81 asy_files=23 asy_failures=0 pages=81`, `warnings: 0`, no colour leak, `OK`.
