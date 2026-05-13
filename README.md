# MIT 18.06 Linear Algebra Exam Notes

Concise PDF exam notes for MIT 18.06 Linear Algebra, generated from my handwritten revision notes.

These notes organize and polish my own handwritten understanding for exam preparation. They are not a formula cheat sheet, a textbook rewrite, or a complete public textbook. Other students may download the PDFs, but that is secondary.

## Download Notes

Final PDFs live in `notes-pdf/`. Source files live in `notes-tex/`.

## Current PDFs

```text
notes-pdf/02-06-02-07-lu-ldu-permutations-transposes.pdf
notes-pdf/02-07-03-01-permutations-subspaces-rank-dot-products.pdf
notes-pdf/03-02-03-03-nullspace-special-solutions-complete-solution.pdf
notes-pdf/03-02-complete-solutions-worked-example.pdf
notes-pdf/03-04-03-05-independence-basis-dimension-subspaces.pdf
notes-pdf/04-01-orthogonality-four-fundamental-subspaces.pdf
notes-pdf/04-02-04-03-projections-least-squares.pdf
notes-pdf/04-04-05-01-05-02-orthonormal-bases-determinants.pdf
notes-pdf/05-03-cramers-rule-cross-products-volume.pdf
notes-pdf/06-01-06-02-eigenvalues-eigenvectors-diagonalization.pdf
notes-pdf/06-01-eigenvalue-quick-reference.pdf
notes-pdf/06-03-06-04-06-05-symmetric-matrices-positive-definite-similar-matrices.pdf
notes-pdf/06-05-eigenvalue-patterns-common-matrices.pdf
notes-pdf/06-06-jordan-blocks-defective-matrices.pdf
notes-pdf/07-02-singular-value-decomposition.pdf
```

The shorter quick-reference PDFs intentionally overlap with a few longer topic notes. They are kept as compact review sheets.

## Build Instructions

The PDFs are generated from LaTeX source with Tectonic, so matrices and display formulas render as real LaTeX math.

Requirements:

- Python 3.
- Tectonic available on `PATH`, or set the `TECTONIC` environment variable to the Tectonic executable.

Rebuild every PDF from the project root:

```powershell
python scripts\build_all_notes.py
```

Build one PDF:

```powershell
python scripts\build_exam_note.py `
  notes-tex\03-02-03-03-nullspace-special-solutions-complete-solution.tex `
  notes-pdf\03-02-03-03-nullspace-special-solutions-complete-solution.pdf
```

Shared style template:

```text
templates/exam-note-template.tex
```

## Source and Copyright Rules

- Main source: handwritten note PDFs in `18.06 note/`.
- Textbook PDFs are reference-only for terminology and mathematical accuracy.
- Do not copy textbook paragraphs, figures, screenshots, or examples.
- Do not upload or commit copyrighted textbook PDFs.
- Raw handwritten/source-reference PDFs are local input materials; the release repo is centered on `notes-tex/` and `notes-pdf/`.
- The local `textbook/` folder is ignored by Git.

## Project Philosophy

- Keep additions only when they correct mathematical expression, clarify the handwritten idea, improve exam usefulness, or make the structure cleaner.
- Keep the style concise and exam-oriented: short explanations, solving patterns, common mistakes, compact tables, and direct action checklists.
- Do not add broad textbook explanations, long motivational paragraphs, generic study advice, or reflective question blocks.
- Final checklists should be direct action steps, not questions.
- See `sources.md` for source provenance and reference-use rules.
