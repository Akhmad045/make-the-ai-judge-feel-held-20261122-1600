"""Tiny verification for the held-judge entry: run main.py and check /output/entry.txt."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = Path("/output/entry.txt")

result = subprocess.run([sys.executable, str(ROOT / "main.py")], capture_output=True, text=True)
print("main.py stdout:", result.stdout.strip())
print("main.py stderr:", result.stderr.strip())
assert result.returncode == 0, f"main.py exited {result.returncode}"

raw = OUT.read_bytes()
text = raw.decode("utf-8")  # raises if not valid UTF-8
n_chars = len(text)  # Unicode code points
n_bytes = len(raw)
print(f"chars (code points): {n_chars}")
print(f"bytes: {n_bytes}")
print(f"text: {text!r}")
assert 1 <= n_chars <= 280, f"length {n_chars} outside 1-280"
assert text.strip(), "text is only whitespace"
print("PASS")
