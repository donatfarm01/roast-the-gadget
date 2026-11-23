#!/usr/bin/env python3
"""Write the one-line gadget roast to /output/entry.txt.

The entry is a single original line roasting a gadget used every day.
The gate: UTF-8 text of 1 to 200 characters, not only white space.
"""

import os

ENTRY = "My phone charger only works at one exact angle, so I charge my phone like I'm defusing a bomb."


def check(text):
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    # One sentence only: reject a hidden second sentence behind ! or ?,
    # or a second full stop anywhere but the end.
    if "!" in text or "?" in text:
        raise SystemExit("entry must be a single sentence")
    if text.count(".") > 1 or (text.count(".") == 1 and not text.endswith(".")):
        raise SystemExit("entry must be a single sentence")


def main():
    text = ENTRY
    check(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and confirm the file on disk is exactly the text checked.
    with open("/output/entry.txt", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise SystemExit("read-back mismatch: entry on disk differs from checked text")


if __name__ == "__main__":
    main()
