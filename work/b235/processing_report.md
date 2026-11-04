# AoPS batch 235 processing report

**75 question records** prepared from the 100 topics screened in batch 235.

Claude did all of the work in this batch, with no DeepSeek or other external model. It screened every topic and solved each problem in full before choosing tags and a difficulty. Every computable answer was checked with exact or brute-force code (`chk_p235_01.py` to `chk_p235_03.py`), and every diagram was checked by eye on contact sheets. The builders are `p235_01.py` to `p235_03.py`.

## IDs and duplicates

- IDs have the form `aops-topic-<AoPS topic id>-q<original part number>`. Multi-problem posts:
  - 1709513 (arithmetic-progression challenge, problems numbered 5-13 in the post): q05-q13.
  - 1708333 (three problems): only q03 is used (see Screening).
  - 1707676 (five geometry questions): q01, q04, q05.
  - 1707222 (four MATHCOUNTS problems): q01-q04. q01, q02 and q04 are aliases; q03 is exported.
  - 1704691 (handbook Warm-Up P1-P3): q01-q03. q02 and q03 are aliases; q01 is exported.
  - 1710170 (FBH problem with parts a and b) is one record, q01.
- 11 repeats are aliased instead of exported:
  - `aops-topic-1710800-q01` -> `aops-topic-2796071-q07` (smallest n with 11 dividing 2^n+1 and 13 dividing 3^n-1, 15; same wording)
  - `aops-topic-1710801-q01` -> `aops-topic-2796071-q11` (224 in base -3)
  - `aops-topic-106088-q01` -> `aops-topic-2791395-q01` (20% of the jellybeans eaten each day, 32 left after two days, 50)
  - `aops-topic-1709584-q01` -> `aops-topic-1754145-q01` (FBH 2018 Grade 8 P4, a/b+b/c+c/a <= b/a+c/b+a/c for a >= b >= c; identical)
  - `aops-topic-1707222-q01` -> `aops-topic-1755042-q115` (mean of three-digit numbers with distinct nonzero digits, 555)
  - `aops-topic-1707222-q02` -> `aops-topic-1745995-q01` (rectangle PQRS on a coordinate plane, perimeter 70)
  - `aops-topic-1707222-q04` -> `aops-topic-1757353-q03` (x^3-19x^2+cx+d with integer roots in geometric progression, -102)
  - `aops-topic-1311798-q01` -> `aops-topic-3097731-q05` (the harmonic series diverges)
  - `aops-topic-1704547-q01` -> `aops-topic-2193322-q01` ((2x-1)(x+1)(x+7) > 0)
  - `aops-topic-1704691-q02` -> `aops-topic-1752482-q01` (five coin flips with no two heads in a row, 13/32)
  - `aops-topic-1704691-q03` -> `aops-topic-2039398-q01` (mean of three-digit numbers with digits from {2,0,1,9}; the earlier record already asks both readings, 433 and 1288/3)
- Duplicate only: 1710800, 1710801, 106088, 1709584, 1311798, 1704547.
- Near misses kept (same idea, different numbers or target):
  - `1711161-q01` (rainy vacation, 10 rainy days, 13 and 17 dry half-days) vs `aops-topic-3038270-q01` (13, 11, 12).
  - `1706974-q01` (solve 9 = b+4 mod 20, and the step 1 = b+2 mod 3) vs `aops-topic-2758036-q01` (the textbook system x = 1 mod 3, x = 2 mod 4). The new record leaves out the system.
  - `1705567-q01` (sum of 2n/4^n) vs `aops-topic-2168035-q01` (sum of n/2^n).
  - `1704105-q01` (extremes of x^2+y^2 on a general circle) vs `aops-topic-2757304-q01` (one circle, integer points only).
- dup.py found no repeats with the drafts of batches 231-234. Nothing in `xnotes.md` is addressed to batch 235.
- `deduplication_registry.json` is cumulative; batches 76-80 are still missing from it.

## Screening

Statuses: included 63, partial 2, excluded 29, duplicate 6.

