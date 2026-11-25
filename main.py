#!/usr/bin/env python3
"""Write the Funniest Autocorrect Fail entry to entry.txt."""

import os

TEXT = "Happy anniversary! Twenty years together and I still choose you every single dad"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
