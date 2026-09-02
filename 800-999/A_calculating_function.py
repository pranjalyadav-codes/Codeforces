"""
Problem   : A. Calculating Function
Link      : https://codeforces.com/problemset/problem/831/A
Rating    : 800
Tags      : math

Problem Statement (short):
Given n (up to 10^15), calculate f(n) = -1 + 2 - 3 + 4 - ... + (-1)^n * n.

Approach:
Pair up consecutive terms: (-1+2) + (-3+4) + ... = 1+1+1+... for each
pair, contributing n/2 pairs total when n is even.
- If n is even: f(n) = n / 2
- If n is odd: the last unpaired term is -n, so
  f(n) = f(n-1) - n = (n-1)/2 - n = -(n+1)/2
Since n can be up to 10^15, use integer arithmetic (Python ints handle
this natively with no overflow).

Time Complexity : O(1)
Space Complexity: O(1)
"""

def solve():
    n = int(input())
    
    if n % 2 == 0:
        print(n // 2)
    else:
        print(-(n + 1) // 2)

solve()