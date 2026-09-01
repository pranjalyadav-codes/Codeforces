"""
Problem   : A. Beautiful Year
Link      : https://codeforces.com/problemset/problem/271/A
Rating    : 800
Tags      : implementation, brute force

Problem Statement (short):
Given a year y, find the minimum year strictly greater than y whose
digits are all distinct (no repeated digits).

Approach:
Start checking from y+1 upward. For each candidate year, convert it to
a string and check if the number of distinct characters equals the
total number of characters (i.e. no digit repeats). Return the first
year that satisfies this condition. Since the answer is guaranteed to
exist and y <= 9000, this brute force check is very fast.

Time Complexity : O(k) where k = number of years checked before finding
                   a valid one (small in practice, well within limits)
Space Complexity: O(1)
"""

def has_distinct_digits(year):
    s = str(year)
    return len(set(s)) == len(s)

def solve():
    y = int(input())
    year = y + 1
    while not has_distinct_digits(year):
        year += 1
    print(year)

solve()