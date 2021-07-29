#! /usr/bin/env python3

import argparse
import logging
import re

rex = re.compile(r"^(\d+)(.*)$")

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def main():
    parser = argparse.ArgumentParser(
        description="Script to re-number the items in a Markdown numbered list"
    )
    parser.add_argument("filename", help="Path to a markdown file to re-number lists")
    parser.add_argument(
        "--dryrun",
        action="store_true",
        help="Causes the file that would be written to be printed to the screen instead",
    )
    args = parser.parse_args()

    # Get the original content and set step number counter
    lines = open(args.filename).readlines()
    counter = 1

    new_lines = []

    for line in lines:
        m = rex.search(line)
        if m:
            new_lines.append(f"{counter}{m.group(2)}\n")
            counter += 1
        else:
            new_lines.append(line)

    if args.dryrun:
        print("".join(new_lines))
    else:
        with open(args.filename, "w") as fp:
            fp.writelines(new_lines)


if __name__ == "__main__":
    main()
