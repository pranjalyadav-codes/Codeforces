"""
Problem   : A. Hit the Lottery
Link      : https://codeforces.com/problemset/problem/996/A
Rating    : 800
Tags      : greedy, math

Problem Statement (short):
Given n dollars and bill denominations 1, 5, 10, 20, 100, find the
minimum number of bills needed to make exactly n dollars.

Approach:
Use a greedy approach: always use as many of the largest denomination
as possible before moving to the next smaller one. This works here
because the denominations (100, 20, 10, 5, 1) are structured so that
greedy always gives the optimal (minimum) number of bills.
For each denomination d (largest to smallest):
    count += n // d
    n = n % d

Time Complexity : O(1) (fixed number of denominations)
Space Complexity: O(1)
"""

def solve():
    n = int(input())
    denominations = [100, 20, 10, 5, 1]
    
    count = 0
    for d in denominations:
        count += n // d
        n %= d
    
    print(count)

solve()