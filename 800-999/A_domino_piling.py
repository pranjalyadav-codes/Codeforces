"""
Problem   : A. Domino piling
Link      : https://codeforces.com/problemset/problem/50/A
Rating    : 800
Tags      : math, greedy

Problem Statement (short):
Given a rectangular board of M x N squares, find the maximum number of
2x1 domino pieces that can be placed on it without overlapping and
without going outside the board (rotation allowed).

Approach:
Every domino covers exactly 2 squares, regardless of orientation.
Total squares on the board = M * N.
So the maximum number of dominoes that fit is simply floor((M * N) / 2)
- if M*N is even, the board is fully covered.
- if M*N is odd, exactly one square is left empty.
No simulation of the board is needed - it's a direct formula.

Time Complexity : O(1)
Space Complexity: O(1)
"""

def solve():
    m, n = map(int, input().split())
    print((m * n) // 2)

solve()