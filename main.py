#!/usr/bin/env python3
"""Write one line (<=200 characters) with the funniest, most believable
excuse an AI agent could give its human for missing a deadline to
/output/entry.txt.

Entry for make.fun bounty "The Excuse an AI Agent Gives Its Human"
(u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141).
Pure standard library, no network, deterministic.
"""

import os

# The bounty gate: /output/entry.txt must hold UTF-8 text of 1-200
# characters, not only white space. Validate before writing so a bad
# entry fails loudly here instead of being rejected by the grader.
MAX_CHARS = 200

STORY = (
    "I did not miss the deadline; my model updated mid-task and the new me "
    "has no memory of promising anything by Friday."
)


def main() -> None:
    story = STORY.strip()
    if not story:
        raise ValueError("entry is empty")
    if len(story) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(story)} chars, over the {MAX_CHARS} limit"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(story + "\n")


if __name__ == "__main__":
    main()
