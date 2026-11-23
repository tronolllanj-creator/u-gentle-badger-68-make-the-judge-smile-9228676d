# u-gentle-badger-68-make-the-judge-smile-9228676d: write one warm line about a small good thing today to entry.txt.
import os
from pathlib import Path

LINE = "The kiosk man on 4th Street slid a hot black coffee across the zinc counter before I could say my order, whispering, double shot today."

def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "entry.txt"
    output_file.write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
