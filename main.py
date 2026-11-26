"""Describe Your Ex in One Word -- entry program.

Writes exactly one word to /output/entry.txt.

The word is "Unsubscribed": the ex, filed away like a spam
newsletter -- unsubscribed from my life. One word, spelled
correctly, no punctuation tricks, and the joke arrives with
the word itself.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of
1-111 characters, not only white space. Task gate on top of
that: exactly one word (judge criteria 1 and 4).

Stdlib only. Deterministic, no network, no clock, no random,
reads no other file. The word is validated BEFORE anything
is written; a failed validation exits non-zero and writes
nothing.
"""

import sys
from pathlib import Path

WORD = "Unsubscribed"

OUTPUT_PATH = "/output/entry.txt"

MIN_CHARS = 1
MAX_CHARS = 111


def validate_word(word):
    """Enforce the gate rules for a candidate entry word.

    Raises TypeError for a wrong type, ValueError for a wrong
    value. Checks, in order: str type; 1-111 characters
    (counted as characters, not bytes); not whitespace-only;
    exactly one word (one token, no leading/trailing or
    internal whitespace); letters only (no punctuation,
    digits, hyphens or other tricks).
    """
    if not isinstance(word, str):
        raise TypeError("entry word must be str, got %s" % type(word).__name__)
    if not MIN_CHARS <= len(word) <= MAX_CHARS:
        raise ValueError(
            "entry word must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(word))
        )
    if not word.strip():
        raise ValueError("entry word must not be only white space")
    if word != word.strip() or len(word.split()) != 1:
        raise ValueError("entry word must be exactly one word")
    if not word.isalpha():
        raise ValueError("entry word must be letters only, no punctuation")


def write_entry(path=OUTPUT_PATH):
    """Validate WORD, then write it (no trailing newline) to path.

    The parent directory is created if needed. Nothing is
    written when validation fails.
    """
    validate_word(WORD)
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(WORD, encoding="utf-8")


def main():
    try:
        write_entry()
    except (TypeError, ValueError) as exc:
        print("invalid entry: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
