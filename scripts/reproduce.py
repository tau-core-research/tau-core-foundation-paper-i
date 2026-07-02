#!/usr/bin/env python3
from pathlib import Path
import os
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "paperI_submission_source"


def run(cmd, cwd=ROOT):
    print("$", " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)


def compile_pdf():
    tex = SRC / "main.tex"
    env = os.environ.copy()
    env["SOURCE_DATE_EPOCH"] = "1767225600"
    if shutil_which("tectonic"):
        subprocess.run(["tectonic", "main.tex"], cwd=SRC, check=True, env=env)
    elif shutil_which("pdflatex"):
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], cwd=SRC, check=True, env=env)
        subprocess.run(["bibtex", "main"], cwd=SRC, check=False, env=env)
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], cwd=SRC, check=True, env=env)
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], cwd=SRC, check=True, env=env)
    else:
        raise SystemExit("No TeX engine found. Install tectonic or pdflatex.")
    if not (SRC / "main.pdf").exists():
        raise SystemExit("PDF build failed: main.pdf missing")


def shutil_which(name):
    from shutil import which

    return which(name)


def main():
    run([sys.executable, "scripts/build_figures.py"])
    compile_pdf()
    run([sys.executable, "scripts/build_arxiv_source.py"])
    run([sys.executable, "-m", "pytest", "-q"])
    print("FOUNDATION_PAPER_I_REPRODUCTION_COMPLETE")


if __name__ == "__main__":
    main()
