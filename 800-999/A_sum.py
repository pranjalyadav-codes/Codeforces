"""
Problem   : A. Sum
Link      : https://codeforces.com/problemset/problem/1742/A
Rating    : 800
Tags      : implementation, math, brute force

Problem Statement (short):
Given three integers a, b, c, determine if one of them equals the sum
of the other two. Print "YES" if so, otherwise "NO".

Approach:
Check all three possible cases:
- a == b + c
- b == a + c
- c == a + b
If any of these hold, print "YES", otherwise print "NO". Since there
are t test cases, wrap this logic in a loop.

Time Complexity : O(1) per test case
Space Complexity: O(1)
"""

def solve():
    a, b, c = map(int, input().split())
    if a == b + c or b == a + c or c == a + b:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()