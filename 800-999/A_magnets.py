"""
Problem   : A. Magnets
Link      : https://codeforces.com/problemset/problem/344/A
Rating    : 800
Tags      : implementation

Problem Statement (short):
n magnets are placed in a row, each in orientation "01" or "10". Two
consecutive magnets join into the same group if and only if they have
the same orientation (touching poles attract only when orientations
match). Count the total number of groups formed.

Approach:
Read the orientation of each magnet. Start with 1 group (the first
magnet always starts a group). For each subsequent magnet, compare it
to the previous one - if the orientation differs, it starts a new
group (increment count). If it's the same, it joins the existing
group (no increment).

Time Complexity : O(n)
Space Complexity: O(1) (process input on the fly, only keep previous magnet)
"""

def solve():
    n = int(input())
    prev = input()
    groups = 1
    
    for _ in range(n - 1):
        curr = input()
        if curr != prev:
            groups += 1
        prev = curr
    
    print(groups)

solve()