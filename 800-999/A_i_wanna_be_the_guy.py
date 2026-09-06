"""
Problem   : A. I Wanna Be the Guy
Link      : https://codeforces.com/problemset/problem/469/A
Rating    : 800
Tags      : implementation, sets

Problem Statement (short):
Given n levels, Little X can pass p specific levels and Little Y can
pass q specific levels. Check if together (union of both sets) they
can cover all n levels from 1 to n.

Approach:
Read X's levels and Y's levels into a single set (union automatically
removes duplicates). If the size of that combined set equals n, all
levels are covered - print "I become the guy.". Otherwise, print
"Oh, my keyboard!".

Time Complexity : O(p + q)
Space Complexity: O(p + q) for the set
"""

def solve():
    n = int(input())
    
    x_levels = list(map(int, input().split()))[1:]  # skip p, take the levels
    y_levels = list(map(int, input().split()))[1:]  # skip q, take the levels
    
    combined = set(x_levels) | set(y_levels)
    
    if len(combined) == n:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")

solve()