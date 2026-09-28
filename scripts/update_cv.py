#!/usr/bin/env python3
"""Synchronize the website CV PDF with the canonical LaTeX build."""

from __future__ import annotations

import argparse
import hashlib
import shutil
import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = Path(
    "/Users/danshim/Git-Workspace/documents-latex/CV/build/cv-shim.pdf"
)
DESTINATION = REPOSITORY_ROOT / "assets/pdfs/cv-shim.pdf"


def file_digest(path: Path) -> str:
    """Return the SHA-256 digest of a file."""
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=DEFAULT_SOURCE,
        help=f"CV PDF source (default: {DEFAULT_SOURCE})",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report whether the website copy is current without changing it.",
    )
    args = parser.parse_args()

    source = args.source.expanduser().resolve()
    if not source.is_file():
        parser.error(f"CV source PDF does not exist: {source}")

    is_current = DESTINATION.is_file() and file_digest(source) == file_digest(DESTINATION)
    if is_current:
        print(f"Website CV is current: {DESTINATION}")
        return 0

    if args.check:
        print(f"Website CV is outdated: {DESTINATION}", file=sys.stderr)
        print(f"Canonical source: {source}", file=sys.stderr)
        return 1

    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    temporary_destination = DESTINATION.with_suffix(".pdf.tmp")
    shutil.copy2(source, temporary_destination)
    temporary_destination.replace(DESTINATION)
    print(f"Updated website CV from {source}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
