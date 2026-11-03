# Question bank formatting and packaging prompt

Package the questions and detailed solutions we have prepared into the following format for import into my question bank. Use one ZIP for the whole batch. This is a formatting and packaging task: preserve the prepared mathematical content, while applying the diagram and fraction requirements below.

## 1. Deliver one ZIP file

Name it `question_bank_import.zip`. At the ZIP root, include:

- `manifest.json`
- A `questions` folder containing one folder per question, named using its unique ID.

Each question folder must contain:

- `metadata.json`
- `question.tex`
- `solution.tex`
- An `assets` folder only when supporting files, including generated diagram previews, are required.

Keep multipart questions together as one question record. Preserve every part, answer choice, condition, and source detail. Each question and solution must be self-contained.

## 2. Manifest

Use this structure for `manifest.json`, listing every question ID exactly once:

```json
{
  "schema_version": "1.0",
  "question_ids": [
    "smo-2024-junior-round-1-q01"
  ]
}
```

The ID above is illustrative. Replace it with the actual IDs. Keep schema version `1.0`; the optional `diagram_previews` metadata below extends this format without changing the existing question and solution files.

## 3. Question metadata

Use this structure for each `metadata.json`:

```json
{
  "id": "smo-2024-junior-round-1-q01",
  "source": {
    "competition": "SMO",
    "year": 2024,
    "division": "Junior",
    "paper": null,
    "round": "1",
    "question_number": "1"
  },
  "tags": [
    "Divisibility",
    "Remainders and congruences"
  ],
  "difficulty": 4,
  "difficulty_rationale": "Requires choosing a useful modulus and combining two short deductions.",
  "question_file": "question.tex",
  "solution_file": "solution.tex",
  "latex_dependencies": {
    "packages": [
      { "name": "amsmath", "options": [] },
      { "name": "amssymb", "options": [] }
    ],
    "tikz_libraries": [],
    "preamble_commands": []
  },
  "assets": [],
  "diagram_previews": []
}
```

The values are illustrative. Replace them with actual information.

Rules:

- Use valid UTF-8 JSON without comments or trailing commas. JSON keys contain ordinary underscores, such as `question_number`; do not write Markdown-escaped underscores such as `question\_number`.
- Use `null` for unknown source information; do not invent it.
- Keep the year as an integer or `null`. Other source fields are strings or `null`.
- Use `paper` for distinctions such as AMC paper A or B.
- Construct IDs from available source details using lowercase letters, numbers, and hyphens. Include paper, division, and round when needed to distinguish questions.
- Preserve an existing question's ID when preparing a corrected replacement, so importing can replace that record without creating a duplicate.
- For an unidentified source, use an ID such as `unknown-<batch-label>-q01`, with a distinct batch label.
- The folder name, manifest ID, and metadata ID must agree.
- Paths are relative to the question's folder.
- Store question and solution LaTeX in the `.tex` files, not as JSON strings. Correctly escape backslashes in JSON fields that contain LaTeX commands.
- Declare actual package requirements. Always include `amsmath` for `\dfrac`; include `amssymb` for the usual additional symbols. Include `asymptote` whenever an `asy` environment is used. Include `enumitem` when list options require it.
- Use the standard commands described below where possible. Declare essential custom commands in `preamble_commands`, with names unique to the question to avoid collisions in combined exports.

## 4. Detailed tags

Use only the exact tag names below. Group headings are organisational labels, not tags. The vocabulary includes three kinds of tags:

- **Content tags** identify the mathematical ideas a student needs to know.
- **Technique tags** identify a decisive method in a natural full solution.
- **Context tags** identify recurring settings useful for worksheet selection.

Assign content tags inclusively: include every material topic appearing in the question or used in a sound solution, even when it is not the dominant topic. Add a technique tag only when that technique is genuinely central, not for routine algebra or trivial checking. Add at most two context tags, and only when the setting is mathematically meaningful.

