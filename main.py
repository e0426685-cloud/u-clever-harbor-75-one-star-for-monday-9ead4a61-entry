#!/usr/bin/env python3
"""One Star for Monday.

Writes a single-line, one-star review of Monday — written as though
Monday were a restaurant — to /output/entry.txt.

Rules enforced here, matching the bounty gate:
  * the entry is one line of plain UTF-8 text
  * 1 to 180 characters
  * at most 25 words
"""

import os

ENTRY = (
    "One star. Waited an hour for a table, the waiter never came, and "
    "the Monday special was Friday's leftovers, somehow worse. "
    "See you next week."
)

MAX_CHARS = 180
MAX_WORDS = 25


def validate(line):
    """Check the entry against the bounty gate; raise SystemExit if bad."""
    if not line.strip():
        raise SystemExit("entry is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    words = line.split()
    if len(words) > MAX_WORDS:
        raise SystemExit(
            "entry is %d words, over the %d limit" % (len(words), MAX_WORDS)
        )
    return line


def main():
    line = validate(ENTRY.strip())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Plain open() on purpose: tempfile.mkstemp forces mode 0600, and a
    # grader running as a different user could not read the file.
    # No trailing newline: the file is exactly the one review line, so its
    # byte count is the line's character count.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