Partial:
- 1708333: only problem 3 (the magic bridge) is used. Problem 1 (Bernie's cannery) gives irrational hours and counts (x = 2+sqrt309, y = (1+sqrt809)/2). Problem 2 (the wallet thief, each suspect telling two truths and one lie) contradicts itself: William's statements clear William and Fred, so Jenny's lie is "William did it" and "I don't know where the wallet was" is true; but Al's statements then force "Jenny knows where the wallet was".
- 1707676: questions 1, 4 and 5 are used. Question 2 ("how do you find the internal tangent of a circle") and question 3 ("is there a formula for the goat-grazing problem") state no specific problem.

Excluded as not usable (beyond non-maths posts):
- Data only in a missing image or attachment: 1710176 (FBH 2017 Grade 8 P2, the 5x5 table), 1636579 (polyomino dissection), 1708960 (squares in a picture, inside an advice post), 1707376 ("see attachment").
- No problem text: 1704306, 1704321 (redacted).
- Ill-posed or not reconstructible:
  - 1706814: probability that a randomly placed unit circle avoids 29 others; no distribution is given.
  - 1704370: an SPOJ series whose rule cannot be found from five terms.
  - 1704669: a garbled Turkish olympiad system; the natural reading has no real solution.
  - 1690518: a textbook true/false item about 32 kg : 36 dollars = 8 kg : 9 dollars; the intended answer depends on a textbook convention, and the proportion itself holds.
- Not a mathematics question:
  - 1570264: the "Equate" game rules; its only problem is (1+2+3)/2.
  - 1705941: whether a sphere of volume pi^3 can be built "in reality".
  - 1703658: an open-ended list of uses of the difference of squares.

The other 16 excluded topics were non-mathematical: advice on MATHCOUNTS preparation, tryouts, AoPS classes and books, school credit, a petition about mock contests, an FTW clone advert, Khan Academy, polls, a state cutoff question, the countdown-round rules, a question on how to approach transformations, and a post about a sister's silly mistakes.

## Editorial changes

**Wrong posted answers, ill-posed problems and repairs:**
- `1710811-q01`: the conditions a = 2c, bd = c, d = 16 do not determine a. The record asks for a in terms of b (32b) and whether a is determined.
- `1705943-q01`: "Express 4^6+8^3-32^2 as a power of 2" is impossible, since the value is 7 * 2^9 = 3584. The record asks for the form m * 2^k.
- `1709569-q01` (FBH 2018 Grade 7 P2): "digits distinct than zero" means nonzero digits. With distinct digits there is no solution (the maximum is 282 < 293). The answer is 997, and the solution notes the distinct-digit case.
- `1710140-q01` (FBH 2017 Grade 7 P4, climbers and bread): two answers if each group is present (1, 14, 12 and 2, 4, 21), and a third if there are no men. The record asks for all possibilities.
- `1709513-q09`: the post's "S3 = S(S2-S1)" is corrected to S3 = 3(S2-S1).
- `1709513-q10`: the sequence has 180 terms, so it has two middle terms, 546 and 551. The record asks for both.
- `1704033-q01` (donuts): the poster's inclusion-exclusion expression is right, but it equals 216, not 346.
- `1706974-q01`: the poster's b = 4 (mod 20) is corrected to b = 5.
- `1710592-q01` (2018 National Sprint #12): one of the poster's groups weighs 35, not 34. The record gives a correct split and proves that 6 is the minimum.
- `1704691-q01` (handbook, UTC/EST): the poster doubted the key, but the handbook answer 555 is correct.

**Interpretations made explicit:**
- 1709625-q01: "E and F on side ABCD" is read as side AB.
- 1710125-q01: h_a and h_b are the altitudes from A and B.
- 1710118-q01: "every 7th card" means the multiples of 7.
- 1709576-q01: the time is measured over a 24-hour day.
- 1708605-q01: trees of the same kind are indistinguishable.
- 1708235-q01 (HK contest): the nine numbers are distinct positive integers; the pairwise sums need not all be distinct.
- 1707812-q01: N-7 is a positive multiple of 4, 5 and 6, giving 67.
- 106088-q01: 32 jellybeans are left at the end of the second day.
- 1706861-q01: "between" is strict, which excludes 5000.
- 1692181-q01: the face showing is random.
- 1707676-q05: "length of a regular pentagon" means its diagonal (1+sqrt5).
- 1707676-q04: each frustum has radii 6 and 16 and height 48.

**Posts turned into questions:**
- `1711180-q01`: all k with 48k^2+1 a square, proved by Pell descent.
- `1294839-q01`: find the error in the "1+3+9+... = -1/2" argument.
- `1708456-q01`: prove that a line meets a plane in nothing, a point or the whole line.
- `1707260-q01`: the poster asked for a general partition formula, which is not known in closed form. The record instead proves F(N,2), the standard recurrence, and F(N,3) = round(N^2/12).
- `1705590-q01`: equal numbers of quarters, dimes and nickels, done in general with a sample total of $6.00.
- `1704105-q01`: extremes of x^2+y^2 on a general circle.
- `1705202-q01`: the locus is the hyperbolas xy = +-sqrt c.
- `1708628-q01`: the folded-rectangle crease, with the similarity the poster asked about explained.
- `1704985-q01`: the solution explains "Newton's little formula" as finite differences.

## Diagrams

There are 19 Asymptote diagrams in the exported records:
- 17 in solutions;
- 2 in questions: 1709573-q01 (four circles) and 1704985-q01 (rods and connectors), both redrawn from the text because the post's image was missing.

Each diagram has an SVG preview and alt text. Every geometry-tagged record has a solution sketch. The geometry tags were dropped from 1710592-q01 (cookie volumes, a counting problem) rather than adding a meaningless sketch.

Fixes after viewing the contact sheets:
- 1709573-q01: the length labels 2-r and 1+r touched circle arcs, so the right triangle O O2 P is now drawn separately with its labels. The O label was moved off the circles.
- 1710125-q01: the 80 and 126 degree labels overlapped. The 126 degree mark is now on the vertical angle DHE, which has room, and the solution text says so. The 80 degree label was moved into the free part of angle A.
- 1710138-q01: the 60 degree labels were moved off the blue diagonals.
- 1710185-q01: the K and L labels were moved off the dashed circle.
- 1709625-q01: the circle label k had coincided with vertex D and was moved.
- 1708628-q01: the O label was moved off the dashed diagonal.
- 1708456-q01: line m passed almost through P and was moved away; the Pi label was moved inside the plane.
- 1708321-q01: the side labels a were moved off the tick marks.
- 1707676-q04: the elliptical arcs were fixed (the first version failed to compile), and the labels were moved off the ellipses and edges.
- 1705202-q01: the axis labels were moved off the hyperbola branches.
- 1704105-q01: the P1 label was moved off the circle.

## Validation

- `chk.py`: `chk OK` (3 check files).
- `precheck.py 235`: `PRECHECK OK`, with 75 records exported, 11 aliases and 100 topics accounted for.
- `finalize.py 235` (pre-check mode):
  - 75 question records and 19 previews (0 missing, all compiled);
  - 245 ZIP members, `checks_passed: true`;
  - no "GEOMETRY WITHOUT SKETCH" lines;
  - the only slash review lines are the text "blue/blue" and "blue/white" in 1692181-q01.
- `pdfcheck.py`: `records=75 asy_files=19 asy_failures=0 pages=75`, `warnings: 0`, no colour leak, `OK`.