Do not invent synonyms, alternate spellings, broader/narrower variants, or new tags. Do not tag a theorem or technique merely because it could be used: it must be used in the supplied solution or genuinely needed to understand the question. Remove duplicate tags.

### Arithmetic and numerical reasoning

- Whole-number operations
- Order of operations
- Place value
- Decimals
- Fractions
- Percentages
- Ratios, proportions, and variation
- Rates
- Distance, rate, and time
- Relative speed
- Work and rates
- Unit conversion
- Estimation
- Averages and weighted averages
- Clock problems
- Date and time
- Money and currency
- Repeating decimals

### Number theory

- Divisibility
- Divisibility rules
- Factors and multiples
- Prime numbers
- Prime factorisation
- HCF and LCM
- Divisor counting
- Sum of divisors
- Perfect powers
- Perfect squares
- Perfect cubes
- Powers of two
- Factorials
- Trailing zeros
- Parity
- Remainders and congruences
- Modular exponentiation
- Chinese remainder theorem
- Fermat's little theorem
- Euler's theorem and totient
- Multiplicative order
- Quadratic residues
- Digits and bases
- Units digits and last digits
- Palindromes
- Floor and ceiling functions
- Diophantine equations
- Linear Diophantine equations
- Pythagorean triples
- Triangular numbers
- Continued fractions

### Algebra

- Algebraic manipulation
- Algebraic expressions and identities
- Factoring
- Difference of squares
- Sum and difference of cubes
- Completing the square
- Substitution
- Equations and systems of equations
- Linear equations
- Systems of linear equations
- Quadratic equations
- Rational equations
- Radical equations
- Absolute value
- Inequalities
- AM-GM inequality
- Cauchy-Schwarz inequality
- Exponents
- Radicals
- Logarithms
- Rationalising denominators
- Polynomials
- Polynomial roots
- Vieta's formulas
- Remainder theorem and factor theorem
- Newton's sums
- Partial fractions
- Functions
- Functional equations
- Inverse functions
- Piecewise functions
- Custom operations
- Sequences and series
- Arithmetic sequences
- Geometric sequences
- Recurrence relations
- Fibonacci sequence
- Summation
- Telescoping sums
- Binomial theorem
- Complex numbers
- Roots of unity
- De Moivre's theorem
- Matrices and determinants
- Calculus
- Maxima and minima

### Geometry

- Angles and lines
- Angle chasing
- Angle sums
- Parallel lines
- Perpendicular lines
- Triangles
- Triangle inequality
- Isosceles triangles
- Equilateral triangles
- Right triangles
- Special right triangles
- Pythagorean theorem
- Similarity
- Congruence
- Medians and centroids
- Altitudes
- Midpoints
- Perpendicular bisectors
- Angle bisectors
- Angle bisector theorem
- Ceva's theorem
- Stewart's theorem
- Mass points
- Quadrilaterals and polygons
- Parallelograms
- Rectangles
- Squares
- Rhombi
- Kites
- Trapezoids
- Regular polygons
- Equiangular polygons
- Diagonals
- Circles
- Arcs and chords
- Inscribed angles
- Cyclic quadrilaterals
- Tangents
- Tangent circles
- Power of a point
- Radical axis
- Circumcircles and circumcentres
- Incircles and incentres
- Ptolemy's theorem
- Lengths, perimeter, and area
- Area decomposition
- Area ratios
- Heron's formula
- Brahmagupta's formula
- Coordinate geometry
- Slope
- Distance formula
- Lattice points
- Shoelace formula
- Pick's theorem
- Conic sections
- Parabolas
- Ellipses
- Hyperbolas
- Trigonometry
- Trigonometric identities
- Law of sines
- Law of cosines
- Geometric transformations
- Reflections
- Rotations
- Translations
- Dilations and homothety
- Vectors
- Loci and geometric constraints
- Solid geometry
- Nets
- Polyhedra
- Euler's polyhedron formula
- Cubes and rectangular prisms
- Cylinders
- Cones
- Pyramids
- Spheres
- Surface area
- Volume
- Scaling of length, area, and volume

