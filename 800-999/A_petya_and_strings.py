"""
Problem   : A. Petya and Strings
Link      : https://codeforces.com/problemset/problem/112/A
Rating    : 800
Tags      : implementation, strings

Problem Statement (short):
Given two strings of equal length, compare them lexicographically,
ignoring letter case. Print -1 if the first is smaller, 1 if the second
is smaller, 0 if they are equal (case-insensitively).

Approach:
Convert both strings to lowercase (or uppercase) to remove case
sensitivity, then use Python's native string comparison:
- if s1 < s2: print -1
- if s1 > s2: print 1
- else: print 0

Time Complexity : O(n) where n = length of the strings
Space Complexity: O(n) for the lowercased copies
"""

def solve():
    s1 = input().lower()
    s2 = input().lower()
    
    if s1 < s2:
        print(-1)
    elif s1 > s2:
        print(1)
    else:
        print(0)

solve()