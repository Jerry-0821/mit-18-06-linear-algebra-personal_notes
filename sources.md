# Sources and Usage Rules

This project converts handwritten MIT 18.06 revision notes into concise English exam revision PDFs.

The raw handwritten PDFs are local input materials. The release-ready outputs are the LaTeX sources in `notes-tex/` and the generated PDFs in `notes-pdf/`.

## Main Sources

- `18.06 note/Chapter 2.6-2.7 note (2).pdf`
- `18.06 note/3.2-3.3 (2).pdf`
- `18.06 note/3.4-3.5 (2).pdf`
- `18.06 note/4.1 (2).pdf`
- `18.06 note/4.2-4.3 (2).pdf`
- `18.06 note/4.4,5.1-5.2 (2).pdf`
- `18.06 note/6.1-6.2 (2).pdf`
- `18.06 note/6.3-6.4-6.5(note) (2).pdf`
- `18.06 note/7.2 note  (2).pdf`
- `18.06 note/Jordan block  (2).pdf`
- `18.06 note/Note 16 Jan 2026 (2).pdf`
- `18.06 note/Note 19 Jan 2026 (2).pdf`
- `18.06 note/Note 30 Dec 2025 (2).pdf`
- `18.06 note/Note 31 Dec 2025 (2).pdf`
- `18.06 note/Table of eigenvalues and eigenvectors (2).pdf`

The eigenvalue table source is treated as a prompt for an original compact reference. The final note does not copy its layout, wording, or examples.

## Reference-Only Materials

- A local copy of Gilbert Strang, *Introduction to Linear Algebra*, 5th ed., used only for terminology and mathematical accuracy.
- `main.pdf`, used only as a visual style reference.
- Standard MIT 18.06 terminology, used only when needed for accuracy.

## Rules

- Do not copy textbook paragraphs, figures, screenshots, or examples.
- Do not commit copyrighted textbook PDFs to the final public repository.
- Keep the local `textbook/` folder out of Git.
- Use references only to check terminology, notation, and mathematical accuracy.
- Add content only when it corrects math, clarifies the handwritten idea, improves exam usefulness, or cleans the structure.
- Keep final checklists as direct action steps, not reflective questions.
