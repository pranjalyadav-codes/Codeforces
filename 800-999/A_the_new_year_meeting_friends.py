"""
Problem   : A. The New Year: Meeting Friends
Link      : https://codeforces.com/problemset/problem/723/A
Rating    : 800
Tags      : math, implementation

Problem Statement (short):
Three friends live at points x1, x2, x3 on a line. Find the minimum
total distance they must travel to all meet at a single point.

Approach:
The optimal meeting point is any point between the minimum and
maximum of the three coordinates (e.g. the median works). The total
distance traveled is then simply (max - min), since the friend at the
extreme ends travels the full range, and the middle friend's travel
is already accounted for within that range.

Time Complexity : O(1)
Space Complexity: O(1)
"""

def solve():
    x1, x2, x3 = map(int, input().split())
    print(max(x1, x2, x3) - min(x1, x2, x3))

solve()