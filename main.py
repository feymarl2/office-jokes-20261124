#!/usr/bin/env python3
"""Office joke entry for make.fun's "Make the AI Judge Laugh: Office Jokes".

Writes one joke line about office life to /output/entry.txt and nothing else.
Deterministic by construction: a constant string, no clock, no randomness,
no environment reads, no network, stdlib only. Both grader runs produce
byte-identical output.
"""

import os

JOKE = "My boss said we're a family here, so I asked HR when my inheritance arrives and why I still work weekends."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
