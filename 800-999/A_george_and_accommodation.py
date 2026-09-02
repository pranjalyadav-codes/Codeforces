"""
Problem   : A. George and Accommodation
Link      : https://codeforces.com/problemset/problem/709/A
Rating    : 800
Tags      : implementation

Problem Statement (short):
Given n rooms, each with current occupancy p[i] and capacity q[i],
count how many rooms have enough free space for 2 more people
(George and Alex) to move in.

Approach:
For each room, compute the free space as q[i] - p[i]. If this free
space is >= 2, count the room. Sum this count over all n rooms.

Time Complexity : O(n)
Space Complexity: O(1)
"""

def solve():
    n = int(input())
    count = 0
    
    for _ in range(n):
        p, q = map(int, input().split())
        if q - p >= 2:
            count += 1
    
    print(count)

solve()