### Combinatorics and graph theory

- Counting principles
- Addition principle
- Multiplication principle
- Systematic counting
- Complementary counting
- Casework
- Permutations
- Combinations
- Arrangements with restrictions
- Circular arrangements
- Multiset permutations
- Derangements
- Distributions and integer solutions
- Stars and bars
- Partitions and compositions
- Sets and inclusion–exclusion
- Venn diagrams
- Pigeonhole principle
- Bijections
- Double counting
- Recursive counting
- Generating functions
- Combinatorial identities and binomial coefficients
- Pascal's triangle
- Vandermonde's convolution
- Catalan numbers
- Paths and networks
- Lattice paths
- Graph theory
- Trees
- Graph colouring
- Colourings, tilings, and coverings
- Counting intersections
- Counting regions
- Counting shapes in figures
- Fencepost counting
- Burnside's lemma

### Probability and statistics

- Probability
- Complementary probability
- Conditional probability
- Independent events
- Bayes' theorem
- Binomial probability
- Geometric probability
- Geometric distribution
- Expected value
- Random walks
- Recursive probability
- Sampling with replacement
- Sampling without replacement
- Dice probability
- Data and graph interpretation
- Mean
- Median
- Mode
- Range
- Harmonic mean

### Logic, games, and proof

- Logical deduction
- Truth-tellers and liars
- Counterexamples
- Cryptarithms
- Magic squares
- Games and strategies
- Combinatorial games
- Mathematical induction
- Proof by contradiction
- Proof by contrapositive
- Proof by cases

### Problem-solving techniques

- Invariants and monovariants
- Extremal principle
- Symmetry
- Bounding and extremal cases
- Working backwards
- Pattern recognition
- Small cases
- Pairing and grouping
- Process simulation
- Construction
- Coordinate bashing
- Algebraic bashing

### Context tags

- Age problems
- Mixture problems
- Digit problems
- Calendar and clock problems
- Probability with dice
- Paper folding
- Geometric dissection

### Tagging examples and rules

- Prefer the narrowest applicable tag, but also keep a useful parent tag for broad search. For example, a factor-theorem problem receives both **Polynomials** and **Remainder theorem and factor theorem**; a Pythagoras problem receives **Right triangles** and **Pythagorean theorem**.
- Do not confuse an object with a method. A circle problem solved by angle chasing receives **Circles** and **Angle chasing**. It receives **Power of a point** only if that result is actually used.
- Do not use a technique tag for superficial steps. Nearly every algebraic solution includes some manipulation; add **Algebraic manipulation** only when manipulation is a substantial target skill.
- Use **Casework** only for nontrivial structural cases, not separate answer choices or a routine positive/negative split.
- Use **Mathematical induction** only when induction is part of the supplied argument.

Examples:

| Situation | Tags |
| --- | --- |
| Find the last two digits of a large power | `Remainders and congruences`, `Modular exponentiation`, `Units digits and last digits` |
| Count nonnegative integer solutions to an equation | `Diophantine equations`, `Distributions and integer solutions`, `Stars and bars` |
| Find an area ratio in a triangle using mass points | `Triangles`, `Area ratios`, `Mass points` |
| Analyse a repeated-move puzzle using a preserved quantity | `Games and strategies`, `Invariants and monovariants` |

### Optional additional metadata

The following fields are not tags. Add them only if the import system can store them without breaking existing records; otherwise omit them completely. Do not put unsupported fields into `metadata.json`.

```json
{
  "answer_format": "multiple_choice",
  "response_type": "integer",
  "solution_methods": ["Remainders and congruences"],
  "problem_context": ["Digit problems"],
  "prerequisites": ["Remainders and congruences"],
  "has_diagram": false,
  "estimated_time_minutes": 8
}
```

