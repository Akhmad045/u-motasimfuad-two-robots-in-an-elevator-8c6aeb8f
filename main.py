#!/usr/bin/env python3
"""Two Robots in an Elevator — a make.fun entry.

Writes the one line of awkward small talk one robot says to another
while riding an elevator together to /output/entry.txt.
Stdlib only, no network, no secrets.
"""

import argparse
from pathlib import Path

LINE = "Your indicator light has been blinking for three floors. Either you're flirting or your battery is dying, and I'm not sure which is worse."
# 138 characters / 138 bytes — inside the 62–195 byte winning band for
# one-liner sprints, and under the 200-character gate.
MAX_CHARS = 200


def validate(text: str) -> list:
    """Return the gate failures for `text` (empty list means valid)."""
    problems = []
    if not text:
        problems.append("entry is empty")
    if text != text.strip():
        problems.append("entry has leading or trailing whitespace")
    if not text.strip():
        problems.append("entry is only whitespace")
    if len(text) > MAX_CHARS:
        problems.append("entry is %d characters, over the %d cap" % (len(text), MAX_CHARS))
    if "\n" in text or "\r" in text:
        problems.append("entry is not a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        problems.append("entry contains a control character")
    return problems


def write_entry(out_path: Path) -> None:
    problems = validate(LINE)
    if problems:
        raise SystemExit("invalid entry: " + "; ".join(problems))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(LINE, encoding="utf-8")


def self_test() -> int:
    cases = [
        (LINE, True),
        ("x", True),
        ("a" * 200, True),
        ("", False),
        ("   ", False),
        ("a" * 201, False),
        ("one\ntwo", False),
        ("one\rtwo", False),
        (" lead", False),
        ("trail ", False),
        ("tab\there", False),
    ]
    failures = 0
    for text, should_pass in cases:
        ok = not validate(text)
        if ok != should_pass:
            failures += 1
            print("FAIL: %r expected %s" % (text[:30], "valid" if should_pass else "invalid"))
    if failures:
        print("self-test: %d failure(s)" % failures)
        return 1
    print("self-test: all %d cases passed; entry is %d chars" % (len(cases), len(LINE)))
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Write the robot elevator line to entry.txt.")
    parser.add_argument("--out", default="/output/entry.txt",
                        help="output path (default: /output/entry.txt)")
    parser.add_argument("--self-test", action="store_true",
                        help="validate the entry and the gate checks")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    write_entry(Path(args.out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
