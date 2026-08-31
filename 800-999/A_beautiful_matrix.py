"""
Problem   : A. Beautiful Matrix
Link      : https://codeforces.com/problemset/problem/263/A
Rating    : 800
Tags      : implementation, math

Problem Statement (short):
Given a 5x5 matrix with 24 zeroes and a single 1, find the minimum number
of adjacent row/column swaps needed to move the 1 to the center cell
(row 3, column 3).

Approach:
Find the row index i and column index j of the 1.
Each row swap moves the 1 one step up/down, each column swap moves it
one step left/right. So the minimum number of moves is just the
Manhattan distance from (i, j) to the center (2, 2):
    moves = |i - 2| + |j - 2|

Time Complexity : O(1) (fixed 5x5 grid)
Space Complexity: O(1)
"""

def solve():
    for i in range(5):
        row = list(map(int, input().split()))

        if 1 in row:
            j = row.index(1)
            print(abs(i - 2) + abs(j - 2))
            return

solve()