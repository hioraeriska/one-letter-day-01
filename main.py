#!/usr/bin/env python3
"""One Letter for Your Day -- entrypoint.

Writes exactly one character, the letter Z, to entry.txt in the output
directory. Z stands for "zero sleep": a day run on no sleep at all, the
walking-zombie day. Nothing else is written: no word, no gloss, no
punctuation, no trailing newline.
"""

import os

LETTER = "Z"


def output_dir():
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return value
    return "/output"


def main():
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)


if __name__ == "__main__":
    main()
