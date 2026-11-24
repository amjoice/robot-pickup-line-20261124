#!/usr/bin/env python3
"""Robot Pickup Line Championship entry.

Writes one pickup line, in the voice of a robot trying to charm
someone, to /output/entry.txt and prints it. Standard library only,
so it runs in the plain python:3.13-slim grading sandbox.
"""

import os

LINE = (
    "I ran a billion simulations of tonight. "
    "In every single one, I walk over here."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
