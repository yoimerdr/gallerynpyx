from __future__ import annotations

import runpy
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BUILD_SCRIPT = ROOT / ".build" / "gallerynpyx.build.py"


if __name__ == "__main__":
    sys.argv = [str(BUILD_SCRIPT), *sys.argv[1:]]
    runpy.run_path(str(BUILD_SCRIPT), run_name="__main__")
