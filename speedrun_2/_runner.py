"""Tiny test runner shared by every problem file in this folder.

Each problem file defines a function + a CASES list and calls run_tests().
A case is a tuple: (label, args_tuple, expected).
"""

import copy
import time

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
DIM = "\033[2m"
RESET = "\033[0m"


def _short(value, limit=70):
    text = repr(value)
    return text if len(text) <= limit else text[: limit - 3] + "..."


def _stub():
    pass


def run_tests(func, cases, normalize=None):
    """Run every case against func. Returns (passed, total)."""
    total = len(cases)
    passed = 0
    print(f"\n{YELLOW}Running {func.__name__}() — {total} test cases{RESET}\n")
    if func.__code__.co_code == _stub.__code__.co_code:
        print(f"{RED}Not implemented yet — replace `pass` with your solution.{RESET}\n")
        print(f"{RED}Passed 0/{total}{RESET}\n")
        return 0, total
    start_all = time.perf_counter()

    for counter, (label, args, expected) in enumerate(cases, start=1):
        call_args = copy.deepcopy(args)
        start = time.perf_counter()
        try:
            got = func(*call_args)
            error = None
        except Exception as exc:  # show the crash, keep running other cases
            got, error = None, exc
        elapsed_ms = (time.perf_counter() - start) * 1000

        if normalize and error is None:
            try:
                ok = normalize(got) == normalize(expected)
            except Exception:  # e.g. stub returned None
                ok = False
        else:
            ok = error is None and got == expected

        status = f"{GREEN}PASS{RESET}" if ok else f"{RED}FAIL{RESET}"
        print(f"[{counter:>2}/{total}] {status}  {label:<28} {DIM}{elapsed_ms:7.3f} ms{RESET}")
        if ok:
            passed += 1
            continue
        print(f"         input:    {_short(args)}")
        print(f"         expected: {_short(expected)}")
        if error is not None:
            print(f"         error:    {RED}{type(error).__name__}: {error}{RESET}")
        else:
            print(f"         got:      {_short(got)}")

    total_ms = (time.perf_counter() - start_all) * 1000
    color = GREEN if passed == total else RED
    print(f"\n{color}Passed {passed}/{total}{RESET}  "
          f"(executed {total} cases in {total_ms:.2f} ms)\n")
    return passed, total
