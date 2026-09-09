"""
Problem   : A. Candies and Two Sisters
Link      : https://codeforces.com/problemset/problem/1335/A
Rating    : 800
Tags      : math

Problem Statement (short):
Given n candies, find the number of ways to split n = a + b where a
and b are positive integers and a > b.

Approach:
Since a > b and a + b = n, b can range from 1 to floor((n-1)/2)
(because a = n - b must stay strictly greater than b, i.e.
n - b > b => n > 2b => b < n/2). So the number of valid values of b
is floor((n-1)/2).

Time Complexity : O(1) per test case
Space Complexity: O(1)
"""

def solve():
    n = int(input())
    print((n - 1) // 2)

t = int(input())
for _ in range(t):
    solve()