"""
04. Best Time to Buy and Sell Stock  [Easy]  —  Arrays / Loops

`prices[i]` is the stock price on day i. Buy on one day and sell on a LATER
day. Return the max profit, or 0 if no profit is possible.

Example:
    [7, 1, 5, 3, 6, 4]  ->  5   (buy at 1, sell at 6)
    [7, 6, 4, 3, 1]     ->  0

Goal: single pass, track min price so far.
"""

from _runner import run_tests
from typing import List   

def max_profit(prices: List[int]):
    profit = 0
    if len(prices)>0:
        buy_price = prices[0]
        for i in range(1,len(prices)):
            if buy_price > prices[i]:
                buy_price = prices[i]
            profit = max(profit, prices[i]-buy_price)

    return profit



CASES = [
    ("example 1", ([7, 1, 5, 3, 6, 4],), 5),
    ("example 2", ([7, 6, 4, 3, 1],), 0),
    ("single day", ([5],), 0),
    ("empty list", ([],), 0),
    ("flat prices", ([3, 3, 3, 3],), 0),
    ("min after max", ([2, 4, 1, 3],), 2),
    ("steady rise", ([1, 2, 3, 4, 5],), 4),
]


if __name__ == "__main__":
    run_tests(max_profit, CASES)
