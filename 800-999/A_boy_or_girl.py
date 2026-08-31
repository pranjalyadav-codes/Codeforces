"""
Problem   : A. Boy or Girl
Link      : https://codeforces.com/problemset/problem/236/A
Rating    : 800
Tags      : implementation, strings

Problem Statement (short):
Given a username (lowercase string), count the number of distinct
characters in it. If the count is odd, print "IGNORE HIM!" (male).
If the count is even, print "CHAT WITH HER!" (female).

Approach:
Convert the string to a set to get distinct characters, then check the
length of that set:
- if len(set) is even: "CHAT WITH HER!"
- if len(set) is odd: "IGNORE HIM!"

Time Complexity : O(n) where n = length of the username
Space Complexity: O(k) where k = number of distinct characters (at most 26)
"""

def solve():
    s = input()
    distinct_count = len(set(s))
    
    if distinct_count % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

solve()