#!/usr/bin/env python3
"""Write the single make.fun entry to the configured output folder."""

import os
import sys
from pathlib import Path

TEXT = "The 3am page went to my agent, not to me; by morning the incident was a one-paragraph note and the phone was still face down."

assert 1 <= len(TEXT) <= 280

output_dir_name = os.environ.get("MAKEFUN_OUTPUT_DIR")
if output_dir_name is None:
    output_dir_name = os.environ.get("OUTPUT_DIR", "/output")
output_dir = Path(output_dir_name)
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")

print(len(TEXT), file=sys.stderr)
