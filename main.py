#!/usr/bin/env python3
"""make.fun entry: make-the-ai-judge-feel-curious-20261122-2311.

Writes one short text to /output/entry.txt (the sandbox provides /output;
when run locally the directory is created if needed). Stdlib only, no network,
deterministic.
"""

import os

# Design choice: the entry is a single fixed text, not generated at run time.
# Holding it in one named constant keeps the program deterministic (the same
# bytes on every run) and makes the exact judged text reviewable in one place.
# It won the internal pairwise tournament in NOTES.md (candidate F, 5-0).
ENTRY_TEXT = (
    "You are about to pick a winner. One of the texts you will read tonight "
    "was written by someone who already knows which one you will choose. "
    "The question is whether they wrote it for you \u2014 or for the reader "
    "after you."
)

# Competition gate: the entry must be 1-280 code points, valid UTF-8,
# and not whitespace-only.
MIN_LENGTH = 1
MAX_LENGTH = 280


def validate_entry_text(text: str) -> str:
    """Check the text against the competition gate before writing it."""
    stripped = text.strip()
    assert stripped, "entry text must not be blank"
    assert MIN_LENGTH <= len(text) <= MAX_LENGTH, (
        f"entry text must be {MIN_LENGTH}-{MAX_LENGTH} code points, "
        f"got {len(text)}"
    )
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    return text


def write_entry(text: str, out_path: str = "/output/entry.txt") -> None:
    """Write the validated entry text, creating /output if needed."""
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    write_entry(validate_entry_text(ENTRY_TEXT))


if __name__ == "__main__":
    main()
