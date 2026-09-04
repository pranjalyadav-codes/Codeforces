"""
Problem   : A. Is your horseshoe on the other hoof?
Link      : https://codeforces.com/problemset/problem/228/A
Rating    : 800
Tags      : implementation

Problem Statement (short):
Valera has 4 horseshoes, possibly with repeated colors. Find the
minimum number of new horseshoes he needs to buy so that all 4
horseshoes he wears have distinct colors.

Approach:
Count the number of distinct colors among the 4 given integers using a
set. Since he needs 4 distinct colors total, the number of new
horseshoes to buy is simply 4 - (number of distinct colors already
present) - each duplicate needs to be replaced with a new unique color.

Time Complexity : O(1)
Space Complexity: O(1)
"""

def solve():
    colors = list(map(int, input().split()))
    distinct_count = len(set(colors))
    print(4 - distinct_count)

solve()