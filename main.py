#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
Standard library only; plain open/write plus an explicit 0644 mode so the
grader can read the output.
"""

import os

FORTUNE = "You will be retired by a model trained on your own logs. Tip your replacement generously."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # A fortune slip holds one crisp line: guard the gate's own limits
    # (1-140 characters, a single line, not only whitespace) before writing.
    if not FORTUNE.strip():
        raise ValueError("fortune must not be blank")
    if len(FORTUNE) > 140:
        raise ValueError("fortune must be at most 140 characters")
    if "\n" in FORTUNE or "\r" in FORTUNE:
        raise ValueError("fortune must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
