import compileall
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    ok = True
    for name in ["medilink_contract.py", "config.py", "demo_summary.py"]:
        ok = compileall.compile_file(str(ROOT / name), quiet=1) and ok
    for folder in ["tests", "scripts"]:
        ok = compileall.compile_dir(str(ROOT / folder), quiet=1) and ok
    if not ok:
        print("Syntax check failed")
        return 1

    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=ROOT,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())