"""Run every problem file in this folder and print a scoreboard.

    uv run speedrun_2/run_all.py
"""

import contextlib
import importlib.util
import io
import pathlib
import re

from _runner import GREEN, RED, RESET, run_tests

HERE = pathlib.Path(__file__).parent


def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    solved = 0
    files = sorted(HERE.glob("[0-9][0-9]_*.py"))
    for path in files:
        module = load(path)
        source = path.read_text()
        func_name = re.search(r"^def (\w+)", source, re.M).group(1)
        norm_match = re.search(r"normalize=(\w+)", source)
        normalize = getattr(module, norm_match.group(1)) if norm_match else None
        with contextlib.redirect_stdout(io.StringIO()):
            passed, total = run_tests(getattr(module, func_name), module.CASES, normalize)
        done = passed == total
        solved += done
        color = GREEN if done else RED
        print(f"{color}{passed:>2}/{total:<2}{RESET}  {path.name}")
    print(f"\nSolved {solved}/{len(files)} problems")


if __name__ == "__main__":
    main()
