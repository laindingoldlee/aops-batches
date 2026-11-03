# AoPS batch 220 processing report

**61 question records** prepared from the 100 topics screened in batch 220.

Claude did all of the work in this run, with no DeepSeek or other external model. It screened every topic, solved each problem in full before choosing tags and a difficulty, checked every computable answer with exact or brute-force code (`chk_en01.py` to `chk_en03.py`), and checked every diagram by eye on contact sheets. The builders are `en01.py` to `en03.py`.

## IDs and duplicates

- IDs have the form `aops-topic-<AoPS topic id>-q<original part number>`. Multi-problem posts:
  - 1793574 (ages; acid mixture): q01, q02.
  - 1793467 (two sum-and-difference problems): q01, q02.
  - 1791167 (mock MATHCOUNTS Chapter, problems 1-6): q01-q06, numbered as in the post.
  - 1791941 (Problem 1 gold pieces, Problem 2 inequality): q01, q02.
  - 1788973 (problems 1 and 2): q01 is an alias, q02 is exported.
  - Marathon threads 1792707, 1791855, 1791115: only P1 is in the post, so q01.
- 11 repeats are aliased instead of exported:
  - `aops-topic-1792761-q01` -> `aops-topic-1987788-q01` (Kurtlandia 11- and 13-cent coins, 119; same wording)
  - `aops-topic-1793269-q01` -> `aops-topic-1933955-q01` (gcd(n!+1, (n+1)!+1) = 1; the earlier record asks for the gcd)
  - `aops-topic-1793132-q01` -> `aops-topic-2669400-q40` (primes with p(p+1)+q(q+1)=r(r+1), (2,2,3))
  - `aops-topic-1792707-q01` -> `aops-topic-1794543-q01` (b219 draft of this run: triangle rotated about A, AC bisects BB' implies AB' bisects CC'; same problem, from the same marathon P1)
  - `aops-topic-1771789-q01` -> `aops-topic-3260585-q01` (three pairs of twins at a round table, 8/15)
  - `aops-topic-1791613-q01` -> `aops-topic-2492319-q05` (four random points on a circle, quadrilateral contains the centre, 1/2)
  - `aops-topic-1790151-q01` -> `aops-topic-3061583-q01` (triangle whose sides are the medians has 3/4 the area)
  - `aops-topic-1790666-q01` -> `aops-topic-1985848-q01` (no Venn diagram for four sets with four circles)
  - `aops-topic-1786655-q01` -> `aops-topic-2971698-q01` (2018 MATHCOUNTS State Target #8, Varun's novels, 265)
  - `aops-topic-1790194-q01` -> `aops-topic-2168035-q01` (sum of n/2^n = 2)
  - `aops-topic-1788973-q01` -> `aops-topic-2231250-q01` (median AD of the 9-10-13 triangle, 10)
- Duplicate only: 1792761, 1793269, 1793132, 1792707, 1771789, 1791613, 1790151, 1790666, 1786655, 1790194.
- Near-misses kept (same idea, different numbers or target):
  - `1793143-q01` (y^2 = x^3+7) vs `aops-topic-1693483-q01` (y^2 = x^3-3); different argument (factor y^2+1).
  - `1787964-q01` (squares and rectangles in an n by n grid, with proofs) vs `aops-topic-2555332-q01` (the 8 by 8 chessboard only).
  - `1789074-q01` (mean of three-digit numbers from 2, 3, 5, 7) vs `aops-topic-2361244-q01` (digits 1, 3, 4, 5).
- No other repeats with the drafts of batches 212-219 were flagged by dup.py; nothing in xnotes.md is addressed to batch 220.
- `deduplication_registry.json` is cumulative; batches 76-80 are still missing.

## Screening

Statuses: included 51, partial 2, excluded 37, duplicate 10.

Partial:
- 1792647: parts 2 and 3 ("1234...N" and "from N to M") ask for general formulas with no numbers; only part 1 (zeros in 1 to 2019) is used.
- 1792695: the bonus question (both lines from the same side, not necessarily perpendicular) gives no distribution for the lines and is dropped.

Excluded as not usable (beyond non-maths posts):

- No problem text, or the problem is only in a missing image, video or link:
  - 1793680 (TMSCA base-15 problem #60 not stated)
  - 1792555 (pyramid volume question only in an attachment)
  - 1790919 (no problem text)
  - 1790918 ("in the grid below"; grid missing)
  - 1790742 (problem only in a MATHCOUNTS Mini video)
  - 1790184 (2012 MATHCOUNTS National Sprint #22 only in a linked picture)
  - 1789391 (graphs of Introduction to Algebra 9.4.4 only in images)
- Marathon opening posts with no real problem:
  - 1792427 ("0 marathon": rules not stated; only "make 0 from 2,2,2,2")
  - 1791418 (pre-calculus marathon: P1 is just f(x)=(x-3)/(x^2-3x-10) with no question)
  - 1791414 (quadratic marathon: rules only)
  - 1790004 ("make" marathon: rules and a trivial example only)

The other 26 excluded topics were non-mathematical:
- AMC results, MATHCOUNTS alternates, wild cards, countdown round and team-round strategy
- predicted national qualifiers and chapter results
- book, course and study advice (AMC 8, Intro to Geometry, C and P, GAIM, NSF, state prep)
- MATHCOUNTS Minis answer requests
- an Alcumus rating contest, a school poll request, "who is going to state", "hardest city"
- the ASMC discussion thread and test-difficulty questions

## Editorial changes

**Wrong posted answers, ill-posed problems and repairs:**

- `aops-topic-1790697-q01` (knights and thieves in a line of 2015): none of the posted choices (0, 1, 2014, 1002, 1003) is correct. The answer is 1008, proved by a monotonicity argument and checked by brute force for small lines. The record is free-response.
- `aops-topic-1791227-q01` (two dice, one number greater than the other): the quoted answer 13/18 is wrong; the correct answer is 5/6. The record asks the solver to judge the key.
- `aops-topic-1791264-q01` (three dice, sum less than 8): the teacher's 8C3/216 counts sums at most 8. For "less than 8" the answer is 7C3/216 = 35/216; the record explains both.
- `aops-topic-1791167-q04`: "Four numbers, 0, 1, 2, 3, 4, 5" corrected to the six numbers, one per variable (answer 3/20).
- `aops-topic-1793574-q01`: the poster's y = 4.5x reads "4.5 times as old"; the record asks for the ages (7 and 2.5) and for the error.
- `aops-topic-1791997-q01`: the poster's guess that a slanting post's shadow always has a different length is not quite right; the record shows the length is L sin(alpha+beta)/sin(beta), equal to L for alpha = beta = 60 degrees.
- `aops-topic-1792514-q01` (the "0 = 3" argument): the record asks for the error (x^3 = 1 does not imply x = 1, and x = 1 is not a root of the original) and the complex roots.

**Interpretations made explicit:**
- 1793819-q01: [ ] read as the floor function; posed as a proof.
- 1793329-q01 (Bulgaria, Grade 7): "ever again" read as "sooner or later"; at least one young man and one girl assumed.
- 1793143-q01: "solve in Z" became a proof that there are no integer solutions.
- 1792786-q01: "AG is produced to X" read as extending AG beyond G.
- 1792695-q01: each player chooses the direction with probability 1/2 and a uniform position.
- 1792157-q01: the series written with three terms are the infinite series.
- 1791167-q02: the empty subset is included (all 2^12 subsets equally likely).
- 1791167-q06: the fractal's figure was attached but the text determines it; the garbled phrase is read as each blue circle containing three white circles.
- 1788394-q01 (2015 MATHCOUNTS National Sprint #11): "as shown" made explicit (square on the side of AC away from B); answer 4 sqrt 5.
- 1789225-q01 (2016 State Sprint #29): dictionary order stated (a prefix comes first); answer 1899.
- 1760605-q01: "best possible estimate" read as the expected value (52.5).
- 1499461-q01: "n^3pq - n divides 3pq" read as 3pq divides n^(3pq) - n; answer 28 (N = 561).
- 1789625-q01: boxes packed with edges parallel to the large box.

**Posts turned into questions:**
- `1787964-q01`: "is there a formula for squares or rectangles in a grid" became formulas with proofs (204 squares and 1296 rectangles on a chessboard). The mention of triangles was dropped.
- `1789696-q01`: "is this a valid induction problem" became: prove the centres are collinear (no induction needed) and find the ratio of radii, (1 + sin 22.5)/(1 - sin 22.5).
- `1789625-q01`: "do floor(abc/xyz) boxes always fit" became a counterexample (one 2-cube in a 3-cube) and a sufficient condition.
- `1788599-q01`: when (x+p)(x+q) < 0 has solutions: exactly when p is not q.
- `1790252-q01`: the forgotten theorem is the multinomial theorem (-2240).
- `1791855-q01`, `1791115-q01`: P1 of two "make the number" marathons (construction answers).

## Diagrams

There are 11 Asymptote diagrams in the exported records: 10 in solutions and 1 in a question (1788394-q01). Each has an SVG preview and alt text. Every geometry-tagged record has a solution sketch. No geometry tags were used for 1792695-q01 (lines in a square: probability only), 1787964-q01 (grid counting) or the aliased records.

Fixes after viewing the contact sheets:
- 1793187-q01: the point E was renamed in the code, since the pair named E moved the labels E, y and x far from the side BC.
- 1792786-q01: a redundant dashed segment over side CA was removed and the L label was moved off the red line.
- 1792730-q01: the E and F labels were moved off the dashed circle.
- 1791997-q01: the post now leans away from the sun, as the text says.
- 1788394-q01: the 4 sqrt 5 label was moved off diagonal CA and the foot F was labelled.
- 1788973-q02: the P label was moved off the dashed perpendiculars.
- 1789696-q01: the lines were lengthened past the circles, three circles are drawn, and the w0 label was moved below the axis.
- 1789625-q01: the oblique direction was changed so that the centre Z no longer coincides with a corner of the small cube, and the labels were moved off hidden edges.
- 1792707-q01 (now an alias): the angle arcs were removed and the labels were moved off the lines.

## Validation

- `chk.py`: `chk OK` (3 check files).
- `precheck.py 220`: `PRECHECK OK`. 61 records exported, 11 aliases, 100 topics accounted for, 11 diagrams.
- `finalize.py 220` (pre-check mode): 61 question records, 11 previews (0 missing, all compiled), 195 ZIP members, `checks_passed: true`. The slash review list is empty and there are no "GEOMETRY WITHOUT SKETCH" lines.
- `pdfcheck.py`: `records=61 asy_files=11 asy_failures=0 pages=61`, `warnings: 0`, no colour leak, `OK`.

## Cross-batch review

After all nine batches were drafted, Claude reviewed every figure of this batch again at full size, checked repeats against the other eight batches (a similarity scan of all exported records, plus the workers' notes), and re-solved two randomly sampled records from the question alone.

No changes were needed in this batch.

Final state after the in-order rebuild (QB_FINAL=1, registry chained from batch 219): 61 records, 11 diagram previews, 195 ZIP members; statuses included 51, partial 2, excluded 37, duplicate 10. chk, precheck, finalize and pdfcheck all pass, and no figure leaks a colour.