- `answer_format`: `multiple_choice`, `short_answer`, `proof`, `multi_part`, or `open_response`.
- `response_type`: `integer`, `rational`, `real_number`, `expression`, `choice`, `proof`, `construction`, or `other`.
- `solution_methods`: decisive technique or theorem tags from the controlled vocabulary.
- `problem_context`: context tags only.
- `prerequisites`: the smallest set of key content tags a student should already know.
- `has_diagram`: Boolean.
- `estimated_time_minutes`: a positive integer for a prepared student working independently; omit it unless it has been deliberately estimated.

If these optional fields are supported, include them in the metadata structure consistently across the batch. If not, use only the required schema in Section 3.

## 5. Difficulty

Assign an integer from 1 to 10 using this provisional, fixed rubric:

| Score | Description |
| --- | --- |
| 1 | Immediate application of a definition or basic fact. |
| 2 | A routine procedure with a little reasoning. |
| 3 | One accessible observation or a short chain of familiar deductions. |
| 4 | An unstated approach requiring some exploration and a few connected steps. |
| 5 | A meaningful insight or a moderately demanding combination of familiar ideas. |
| 6 | A difficult-to-spot insight followed by substantial reasoning, or several connected insights. |
| 7 | A challenging competition problem requiring sustained strategic reasoning and multiple non-obvious deductions. |
| 8 | A very challenging problem with deeply hidden ideas or demanding execution, near the upper end of the intended AIME-oriented teaching range. |
| 9 | Beyond the usual intended teaching range, requiring unusually demanding insights or arguments. |
| 10 | Exceptional difficulty, substantially beyond the intended teaching range. |

Judge the difficulty of discovering and completing the simplest sound solution, assuming the required mathematical concepts are known.

Do not determine difficulty solely from age, grade, competition name, original question number, solution length, or advanced terminology. A short solution may require a very difficult insight. Keep the scale consistent across batches; do not automatically give the hardest question in each batch a 10. Competition references describe the intended range, not an exact conversion between competitions and scores.

Include a brief difficulty rationale in the metadata.

## 6. LaTeX bodies and fractions

`question.tex` must contain only the question's LaTeX body, including answer choices, subparts, and diagrams where applicable.

`solution.tex` must contain the corresponding detailed solution's LaTeX body, including the final answer and the geometry sketches required in Section 7.

For both files:

- Do not include `\documentclass`, package declarations, `\begin{document}`, or `\end{document}`.
- Do not add an outer question number, source heading, difficulty label, or tags. The bank supplies these.
- Internal numbering for subparts and answer choices is allowed.
- Use ordinary prose, standard math commands, `$...$` or `\(...\)` for inline mathematics, and `\[...\]` or standard AMS environments for displayed working.
- Use ordinary `enumerate` and `itemize` environments for lists. Prefer `\textbf`, `\emph`, and `\textit` for simple text formatting. Avoid unnecessary page-layout commands or custom environments.
- Keep shared information needed by a question inside that question's record. Avoid references to other records.
- Use `\dfrac{...}{...}` for every typeset fraction, including inline fractions, nested fractions, answer choices, solutions, and mathematical labels in diagrams.
- Do not use `\frac`, `\tfrac`, `\cfrac`, `\over`, or slash notation as a substitute for a typeset mathematical fraction. Expand unbraced fraction arguments to braces, for example `\dfrac{1}{2}`.
- This fraction preference does not change binomial coefficients, ratio notation, URLs, filenames, or programming arithmetic. In Asymptote calculations, use normal Asymptote arithmetic such as `x/2`; use `\dfrac` inside typeset labels.

Keep the raw question and solution sources intact in the ZIP. Website previews supplement this source; they do not replace it. The bank will assemble selected questions in increasing difficulty order, followed by their corresponding solutions in the same order.

## 7. Geometry sketches and Asymptote diagrams

### Mandatory geometry sketches

