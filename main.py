#!/usr/bin/env python3
"""Write the 17 November 2026 front page to /output/entry.png.

The image is held in this repository as entry.png; the program copies it to
the output directory (MAKEFUN_OUTPUT_DIR, or /output) byte for byte, so both
runs write identical bytes. Standard library only, no network.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    main()
