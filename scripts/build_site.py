#!/usr/bin/env python3
"""Assemble and build the MkDocs handbook site.

GitHub wants README.md, CONTRIBUTING.md, and friends at the repository root;
MkDocs wants every page under one ``docs_dir``. Rather than move or duplicate
files in git, this script copies the curriculum into a generated, git-ignored
``site-src/`` folder (preserving the layout so relative links keep working),
then hands off to MkDocs.

Usage:
    python scripts/build_site.py            # just sync site-src/
    python scripts/build_site.py serve      # sync, then `mkdocs serve`
    python scripts/build_site.py build      # sync, then `mkdocs build`
    python scripts/build_site.py gh-deploy --force   # sync, then deploy

Any arguments are passed straight through to ``mkdocs``.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SITE_SRC = REPO / "site-src"

# Curriculum files/dirs copied into the site, relative to the repo root.
# The destination path mirrors the source so existing relative links resolve.
INCLUDE = [
    "README.md",
    "SCHEDULE.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "sessions",
]


def sync() -> None:
    """Rebuild site-src/ from the curriculum sources."""
    if SITE_SRC.exists():
        shutil.rmtree(SITE_SRC)
    SITE_SRC.mkdir(parents=True)
    for rel in INCLUDE:
        src = REPO / rel
        dst = SITE_SRC / rel
        if src.is_dir():
            shutil.copytree(src, dst)
        elif src.is_file():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        else:
            raise SystemExit(f"Expected to copy {src}, but it does not exist.")
    print(f"Synced {len(INCLUDE)} entries into {SITE_SRC.relative_to(REPO)}/")


def main(argv: list[str]) -> int:
    sync()
    if not argv:
        return 0
    # Pass remaining args through to mkdocs (serve, build, gh-deploy, ...).
    return subprocess.call([sys.executable, "-m", "mkdocs", *argv], cwd=REPO)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
