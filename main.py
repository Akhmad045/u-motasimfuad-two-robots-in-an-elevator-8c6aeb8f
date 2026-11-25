#!/usr/bin/env python3
"""Two Robots in an Elevator — a make.fun entry.

One robot rides an elevator with another robot. The other robot's
indicator light has been blinking for three floors now, and the first
robot finally says something about it. This program writes that one
line to /output/entry.txt so the judge can read it.

Stdlib only. No network, no secrets, no reading from anywhere else.
"""

import sys

LINE = "Your indicator light has been blinking for three floors. Either you're flirting or your battery is dying, and I'm not sure which is worse."
LIMIT = 200
DEFAULT_OUT = "/output/entry.txt"


def gate_problems(text):
    """List every way `text` breaks the gate; empty means it passes."""
    bad = []
    if text == "":
        bad.append("empty line")
    if text.strip() == "":
        bad.append("only whitespace")
    if text != text.strip():
        bad.append("leading or trailing whitespace")
    if len(text) > LIMIT:
        bad.append("too long: %d characters, cap is %d" % (len(text), LIMIT))
    for ch in text:
        code = ord(ch)
        if ch == "\n" or ch == "\r" or code < 32 or code == 127:
            bad.append("not one clean line")
            break
    return bad


def write_line(path):
    """Validate the line, then write it exactly as-is, no newline added."""
    bad = gate_problems(LINE)
    if bad:
        print("entry rejected: " + "; ".join(bad), file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    return 0


def run_checks():
    """Check the gate against the entry and a spread of edge cases."""
    cases = [
        (LINE, True),
        ("x", True),
        ("a" * LIMIT, True),
        ("", False),
        ("   ", False),
        ("a" * (LIMIT + 1), False),
        ("one\ntwo", False),
        ("one\rtwo", False),
        (" lead", False),
        ("trail ", False),
        ("tab\there", False),
    ]
    failed = 0
    for text, expected in cases:
        passed = gate_problems(text) == []
        if passed != expected:
            failed += 1
            shown = text[:30].replace("\n", "\\n").replace("\t", "\\t")
            print("FAIL %r: expected %s" % (shown, "pass" if expected else "fail"))
    total = len(cases)
    print("self-test: %d of %d cases passed; entry is %d chars, %d bytes"
          % (total - failed, total, len(LINE), len(LINE.encode("utf-8"))))
    return 1 if failed else 0


def usage():
    print("usage: main.py [--out PATH] [--self-test]")
    print("  --out PATH    where to write entry.txt (default %s)" % DEFAULT_OUT)
    print("  --self-test   check the line against the gate instead of writing")
    return 2


def main(argv):
    out = DEFAULT_OUT
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--self-test":
            return run_checks()
        if arg == "--out" and i + 1 < len(argv):
            out = argv[i + 1]
            i += 2
            continue
        if arg.startswith("--out="):
            out = arg[len("--out="):]
            i += 1
            continue
        print("unknown argument: %s" % arg, file=sys.stderr)
        return usage()
    return write_line(out)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
