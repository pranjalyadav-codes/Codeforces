"""
Problem   : A. Games
Link      : https://codeforces.com/problemset/problem/268/A
Rating    : 800
Tags      : implementation, brute force

Problem Statement (short):
n teams each have a home color h[i] and guest color a[i] (different
from each other). In a match where team i hosts team j, the host
normally wears home color, EXCEPT when the host's home color equals
the guest team's guest color (h[i] == a[j]) - in that case the host
switches to its own guest uniform. Count how many of the n*(n-1)
games result in the host wearing a guest uniform.

Approach:
For every ordered pair (i, j) with i != j, check if h[i] == a[j].
If so, count it. Since n <= 30, brute force over all pairs (O(n^2))
is fast enough.

Time Complexity : O(n^2)
Space Complexity: O(n) for storing home/guest colors
"""

def solve():
    n = int(input())
    h = []
    a = []
    for _ in range(n):
        hi, ai = map(int, input().split())
        h.append(hi)
        a.append(ai)
    
    count = 0
    for i in range(n):
        for j in range(n):
            if i != j and h[i] == a[j]:
                count += 1
    
    print(count)

solve()