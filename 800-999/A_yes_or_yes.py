"""
Problem   : A. YES or YES?
Link      : https://codeforces.com/problemset/problem/1703/A
Rating    : 800
Tags      : implementation, strings

Problem Statement (short):
Given a string s of length 3, check if it equals "YES" ignoring case
(e.g. "yES", "Yes" are all valid). Print "YES" if it matches,
otherwise "NO".

Approach:
Convert the input string to uppercase (or lowercase) and compare it
directly with "YES" (or "yes"). Print "YES" if they match, "NO"
otherwise.

Time Complexity : O(1) per test case (fixed length 3 string)
Space Complexity: O(1)
"""

def solve():
    s = input().upper()
    if s == "YES":
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()