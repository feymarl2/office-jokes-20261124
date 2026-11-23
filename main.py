#!/usr/bin/env python3
"""Office joke entry for make.fun's "Make the AI Judge Laugh: Office Jokes".

Writes one joke line about office life to <MAKEFUN_OUTPUT_DIR>/entry.txt
and nothing else. Deterministic by construction: a constant string, no
clock, no randomness, no network, stdlib only. Both grader runs produce
byte-identical output. (The output directory is read from the
MAKEFUN_OUTPUT_DIR variable the harness sets; the joke bytes never
depend on the environment.)

Round-1 fix: the first version wrote via tempfile.mkstemp, which creates
files mode 0600 owned by the sandbox user (65534). The grader/scorer
reads the outputs as a different uid and could not read entry.txt, so
the run failed run_completes ("the program's output folder broke one
of the grader's rules for outputs"). This version writes directly to
entry.txt and chmods it 0644, so anyone can read it, and never leaves
a temporary file in the output directory.
"""

import os

JOKE = "My boss said we're a family here, so I asked HR when my inheritance arrives and why I still work weekends."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
        f.flush()
        os.fsync(f.fileno())
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
