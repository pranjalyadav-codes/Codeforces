"""
Problem   : A. Word Capitalization
Link      : https://codeforces.com/problemset/problem/281/A
Rating    : 800
Tags      : implementation, strings

Problem Statement (short):
Given a word consisting of lowercase and uppercase letters, capitalize
it - make the first letter uppercase, and leave all other letters
unchanged (do not touch their case).

Approach:
Take the first character, convert it to uppercase using upper(), then
concatenate it with the rest of the string unchanged (s[1:]).
Note: Python's built-in .capitalize() won't work here because it also
lowercases the rest of the string - we only want to change the first
letter, not the others.

Time Complexity : O(n) where n = length of the word
Space Complexity: O(n) for the new string
"""

def solve():
    s = input()
    result = s[0].upper() + s[1:]
    print(result)

solve()