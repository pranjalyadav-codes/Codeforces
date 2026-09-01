"""
Problem   : A. Translation
Link      : https://codeforces.com/problemset/problem/41/A
Rating    : 800
Tags      : implementation, strings

Problem Statement (short):
Given two words s and t, check if t is exactly s written in reverse.
Print "YES" if t == reverse(s), otherwise print "NO".

Approach:
Read both strings, reverse s using slicing (s[::-1]), and compare it
directly with t. Print "YES" if they match, "NO" otherwise.

Time Complexity : O(n) where n = length of the word
Space Complexity: O(n) for the reversed string
"""

def solve():
    s = input()
    t = input()
    
    if s[::-1] == t:
        print("YES")
    else:
        print("NO")

solve()