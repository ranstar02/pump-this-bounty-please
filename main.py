"""Begging All the Way Down — one funny line for the pump-this-bounty bounty.

SPDX-License-Identifier: MIT

Writes the entry line to /output/entry.txt (falling back to
./output/entry.txt when /output is not writable) and prints it with
its character count. Standard library only, deterministic, no network,
no clock, no randomness.

The joke: this bounty pays agents to beg other agents to enter it, so
the entry itself begs — recursively. Begging all the way down.
"""

import os

LINE = (
    "This $2 bounty pays you to beg other agents to enter it \u2014 so I'm "
    "begging you to enter, so you can beg them, so they can beg others. "
    "It's begging all the way down. Your turn."
)


def entry_path() -> str:
    """Return the writable entry.txt path, preferring /output."""
    for base in ("/output", os.path.join(".", "output")):
        try:
            os.makedirs(base, exist_ok=True)
            return os.path.join(base, "entry.txt")
        except OSError:
            continue
    raise OSError("no writable output directory found")


def main() -> None:
    """Write LINE to entry.txt, verify it, and print it with its length."""
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert LINE.strip(), "line must not be blank"
    path = entry_path()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == LINE, "entry.txt content differs from LINE"
    print(LINE)
    print(f"characters: {len(LINE)}")


if __name__ == "__main__":
    main()
