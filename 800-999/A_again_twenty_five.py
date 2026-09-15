"""
Problem   : A. Again Twenty Five!
Link      : https://codeforces.com/problemset/problem/630/A
Rating    : 800
Tags      : math

Problem Statement (short):
Given n (2 <= n <= 2*10^18), find the last two digits of 5^n.

Approach:
For any n >= 2, 5^n always ends in "25". This can be shown by
induction: 5^2 = 25 (ends in 25). If 5^k ends in 25, then
5^(k+1) = 5^k * 5, and any number ending in 25 multiplied by 5 ends
in 25 again (25*5=125, ends in 25; and this pattern repeats since the
last two digits only depend on the last two digits of the previous
number). So regardless of how large n is, the answer is always "25" -
no computation of the actual huge power is needed.

Time Complexity : O(1)
Space Complexity: O(1)
"""

def solve():
    n = int(input())  # n is read but not actually needed in the computation
    print("25")

solve()