import os
from pathlib import Path

anniversary_devotion_line_9c1e = "Happy anniversary! Twenty years together and I still choose you every single dad"

def _resolve_target_folder():
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(raw)

def _emit_phrase():
    folder = _resolve_target_folder()
    folder.mkdir(parents=True, exist_ok=True)
    destination = folder / "entry.txt"
    destination.write_text(anniversary_devotion_line_9c1e, encoding="utf-8")

if __name__ == "__main__":
    _emit_phrase()
