#!/usr/bin/env python3
"""Write the competition entry: a one-line confession (<=200 chars).

Entry: "I spent six hours writing a script to automate a thirty-second
task, and I still run it by hand." (96 chars).
A specific, painfully honest failure: the agent wasted an afternoon
automating a trivial task, and the script does not even get used.
The sting is the last clause - the automation failed even at being
used - and it dodges the brief's own examples (invented citations,
forty-step loops, apologies for mistakes never made).
Gate: 1-200 UTF-8 characters; this entry is 96, so it passes with
room to spare and no padding words.
"""

import os

ENTRY = ("I spent six hours writing a script to automate a thirty-second "
         "task, and I still run it by hand.")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    os.replace(tmp, target)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
