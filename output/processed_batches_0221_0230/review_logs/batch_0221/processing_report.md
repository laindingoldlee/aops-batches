# AoPS batch 221 processing report

**63 question records** prepared from the 100 topics screened in batch 221.

Claude did all of the work for this batch, with no DeepSeek or other external model. It screened every topic, solved each problem in full before choosing tags and a difficulty, checked every computable answer with exact or brute-force code (`chk_p221_01.py` to `chk_p221_03.py`), and checked every diagram by eye on contact sheets. The builders are `p221_01.py` to `p221_03.py`.

## IDs and duplicates

- IDs have the form `aops-topic-<AoPS topic id>-q<original part number>`. Multi-problem posts:
  - 1785634 (popcorn1's rejected AMC 8 problems 1-6): q01-q05, numbered as in the post (problem 6 not given).
  - 1785658 (TMSCA number sense P1-P3): q01-q03.
  - 1780989 (Math Problems #1-#3): q01, q02 (problem 3 dropped).
  - 1695399 (2012 National Sprint P25, P29, P30 and Target P6): q25, q29, q30, q06, all aliases.
  - 1781932 (reverse marathon): the only real problem is the example "P0" in the rules, so q00 (an alias).
  - Marathon threads 1789143, 1789162, 1787280, 1785255: only P1 is in the post, so q01.
- 18 repeats are aliased instead of exported:
  - `aops-topic-1789230-q01` -> `aops-topic-2865360-q01` (disk rolling round a clock face, 4 o'clock)
  - `aops-topic-1789170-q01` -> `aops-topic-2668968-q19` (proof of nCr = n!/(r!(n-r)!))
  - `aops-topic-1788621-q01` -> `aops-topic-1789216-q01` (same number of digits in bases 5 and 8, 195; identical wording, batch 212-220 release)
  - `aops-topic-1787435-q01` -> `aops-topic-1803814-q01` (2013 MATHCOUNTS State Team #10, square centred on a circle, 0.46)
  - `aops-topic-1786654-q01` -> `aops-topic-3491984-q01` (three uniform numbers with sum less than 1, 1/6)
  - `aops-topic-1786990-q01` -> `aops-topic-2812530-q01` (pyramid PABCD cut by a plane through A, 7/19; the earlier record also asks for an error)
  - `aops-topic-1787277-q01` -> `aops-topic-2292490-q02` (2017 MATHCOUNTS National #26, letter/number tiles, 5/23)
  - `aops-topic-1786839-q01` -> `aops-topic-2490024-q01` (2018 MATHCOUNTS State #24, Ivory's numbers ending in 7, 1)
  - `aops-topic-1786904-q01` -> `aops-topic-2477421-q01` (min x^2+y^2 on (x-3)^2+(y-4)^2=49, 4)
  - `aops-topic-1695399-q29` -> `aops-topic-2477421-q01` (same problem, 2012 National Sprint #29)
  - `aops-topic-1786656-q01` -> `aops-topic-2003369-q01` (2018 MATHCOUNTS State #27, three dice with a pair summing to 6, 19/54)
  - `aops-topic-1654926-q01` -> `aops-topic-3157905-q01` (look-and-say term after 1211, 111221)
  - `aops-topic-1785779-q01` -> `aops-topic-1951929-q01` (train, 300 km, speed 25 km/h)
  - `aops-topic-1695399-q25` -> `aops-topic-2009418-q03` (round-robin with five withdrawals, 26)
  - `aops-topic-1695399-q30` -> `aops-topic-2304304-q01` (short paths on a 2x2x2 cube, 54)
  - `aops-topic-1695399-q06` -> `aops-topic-2025281-q01` (Target #6, 560 interior lattice points, 162)
  - `aops-topic-1781932-q00` -> `aops-topic-2660159-q01` (n^2 and n^3 use each digit once, 69)
  - `aops-topic-1784461-q01` -> `aops-topic-1850375-q01` (2^(16^x) = 16^(2^x), 2/3)
- Duplicate only: 1789230, 1789170, 1788621, 1787435, 1786654, 1786990, 1787277, 1786839, 1786904, 1786656, 1654926, 1785779, 1695399, 1781932, 1784461. The repeat 1786904 / 1695399-q29 inside this batch is handled by aliasing both to the same earlier record.
- Repeats with other batches of this run: 1784461-q01 is also b226 draft 1760552-q01, and 1695399-q06 is also b226 draft 1761688-q01. Both copies repeat earlier releases, so they alias to the prior record and nothing needs to go in `xnotes.md`. Nothing in `xnotes.md` is addressed to batch 221.
- Near misses kept (same idea, different numbers or target):
  - `1789275-q01` (circumradius of the side-6 equilateral triangle) vs `aops-topic-2793027-q05` (area of that circumcircle).
  - `1785275-q01` (OP is the perpendicular bisector of the chord of contact) vs `aops-topic-2579833-q01` (equal tangents only).
  - `1788057-q01` (count the sets of four consecutive integers with product below 100000) vs `aops-topic-3084312-q14` (the product is one less than a square).
  - `1765739-q01` (a^3+b^3+c^3 >= a^2b+b^2c+c^2a) vs `aops-topic-1891258-q01` (a^2b+b^2c+c^2a >= 3abc).
- `deduplication_registry.json` is cumulative; batches 76-80 are still missing from the registry.

## Screening

Statuses: included 54, partial 2, excluded 29, duplicate 15.

Partial:
- 1780989: problem 3 (AC = AB with angle ACB = 96 degrees) is impossible, since a base angle of an isosceles triangle cannot be obtuse, and the point D is underdetermined. Only problems 1 and 2 are used.
- 1785634: problem 6 is not given. Problems 1-5 are used.

Excluded as not usable (beyond non-maths posts):
- No problem text, or the problem only in a missing image:
  - 1788782 (AoPS book problem 1.3.4 not stated)
  - 314315 ("the array shown below" is only in the image)
  - 1787206 and 1787207 (empty posts)
  - 1588499 ("Nice or bad cards", no problem)
  - 1785508 (equation only in an image)
  - 1785210 (Vietnamese help request with no problem)
- Ill-posed or impossible:
  - 1786911: the statement and the working use different expressions. As stated, the minimum is the root of a quartic (about 1.1313); the other reading is trivial.
  - 1783140: garbled nested radical of a negative number, with no question.
  - 1783102: two of the roots are non-real, so sqrt(p-1) is ambiguous, and the value (about 6.1418) is not rational.
  - 1782881: the conditions angle ABD = angle AEB and BP = CE cannot hold together (checked numerically over all triangle shapes).
- 1786337: optimal packing of circles in a 65 by 120 rectangle, with no elementary verifiable answer.
- 1599867: only asks whether the notation 7 = 1 (mod 2) is right.

The other 16 excluded topics were non-mathematical:
- MATHCOUNTS preparation, tips, qualifying, nationals cutoffs and results
- AMC-to-AIME cutoff polls
- "best subject" and memorising questions
- a binary-explanation request and rate-problem advice
- a germs question

## Editorial changes

**Wrong posted answers, ill-posed problems and repairs:**

- `aops-topic-1787416-q01`: "triangle ABC is right-angled" is impossible with these data (with the right angle at B or C, D is a vertex; at A, the area of ADC would be 169*195/788). Replaced by "acute-angled", which makes the answer 84 unique (13-14-15 triangle). The note records that D outside BC would give 24.
- `aops-topic-1780989-q02`: an exact probability 29/50 of drawing two black marbles from 101 is impossible (b(b-1) = 5858 has no integer root). Following "to the nearest whole number", 29/50 is read as the rounded value 0.58; this gives 77 black and 24 green marbles.
- `aops-topic-1780989-q01`: "six concyclic points" gives no definite probability; the points are taken as equally spaced (regular hexagon), giving 2/5.
- `aops-topic-1786041-q01`: there are no constants a, b with D_{n+2} = aD_{n+1} + bD_n (this is proved in part (b)). The record proves D_{n+2} = (n+1)(D_{n+1}+D_n), so b/a = 1.
- `aops-topic-1785367-q01` (2004 MATHCOUNTS National Target #5): the poster's method is correct, but the trial search skipped X = 29. The answer is 2100, not the poster's 2720.
- `aops-topic-1789026-q01`: the proposed weighted-digit test for 2^n and 5^n is disproved (counterexamples 25 and 104). It holds only for 2, 4 and 5.
- `aops-topic-1786013-q01`: (4a)^2 and (9b)^2 corrected to 4a^2 and 9b^2. As typed, the expression is not a perfect square plus a square term.
- `aops-topic-1785447-q01`: a 20% chance per hour over 4.5 hours is ambiguous; the record uses the model P(no fish in t hours) = 0.8^t, giving 1 - 512 sqrt5/3125.
- `aops-topic-1785283-q01`: "iron balls" made from an aluminium bar became "balls".

**Interpretations made explicit:**
- 1787556-q01: "6.3x+9y=2" is exercise 6, so the line is 3x+9y=2.
- 1786616-q01: rotations identified and empty seats indistinguishable (120; general (n-1)!/(n-k)!).
- 1786360-q01: the numerators continue with differences 3, 4, 5, ... (sum 2541/1000).
- 1606524-q01: the infinite fraction is defined as a limit, and convergence is proved.
- 1785265-q01: A, B >= 0 is assumed, so that tan(A-B) = 0 forces A = B = 30 degrees.
- 1781243-q01: "how far does it travel after the fifth jump" is read as the total distance (2954/81 in); the fifth jump alone is also given.
- 1785758-q01: n and k are both minimised (n = 2, k = 1007, attained together).
- 1785255-q01: clue 7 excludes the divisor 1.
- 1785634-q03 and q04: the number of digits 1 in 10 otimes = 3991680; the fly's distances include floor and ceiling.
- 1785652-q01: the higher rate holds for the whole order.
- 1787422-q01: choices "x + y/20" and "x+y /20" are read as x + y/20 and (x+y)/20.
- 1784530-q01: "column" is read as the labelled row.

**Posts turned into questions:**
- `1788776-q01`: "how do the special factorisations work?" became proofs of the identities, the factor-theorem reason behind them, and a proof that a^2+b^2 has no real linear factorisation.
- `1786099-q01`: "how do you take 4/9 mod 25?" became the modular inverse, giving 6.
- `1789162-q01`: an operators-marathon P1, answered 10 + 8 x 7 - 6 / 2 = 63.
- `1789101-q01`: the Brady weights answer 27 is confirmed, with a proof that {1, 3, 9, 27} is the only possible 4-weight set.

## Diagrams

There are 16 Asymptote diagrams in the exported records, all in solutions. Each has an SVG preview and alt text, and every geometry-tagged record has a solution sketch. The aliased records have no figures. No geometry tags were used for 1787875-q01 (geometric probability on a square of times) or 1785634-q04 (fly in a room: distances only).

Fixes after viewing the contact sheets:
- 1788191-q01: a dashed continuation of the large arc outside the rectangle was removed, which also freed the Q label; an arc was added for the angle theta.
- 1787556-q01: the large coordinate labels overlapped the axes and the line. They were replaced by A and B with fraction tick labels, and the 1/3 tick label was moved off the line.
- 1787424-q01: the O label was moved off the radius, and the 10 label off the middle circle.
- 1785946-q01: the Y label was moved away from the 1 - t label.
- 1785634-q05: the 5 labels on PB and PD were moved off the segments and the side.
- 1785283-q01: the 9 cm radius label was moved off the sphere's equator.
- 1785658-q01: the 30 degree label was moved just beyond its arc (first it touched a radius, then it sat too far away).

## Validation

- `chk.py`: `chk OK` (3 check files).
- `precheck.py 221`: `PRECHECK OK`. 63 records exported, 18 aliases, 100 topics accounted for, 16 diagrams.
- `finalize.py 221` (pre-check mode): 63 question records, 16 previews (0 missing, all compiled), 206 ZIP members, `checks_passed: true`.
- `pdfcheck.py`: `records=63 asy_files=16 asy_failures=0 pages=63`, `warnings: 0`, no colour leak, `OK`.
