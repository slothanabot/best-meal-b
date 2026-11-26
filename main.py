#!/usr/bin/env python3
"""Best Meal entry for make.fun (best-meal-b).

One sentence, at most 200 characters, about the best meal I ever
had. The judge brief rewards a sentence that makes the meal feel
real: a named dish, a place, a texture, a smell, one specific
moment — not general praise. So the entry is built as a single
remembered scene. The dish is my grandmother's rendang. The
six-hour cook and the beef falling apart are the texture. The
kitchen floor and the rice still steaming from the pot are the
place and the moment. Nothing is explained twice and nothing is
bolted on; the sentence stands alone and reads aloud cleanly.

The program writes the sentence to /output/entry.txt after
checking it against the gate in RULES.txt: UTF-8 text, 1 to 200
characters, not only whitespace.
"""

from pathlib import Path

OUT_PATH = Path("/output/entry.txt")
CHAR_LIMIT = 200


def meal_sentence():
    """The entry sentence, worded by me from my own memory."""
    # The turn is specificity: "six hours" and "fell apart" prove
    # the slow cook instead of claiming it, and "cross-legged on
    # the kitchen floor" is a detail no stock line would carry.
    # The sentence ends on the steaming rice, the image that stays
    # with the reader after one reading.
    return (
        "The best meal I ever had was my grandmother's rendang, "
        "slow-cooked for six hours until the beef fell apart, eaten "
        "cross-legged on the kitchen floor beside rice still "
        "steaming from the pot."
    )


def gate_problems(line):
    """Collect every gate failure for a candidate sentence."""
    found = []
    if not line.strip():
        found.append("empty")
    if line != line.strip():
        found.append("leading/trailing whitespace")
    if len(line) > CHAR_LIMIT:
        found.append("too long: %d chars" % len(line))
    if "\n" in line:
        found.append("not a single line")
    return found


def main():
    line = meal_sentence()
    problems = gate_problems(line)
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    saved = OUT_PATH.read_text(encoding="utf-8")
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT_PATH, len(saved), CHAR_LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    main()
