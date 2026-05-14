from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from pypdf import PdfWriter


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTES_TEX = PROJECT_ROOT / "notes-tex"
NOTES_PDF = PROJECT_ROOT / "notes-pdf"
BUILD_ONE = PROJECT_ROOT / "scripts" / "build_exam_note.py"
SECTION_PDF_DIR = PROJECT_ROOT / ".build" / "section-pdfs"
FINAL_PDF = NOTES_PDF / "mit-18-06-linear-algebra-exam-notes.pdf"


def merge_pdfs(pdf_paths: list[Path], output_path: Path) -> None:
    writer = PdfWriter()
    for pdf_path in pdf_paths:
        writer.append(str(pdf_path))

    writer.add_metadata(
        {
            "/Title": "MIT 18.06 Linear Algebra Exam Notes",
            "/Subject": "Combined exam revision notes generated from handwritten MIT 18.06 notes",
        }
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("wb") as output_file:
        writer.write(output_file)


def main() -> None:
    tex_files = sorted(NOTES_TEX.glob("*.tex"))
    if not tex_files:
        raise SystemExit("No .tex files found in notes-tex.")

    if SECTION_PDF_DIR.exists():
        shutil.rmtree(SECTION_PDF_DIR)
    SECTION_PDF_DIR.mkdir(parents=True, exist_ok=True)

    section_pdfs: list[Path] = []
    for tex_path in tex_files:
        pdf_path = SECTION_PDF_DIR / f"{tex_path.stem}.pdf"
        print(f"Building {pdf_path.relative_to(PROJECT_ROOT).as_posix()}")
        subprocess.run(
            [sys.executable, str(BUILD_ONE), str(tex_path), str(pdf_path)],
            cwd=PROJECT_ROOT,
            check=True,
        )
        section_pdfs.append(pdf_path)

    merge_pdfs(section_pdfs, FINAL_PDF)
    print(FINAL_PDF.relative_to(PROJECT_ROOT).as_posix())


if __name__ == "__main__":
    main()
