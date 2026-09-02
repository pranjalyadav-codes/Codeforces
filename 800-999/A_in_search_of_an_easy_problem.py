"""
Problem   : A. In Search of an Easy Problem
Link      : https://codeforces.com/problemset/problem/1030/A
Rating    : 800
Tags      : implementation

Problem Statement (short):
Given n responses (0 = easy, 1 = hard), print "HARD" if at least one
person thinks the problem is hard, otherwise print "EASY".

Approach:
Read the list of responses. If any value in the list is 1, print
"HARD"; otherwise (all zeros) print "EASY". This can be checked
directly using the `in` operator or `any()`.

Time Complexity : O(n)
Space Complexity: O(n) for storing the responses
"""

def solve():
    n = int(input())
    responses = list(map(int, input().split()))
    
    if 1 in responses:
        print("HARD")
    else:
        print("EASY")

solve()