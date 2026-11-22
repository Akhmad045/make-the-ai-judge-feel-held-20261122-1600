"""Entry for make-the-ai-judge-feel-held-20261122-1600.

Writes one short text to /output/entry.txt.
"""

from pathlib import Path

LINES = [
    "The kettle has gone quiet.",
    "Steam rises, thins, is gone.",
    "Outside, the light leaves the rooftops one by one, and the house settles into its own small sounds — a clock, a chair, your breath finding its slower shape.",
]


def build_text() -> str:
    # One unhurried paragraph: short sentences, then one long settling one.
    return " ".join(line.strip() for line in LINES)


def main() -> None:
    text = build_text()
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
