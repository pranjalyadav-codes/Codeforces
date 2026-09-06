"""
Problem   : A. Anton and Letters
Link      : https://codeforces.com/problemset/problem/443/A
Rating    : 800
Tags      : implementation, strings

Problem Statement (short):
Given a line like "{a, b, c}" listing lowercase letters separated by
", ", possibly with duplicates, count the number of distinct letters.

Approach:
Read the full line, then filter out only the lowercase alphabet
characters (ignore '{', '}', ',', and spaces). Put them into a set to
get distinct letters, then print the size of that set.

Time Complexity : O(n) where n = length of the input line
Space Complexity: O(k) where k = number of distinct letters (at most 26)
"""

def solve():
    s = input()
    letters = set(ch for ch in s if ch.islower())
    print(len(letters))

solve()