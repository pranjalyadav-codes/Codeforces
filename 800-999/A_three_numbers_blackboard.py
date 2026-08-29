"""
Problem   : A. Three Numbers on the Blackboard
Link      : https://codeforces.com/contest/2256/problem/A
Rating    : 800
Tags      : math, greedy, sorting

Problem Statement (short):
Given three non-negative integers a, b, c, you may repeatedly replace any
one number with the sum of the other two. Find the minimum possible range
(max - min) achievable.

Approach:
Sort the numbers so a <= b <= c.
- If a + b <= c: replacing c with (a+b) shrinks the max, giving a new
  range of b (new triple becomes a, b, a+b -> range = (a+b) - a = b).
- If a + b > c: no operation can reduce the range further, so the
  answer is simply the original range, c - a.

Time Complexity : O(1) per test case
Space Complexity: O(1)
"""

def solve():
    a, b, c = map(int, input().split())
    a, b, c = sorted([a, b, c])
    
    if a + b <= c:
        print(b)
    else:
        print(c - a)

t = int(input())
for _ in range(t):
    solve()