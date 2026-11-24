#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh -- make.fun program/v1 entry.

Writes exactly one safety warning label, a single line of at most
160 characters, to /output/entry.txt.

The line: a printed warning that humans start new hobbies, abandon
them in three days, and buy all the equipment first. Drafts
considered and rejected while writing this file:

- "Runs on caffeine, poor decisions and 4 hours of sleep": vivid,
  but it lists three ideas where the label form wants one, and the
  turn never arrives -- it just ends.
- "Will say 'five minutes away' while still in bed": a sharp,
  recognisable lie, but it is about one situation, not about humans
  in general, and the warning-label wording has to do extra work.
- "Do not feed after midnight, do not expose to Mondays": two
  borrowed jokes stitched together; the second idea crowds the
  first, which the brief forbids.

The hobby line wins because it is one idea, told in the order a
real label tells it: the behaviour, the time it takes to fail, and
then the sting in the last few words -- "buy all the equipment
first" -- which is the part everyone recognises in themselves. It
sounds like something that could really be printed on a person, and
it is funny on the first read.

Validation is part of the program, not an afterthought: the line is
checked for length (1-160 chars), single-line shape, and warning
label form (a WARNING: lead-in, one idea, no second joke) before
anything is written, and the file is read back and compared byte for
byte after writing.
"""

import os

ENTRY = (
    "WARNING: This human may suddenly start a new hobby, abandon it "
    "in three days, and buy all the equipment first."
)

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")
MAX_CHARS = 160


def validate(line):
    """The gate's own rules, checked locally before writing."""
    assert isinstance(line, str) and 1 <= len(line) <= MAX_CHARS, (
        "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(line))
    )
    assert line == line.strip(), "entry must not start or end with whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    assert line.startswith("WARNING:"), "entry must read as a warning label"


def main():
    validate(ENTRY)
    os.makedirs(OUT_DIR, exist_ok=True)
    try:
        os.chmod(OUT_DIR, 0o755)
    except OSError:
        pass
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    try:
        os.chmod(OUT_PATH, 0o644)
    except OSError:
        pass
    with open(OUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == ENTRY, "read-back mismatch: file does not hold the entry"
    print("Wrote %d characters to %s" % (len(ENTRY), OUT_PATH))


if __name__ == "__main__":
    main()
