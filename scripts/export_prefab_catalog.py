#!/usr/bin/env python3
"""Repository entrypoint for the prefab exporter shipped with the skill."""

from pathlib import Path
import runpy
import sys

SCRIPTS = Path(__file__).resolve().parents[1] / "skills/valheim-modding/scripts"
sys.path.insert(0, str(SCRIPTS))
if __name__ == "__main__":
    runpy.run_path(str(SCRIPTS / "export_prefab_catalog.py"), run_name="__main__")
