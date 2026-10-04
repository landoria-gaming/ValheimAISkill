#!/usr/bin/env python3
"""Import a generated model package and render it in an isolated Unity project."""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--unity", type=Path, required=True)
    parser.add_argument("--package", type=Path, required=True)
    parser.add_argument("--timeout", type=int, default=180)
    args = parser.parse_args()
    project = Path(tempfile.mkdtemp(prefix="valheim-model-unity-test-"))
    editor = project / "Assets/Editor"
    editor.mkdir(parents=True)
    shutil.copyfile(Path(__file__).with_name("ModelExportValidation.cs"), editor / "ModelExportValidation.cs")
    (project / "Packages").mkdir()
    (project / "ProjectSettings").mkdir()
    (project / "ProjectSettings/ProjectVersion.txt").write_text("m_EditorVersion: 6000.0.75f1\n", encoding="utf-8")
    (project / "Packages/manifest.json").write_text(json.dumps({"dependencies": {
        "com.unity.modules.imageconversion": "1.0.0", "com.unity.modules.physics": "1.0.0",
        "com.unity.modules.jsonserialize": "1.0.0"
    }}), encoding="utf-8")
    report = project / "validation.json"
    log = project / "editor.log"
    env = dict(os.environ, VALHEIM_MODEL_PACKAGE=str(args.package.resolve(strict=True)),
               VALHEIM_MODEL_REPORT=str(report))
    print(f"Isolated Unity import test: {project}", flush=True)
    try:
        result = subprocess.run([str(args.unity.resolve(strict=True)), "-batchmode", "-projectPath", str(project),
                                 "-executeMethod", "ModelExportValidation.Run", "-logFile", str(log)],
                                env=env, timeout=args.timeout,
                                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    except subprocess.TimeoutExpired:
        parser.exit(1, f"Unity test timed out; inspect {log}\n")
    if result.returncode or not report.is_file():
        parser.exit(1, f"Unity test failed; inspect {log}\n")
    print(report.read_text(encoding="utf-8"))
    print(f"Preview: {report.with_suffix('.png')}")


if __name__ == "__main__":
    main()
