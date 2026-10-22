"""
26. FizzBuzz  [Easy]  —  Loops

Return a list of strings for 1..n:
  "FizzBuzz" if divisible by 3 and 5, "Fizz" if by 3, "Buzz" if by 5,
  otherwise the number as a string.

Example:
    n = 5  ->  ["1", "2", "Fizz", "4", "Buzz"]
"""

from _runner import run_tests


def fizzbuzz(n):
    # write your solution here
    pass


CASES = [
    ("example 1", (5,), ["1", "2", "Fizz", "4", "Buzz"]),
    ("n = 15", (15,), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz",
                       "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]),
    ("n = 1", (1,), ["1"]),
    ("n = 0", (0,), []),
    ("n = 3", (3,), ["1", "2", "Fizz"]),
]


if __name__ == "__main__":
    run_tests(fizzbuzz, CASES)
