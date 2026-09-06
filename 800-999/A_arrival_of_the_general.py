"""
Problem   : A. Arrival of the General
Link      : https://codeforces.com/problemset/problem/144/A
Rating    : 800
Tags      : implementation

Problem Statement (short):
Given n soldiers with heights, find the minimum number of adjacent
swaps needed so that the first soldier has the maximum height (first
occurrence) and the last soldier has the minimum height (last
occurrence).

Approach:
- Find index of the FIRST occurrence of the maximum height -> max_idx
- Find index of the LAST occurrence of the minimum height -> min_idx
- Moves to bring max to front = max_idx (number of swaps to move it
  from its position to index 0)
- Moves to bring min to back = (n - 1 - min_idx)
- If max_idx < min_idx (max comes before min in the array), these two
  moves don't interfere, so total = max_idx + (n-1-min_idx)
- If max_idx > min_idx (max is after min), moving max to front shifts
  min one position to the right, so we need one extra swap:
  total = max_idx + (n-1-min_idx) - 1

Time Complexity : O(n)
Space Complexity: O(n) for storing the array
"""

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    max_val = max(a)
    min_val = min(a)
    
    max_idx = a.index(max_val)          # first occurrence of max
    min_idx = len(a) - 1 - a[::-1].index(min_val)  # last occurrence of min
    
    moves = max_idx + (n - 1 - min_idx)
    
    if max_idx > min_idx:
        moves -= 1
    
    print(moves)

solve()