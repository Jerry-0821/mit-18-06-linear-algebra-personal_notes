# MIT 18.06 Linear Algebra Exam Notes

Concise PDF exam notes for MIT 18.06 Linear Algebra, generated from my handwritten revision notes.

These notes organize and polish my own handwritten understanding for exam preparation. They are not a formula cheat sheet, a textbook rewrite, or a complete public textbook. Other students may download the PDFs, but that is secondary.

## Download Notes

The final download is one combined PDF: [mit-18-06-linear-algebra-exam-notes.pdf](notes-pdf/mit-18-06-linear-algebra-exam-notes.pdf).

Source files live in `notes-tex/`.

## Contents

```text
2.6-2.7  LU, LDU, Permutations, and Transposes
2.7-3.1  Permutations, Subspaces, Rank, and Dot Products
3.2-3.3  Nullspace, Special Solutions, and Complete Solutions
3.2      Complete Solutions Worked Example
3.4-3.5  Independence, Basis, Dimension, and Subspaces
4.1      Orthogonality and the Four Fundamental Subspaces
4.2-4.3  Projections and Least Squares
4.4-5.2  Orthonormal Bases, QR, and Determinants
5.3      Inverses, Cramer's Rule, Cross Products, and Volume
6.1-6.2  Eigenvalues, Eigenvectors, and Diagonalization
6.1      Eigenvalue Quick Reference
6.3-6.5  Matrix Exponentials, Symmetric Matrices, and Positive Definiteness
6.5      Eigenvalue Patterns for Common Matrix Types
6.6      Jordan Blocks and Defective Matrices
7.2      Singular Value Decomposition
```

The shorter quick-reference notes intentionally overlap with a few longer topic notes. They are included as compact review sections in the combined PDF.

## Build Instructions

The PDFs are generated from LaTeX source with Tectonic, so matrices and display formulas render as real LaTeX math.

Requirements:

- Python 3.
- Tectonic available on `PATH`, or set the `TECTONIC` environment variable to the Tectonic executable.
- Python package `pypdf` for merging section PDFs.

Rebuild the combined PDF from the project root:

```powershell
python scripts\build_all_notes.py
```

The script builds temporary section PDFs in `.build/section-pdfs/`, then merges them into `notes-pdf/mit-18-06-linear-algebra-exam-notes.pdf`.

Build one section PDF manually:

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
