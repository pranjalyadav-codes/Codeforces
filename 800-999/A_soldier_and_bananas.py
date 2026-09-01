"""
Problem   : A. Soldier and Bananas
Link      : https://codeforces.com/problemset/problem/546/A
Rating    : 800
Tags      : math, implementation

Problem Statement (short):
A soldier wants to buy w bananas, paying i*k dollars for the i-th
banana. He has n dollars. Find how many dollars he needs to borrow
(0 if he already has enough).

Approach:
Total cost = k * (1 + 2 + ... + w) = k * w * (w + 1) / 2
             (sum of first w natural numbers formula)
Amount to borrow = max(0, total_cost - n)

Time Complexity : O(1)
Space Complexity: O(1)
"""

def solve():
    k, n, w = map(int, input().split())
    total_cost = k * w * (w + 1) // 2
    borrow = max(0, total_cost - n)
    print(borrow)

solve()