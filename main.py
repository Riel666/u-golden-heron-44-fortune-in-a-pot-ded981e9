"""One kind, funny fortune for a houseplant, 120 characters or fewer.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "Good fortune grows toward the light. A tall stranger will water you this week, so drink deeply and mind the aphids."


def main():
    assert 1 <= len(TEXT) <= 120, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
