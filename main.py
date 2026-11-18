"""make.fun entry for news-image-20261117 (Python 3.13, stdlib only).

The entry image is entry.png beside this file: a one-image front page
summing up the world news of Tuesday 17 November 2026, rendered by
tools/generate_frontpage.py from headlines hardcoded there. This program
copies those exact bytes to the output path, so every run writes the
same image, deterministically and with no network access.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE_IMAGE = os.path.join(HERE, "entry.png")


def main():
    # Byte-for-byte copy: the judge sees exactly the rendered front page,
    # and two runs always produce identical output bytes.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SOURCE_IMAGE, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
