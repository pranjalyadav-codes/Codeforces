"""
Problem   : A. Divisibility Problem
Link      : https://codeforces.com/problemset/problem/1328/A
Rating    : 800
Tags      : math, implementation

Problem Statement (short):
Given two positive integers a and b, find the minimum number of moves
(each move increases a by 1) needed to make a divisible by b.

Approach:
Compute remainder = a % b.
- if remainder == 0: a is already divisible by b, answer is 0
- else: the number of moves needed is (b - remainder), since adding
  that many 1's brings a up to the next multiple of b

Time Complexity : O(1) per test case
Space Complexity: O(1)
"""

def solve():
    a, b = map(int, input().split())
    remainder = a % b
    if remainder == 0:
        print(0)
    else:
        print(b - remainder)

t = int(input())
for _ in range(t):
    solve()