"""
Problem   : A. Anton and Danik
Link      : https://codeforces.com/problemset/problem/734/A
Rating    : 800
Tags      : implementation, strings

Problem Statement (short):
Given a string of 'A' and 'D' representing game winners, determine who
won more games. Print "Anton" if he won more, "Danik" if Danik won
more, or "Friendship" if they won an equal number of games.

Approach:
Count occurrences of 'A' and 'D' in the string using count().
Compare the two counts:
- if A_count > D_count: print "Anton"
- if D_count > A_count: print "Danik"
- else: print "Friendship"

Time Complexity : O(n) where n = length of the string
Space Complexity: O(1)
"""

def solve():
    n = int(input())
    s = input()
    
    a_count = s.count('A')
    d_count = s.count('D')
    
    if a_count > d_count:
        print("Anton")
    elif d_count > a_count:
        print("Danik")
    else:
        print("Friendship")

solve()