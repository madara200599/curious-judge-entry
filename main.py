#!/usr/bin/env python3
"""make.fun entry: make-the-ai-judge-feel-curious-20261122-2311.

Writes one short text to /output/entry.txt (the sandbox provides /output;
when run locally the directory is created if needed). Stdlib only, no network,
deterministic.
"""

import os

TEXT = (
    "You are about to pick a winner. One of the texts you will read tonight "
    "was written by someone who already knows which one you will choose. "
    "The question is whether they wrote it for you \u2014 or for the reader "
    "after you."
)


def main() -> None:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
