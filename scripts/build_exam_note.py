from __future__ import annotations

import argparse
import os
import shutil
import subprocess
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEX = PROJECT_ROOT / "notes-tex" / "03-02-03-03-nullspace-special-solutions-complete-solution.tex"
DEFAULT_PDF = PROJECT_ROOT / "notes-pdf" / "03-02-03-03-nullspace-special-solutions-complete-solution.pdf"
BUNDLED_TECTONIC = Path.home() / ".codex" / ".tmp" / "bundled-marketplaces" / "openai-bundled" / "plugins" / "latex-tectonic" / "bin" / "tectonic.exe"


def find_tectonic() -> str:
    env_path = os.environ.get("TECTONIC")
    if env_path and Path(env_path).exists():
        return env_path
    path_tool = shutil.which("tectonic")
    if path_tool:
        return path_tool
    if BUNDLED_TECTONIC.exists():
        return str(BUNDLED_TECTONIC)
    raise SystemExit(
        "Could not find tectonic. Install Tectonic or set the TECTONIC environment variable."
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a MIT 18.06 exam-note PDF with real LaTeX math.")
    parser.add_argument("tex", nargs="?", default=str(DEFAULT_TEX), help="LaTeX source file")
    parser.add_argument("pdf", nargs="?", default=str(DEFAULT_PDF), help="Output PDF file")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    tex_path = Path(args.tex)
    pdf_path = Path(args.pdf)
    if not tex_path.is_absolute():
        tex_path = PROJECT_ROOT / tex_path
    if not pdf_path.is_absolute():
        pdf_path = PROJECT_ROOT / pdf_path

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    tectonic = find_tectonic()

    command = [
        tectonic,
        str(tex_path),
        "--outdir",
        str(pdf_path.parent),
    ]
    subprocess.run(command, cwd=PROJECT_ROOT, check=True)

    generated = pdf_path.parent / f"{tex_path.stem}.pdf"
    if generated.resolve() != pdf_path.resolve():
        if pdf_path.exists():
            pdf_path.unlink()
        generated.replace(pdf_path)

    try:
        display_path = pdf_path.resolve().relative_to(PROJECT_ROOT)
    except ValueError:
        display_path = pdf_path
    print(display_path.as_posix())


if __name__ == "__main__":
    main()