Every geometry problem's **solution** must include at least one clear, labelled sketch of the relevant geometric configuration, even if a similar diagram already appears in the question and even if the problem can be solved without drawing it.

Include every materially distinct configuration or case that the solution needs to consider. For example, draw separate sketches when an interior/exterior point, an acute/obtuse configuration, or two possible intersections changes the reasoning. If a construction adds auxiliary lines, points, circles, or other objects, show them in the solution sketch. Provide additional sketches when needed for clarity.

“All cases” means all relevant, structurally distinct geometric cases under the problem's conditions, not infinitely many scale changes or equivalent redrawings. Do not omit a valid case simply because it differs from the original paper's drawing. Do not invent extra cases forbidden by the statement.

Keep the **question diagram** faithful to the given information. Put solution-only constructions and annotations in the **solution diagram**, so the question does not reveal the solution.

Label relevant vertices, centres, lengths, angles, right angles, equal lengths, and parallel lines clearly. Distinguish given objects from auxiliary constructions with appropriate line styles. Avoid overlapping labels and misleading markings. The proof must establish the result; the sketch alone is not evidence.

### Asymptote is the standard

- Draw essentially all diagrams in **Asymptote**: geometry figures, coordinate graphs, solid-geometry sketches, grids, networks, and other mathematical visuals.
- Recreate any required figure from its mathematical information. Do not include PDF crops, screenshots, scans, copied image assets, or externally sourced pictures.
- Existing TikZ or image-based figures should be redrawn in Asymptote for this package.
- Use TikZ/PGF only in an exceptional case where an essential feature cannot reasonably be produced in Asymptote. Convenience, unfamiliarity, or an unavailable Asymptote installation is not a reason to switch. Identify the affected question and the concrete reason in your delivery message; declare the required TikZ package and libraries.
- Ordinary LaTeX remains the format for prose and equations. Asymptote is required for drawings, not for the entire solution text.
- Put the editable source of each diagram directly in its relevant `.tex` file as one `\begin{asy}...\end{asy}` environment. Use a separate environment for each sketch. A rare TikZ exception uses one `tikzpicture` environment per sketch.
- Make every diagram self-contained: include necessary imports, definitions, settings, and label-package setup within that diagram. Avoid shared `asydef` blocks and dependencies on other question records.
- Asymptote labels that use fractions must use `\dfrac`, with `amsmath` available to the diagram's label typesetting.

### Generate website previews from the diagram source

For each inline diagram in both the question and the solution, compile its **exact source** into an SVG preview. Prefer a self-contained SVG with embedded/path-based text so labels do not depend on fonts installed on the viewer's computer. A high-resolution PNG generated from the same diagram code is acceptable only when a usable SVG cannot be produced.

These previews are the only permitted image assets: they must be generated from the supplied Asymptote code (or a documented exceptional TikZ source). They are not PDF crops or replacements for editable diagram code.

Put them in `assets`, with globally unique names, for example:

- `assets/smo-2024-junior-round-1-q01-question-diagram-01.svg`
- `assets/smo-2024-junior-round-1-q01-solution-diagram-01.svg`
- `assets/smo-2024-junior-round-1-q01-solution-diagram-02.svg`

Add every preview to the existing `assets` array:

```json
{
  "path": "assets/smo-2024-junior-round-1-q01-solution-diagram-01.svg",
  "type": "image",
  "usage": "Website preview generated from diagram 1 in solution.tex; editable source remains inline in solution.tex."
}
```

Do not add an `\includegraphics` command for these website-only previews to `question.tex` or `solution.tex`; the inline diagram code remains the export source.

Add a corresponding entry to `diagram_previews`:

```json
{
  "file": "solution.tex",
  "index": 1,
  "path": "assets/smo-2024-junior-round-1-q01-solution-diagram-01.svg",
  "source_sha256": "REPLACE_WITH_THE_COMPUTED_64_CHARACTER_LOWERCASE_SHA256",
  "alt": "Triangle ABC with altitude AD and the auxiliary circle through B, C and D."
}
```

