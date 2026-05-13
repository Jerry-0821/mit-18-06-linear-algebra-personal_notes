from __future__ import annotations

import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTES_TEX = PROJECT_ROOT / "notes-tex"
NOTES_PDF = PROJECT_ROOT / "notes-pdf"
BUILD_ONE = PROJECT_ROOT / "scripts" / "build_exam_note.py"


def main() -> None:
    tex_files = sorted(NOTES_TEX.glob("*.tex"))
    if not tex_files:
        raise SystemExit("No .tex files found in notes-tex.")

    for tex_path in tex_files:
        pdf_path = NOTES_PDF / f"{tex_path.stem}.pdf"
        print(f"Building {pdf_path.relative_to(PROJECT_ROOT).as_posix()}")
        subprocess.run(
            [sys.executable, str(BUILD_ONE), str(tex_path), str(pdf_path)],
            cwd=PROJECT_ROOT,
            check=True,
        )


if __name__ == "__main__":
    main()
