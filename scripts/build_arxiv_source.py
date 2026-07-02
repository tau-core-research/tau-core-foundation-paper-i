#!/usr/bin/env python3
from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "paperI_submission_source"
OUT = ROOT / "arxiv_submission_source.zip"


def main():
    if OUT.exists():
        OUT.unlink()
    files = []
    for path in SRC.rglob("*"):
        if path.is_file():
            if path.suffix in {".aux", ".bbl", ".blg", ".log", ".out", ".toc"}:
                continue
            if path.name == "main.pdf":
                continue
            files.append(path)
    with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(files):
            info = zipfile.ZipInfo(str(path.relative_to(SRC)))
            info.date_time = (2026, 1, 1, 0, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, path.read_bytes())
    print(f"WROTE {OUT}")


if __name__ == "__main__":
    main()
