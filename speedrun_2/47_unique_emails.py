"""
47. Unique Email Addresses  [Easy]  —  Strings / Sets

For each email "local@domain":
  - in the LOCAL part, dots "." are ignored
  - in the LOCAL part, everything after the first "+" is ignored
  - the domain part is unchanged
Return how many distinct addresses actually receive mail.

Example:
    ["test.email+alex@leetcode.com",
     "test.e.mail+bob.cathy@leetcode.com",
     "testemail+david@lee.tcode.com"]   ->  2
"""

from _runner import run_tests


def num_unique_emails(emails):
    # write your solution here
    pass


CASES = [
    ("example 1", (["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com",
                    "testemail+david@lee.tcode.com"],), 2),
    ("all different", (["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"],), 3),
    ("dots in domain matter", (["a@x.com", "a@xcom"],), 2),
    ("plus at start of local", (["+abc@x.com", "@x.com"],), 1),
    ("empty list", ([],), 0),
    ("same after cleaning", (["r.o.u+1@g.com", "rou@g.com", "rou+zz@g.com"],), 1),
]


if __name__ == "__main__":
    run_tests(num_unique_emails, CASES)
