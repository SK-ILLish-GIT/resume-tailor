#!/usr/bin/env python3
"""Print the output PDF path for a variant slug (used by Makefile)."""

from __future__ import annotations

import argparse
import sys

from pdf_names import resolve_pdf_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Resolve output PDF path for a slug")
    parser.add_argument("slug", help="Variant slug or 'master'")
    args = parser.parse_args()
    try:
        print(resolve_pdf_path(args.slug))
    except (FileNotFoundError, ValueError) as exc:
        print(exc, file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