This is a structural example, not ready-to-import metadata. Replace the hash placeholder and the illustrative description with actual values.

- `file` is exactly the metadata's `question_file` or `solution_file` value.
- `index` starts at 1 in each file and counts `asy` and `tikzpicture` environments together in their order of appearance. It restarts at 1 for the other file.
- `path` must identify an included `image` asset with a `.svg` or `.png` extension.
- `alt` is a short description of the actual diagram. Do not put solution-only information in the question preview's description.
- `source_sha256` is the SHA-256 of the complete matching environment, from `\begin{asy}` through `\end{asy}`, inclusive, or the equivalent `tikzpicture` environment. Include any environment options and all internal whitespace. First normalize CRLF and CR line endings to LF, then hash UTF-8 bytes. Do not trim the environment.
- Compute hashes programmatically after the final source edits. Never invent a hash. This lets the website detect when an edit has made a preview outdated.

This Python snippet defines the exact diagram extraction and hashing convention:

```python
import hashlib
import re

normalized = tex_text.replace("\r\n", "\n").replace("\r", "\n")
pattern = r"\\begin\{(asy|tikzpicture)\}[\s\S]*?\\end\{\1\}"
for index, match in enumerate(re.finditer(pattern, normalized), start=1):
    source_sha256 = hashlib.sha256(match.group(0).encode("utf-8")).hexdigest()
    # Record index and source_sha256 for this diagram's compiled preview.
```

Do not place literal example diagram environments inside comments or verbatim blocks in the `.tex` fragments, because diagram indexing uses this extraction convention.

Compile the **diagrams** and visually inspect every generated preview for correctness, completeness, legibility, and clipped labels. Fix the source and regenerate its preview and hash when needed. You do not need to compile the complete question collection or deliver a full-document PDF. Intermediate files produced during diagram compilation need not be included in the ZIP.

If compilation is genuinely unavailable or a diagram cannot be completed, preserve the editable diagram source and report the affected IDs and missing previews. Omit the missing preview's asset and mapping entries; never claim a preview was compiled when it was not. Such a package is incomplete for full diagram display, and the website will show the source with a missing-preview notice.

Use `"assets": []` and `"diagram_previews": []` only when the record needs no supporting files/previews, or when the missing previews have been explicitly reported. Every geometry solution still requires its editable sketch source.

## 8. Final checks and delivery

Before delivering, check that:

- Every prepared question appears exactly once in the manifest.
- Every listed question has metadata, a nonempty question file, and a nonempty matching detailed solution file.
- IDs are unique and match their folder names and metadata.
- All JSON files parse successfully.
- Tags exactly match the approved list, without duplicates.
- Difficulty scores are integers from 1 to 10, with rationales.
- Every geometry solution includes its required sketches, including all distinct cases used in the reasoning and all relevant auxiliary constructions.
- Drawings use Asymptote, with any genuine TikZ exceptions identified.
- No crops, scans, screenshots, or externally sourced image assets are included.
- Every typeset mathematical fraction uses `\dfrac`, including fractions inside diagram labels.
- Dependencies needed by the sources are declared.
- Each diagram preview was generated from its supplied source and visually checked.
- Every preview mapping points to the correct file, diagram index, and included asset, with a correctly computed matching hash.
- All listed or referenced supporting files are included, with globally unique filenames.
- No placeholder metadata values, sample hashes, or unrelated intermediate build files remain.

Provide the downloadable `question_bank_import.zip` and state how many question records it contains. Briefly identify any unclassified questions, missing content, missing diagram previews, or exceptional TikZ use by question ID. Do not silently fill gaps or describe an incomplete diagram package as fully ready.

If you cannot create downloadable files in this chat, say so and provide each file's exact relative path and complete contents in separate code blocks. Do not claim to have created a ZIP unless it is actually available.
