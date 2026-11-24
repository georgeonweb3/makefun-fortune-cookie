#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers - make.fun entry.

Writes one original line of fortune-cookie wisdom to /output/entry.txt.
Python stdlib only, deterministic, no network access.
"""

import os

FORTUNE = "Your legacy code was once someone's clever shortcut, and your clever shortcut is someone's legacy code."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    # Read back and verify the exact output: no trailing newline,
    # 1-120 characters, and byte-identical to the fortune above.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == FORTUNE, "entry.txt does not match the fortune"
    assert 1 <= len(written) <= 120, "entry.txt outside the 1-120 character gate"


if __name__ == "__main__":
    main()
