"""
Problem   : A. Pangram
Link      : https://codeforces.com/problemset/problem/520/A
Rating    : 800
Tags      : implementation, strings

Problem Statement (short):
Given a string of uppercase and lowercase Latin letters, check if it
is a pangram - i.e. every letter of the alphabet (a-z) appears in it
at least once, regardless of case.

Approach:
Convert the string to lowercase, then use a set to find distinct
letters present. If the set of distinct letters has size 26 (all of
a-z present), print "YES", otherwise print "NO".

Time Complexity : O(n) where n = length of the string
Space Complexity: O(1) (set holds at most 26 characters)
"""

def solve():
    n = int(input())
    s = input().lower()
    
    distinct_letters = set(s)
    if len(distinct_letters) == 26:
        print("YES")
    else:
        print("NO")

solve()