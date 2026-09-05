"""
Problem   : A. Hulk
Link      : https://codeforces.com/problemset/problem/705/A
Rating    : 800
Tags      : implementation, strings

Problem Statement (short):
Given n, build a string with n layers alternating "I hate" (odd
layers: 1st, 3rd, 5th...) and "I love" (even layers: 2nd, 4th, 6th...),
each layer joined by "that ", ending with "it".

Approach:
Loop from 1 to n. For each layer i:
- if i is odd: append "I hate"
- if i is even: append "I love"
Join each layer with "that " (except before the last one, where "it"
is appended instead). Build using a list of parts then join with " ".

Time Complexity : O(n)
Space Complexity: O(n) for the parts list
"""

def solve():
    n = int(input())
    parts = []
    
    for i in range(1, n + 1):
        if i % 2 == 1:
            parts.append("I hate")
        else:
            parts.append("I love")
    
    result = " that ".join(parts) + " it"
    print(result)

solve()