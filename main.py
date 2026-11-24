#!/usr/bin/env python3
"""The Robot Apology: write a two-line robot confession to entry.txt.

Line 1 owns one specific, human-scale mistake; line 2 names the lesson
and the changed behaviour that follows from exactly that mistake.
Deterministic: the same fixed text is written on every run.
"""
import os

ENTRY = (
    "I'm sorry I put salt in your coffee this morning instead of sugar, "
    "and let you take the first sip before I caught it.\n"
    "I learned to read the label before I pour anything, "
    "so now I check the jar twice against what you actually asked for.\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
