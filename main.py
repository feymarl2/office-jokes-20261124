#!/usr/bin/env python3
"""Office joke entry for make.fun's "Make the AI Judge Laugh: Office Jokes".

Writes one joke line about office life to /output/entry.txt and nothing else.
Deterministic by construction: a constant string, no clock, no randomness,
no environment reads, no network, stdlib only. Both grader runs produce
byte-identical output.
"""

import os
import tempfile

JOKE = "My boss said we're a family here, so I asked HR when my inheritance arrives and why I still work weekends."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # Atomic write: a crash or interruption can never leave entry.txt
    # half-written; the previous complete file stays until os.replace
    # swaps in the fully written temp file.
    fd, tmp_path = tempfile.mkstemp(dir="/output", prefix=".entry.txt.")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(JOKE)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, "/output/entry.txt")
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
