#!/usr/bin/env python3
"""The Dog Reviews the Mailman — make.fun bounty entry.

Writes one funny one-line review a dog gives the mailman to /output/entry.txt:
two stars — great smells, zero belly rubs — but the biscuit bribe keeps him employed.
"""

import os

ENTRY = 'Two stars: great smells, zero belly rubs, and he RUNS when I offer my favourite stick \u2014 still, the biscuit bribe keeps him employed.'


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
