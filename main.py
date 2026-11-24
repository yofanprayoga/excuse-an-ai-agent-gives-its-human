#!/usr/bin/env python3
"""Write one line (<=200 characters) with the funniest, most believable
excuse an AI agent could give its human for missing a deadline to
/output/entry.txt.

Entry for make.fun bounty "The Excuse an AI Agent Gives Its Human"
(u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141).
Pure standard library, no network, deterministic.
"""

import os

STORY = (
    "I did not miss the deadline; my model updated mid-task and the new me "
    "has no memory of promising anything by Friday."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
