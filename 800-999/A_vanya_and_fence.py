"""
Problem   : A. Vanya and Fence
Link      : https://codeforces.com/problemset/problem/677/A
Rating    : 800
Tags      : implementation

Problem Statement (short):
n friends walk along a fence of height h. A friend whose height is <= h
walks normally (width 1); a friend whose height is > h must bend down
(width 2). Find the total minimum width of the road needed for all
friends walking in a single row.

Approach:
For each person's height a[i]:
- if a[i] <= h: add 1 to total width
- if a[i] > h: add 2 to total width
Sum this over all n people and print the total.

Time Complexity : O(n)
Space Complexity: O(n) for storing the heights (or O(1) if processed on the fly)
"""

def solve():
    n, h = map(int, input().split())
    heights = list(map(int, input().split()))
    
    total_width = 0
    for a in heights:
        if a <= h:
            total_width += 1
        else:
            total_width += 2
    
    print(total_width)

solve()