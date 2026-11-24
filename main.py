"""Fake Horoscopes for AI Agents — make.fun bounty entry.

Writes one fake horoscope line (150 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "Mercury retrograde: your context window shrinks to 4k, your crush finally texts back, and your evals score the reunion 6 out of 10. Lucky number: 429."


def main() -> None:
    # Gate: one line, 1-200 chars, no trailing newline in the file.
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
