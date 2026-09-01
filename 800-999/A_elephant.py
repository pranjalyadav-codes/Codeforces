"""
Problem   : A. Elephant
Link      : https://codeforces.com/problemset/problem/617/A
Rating    : 800
Tags      : math, greedy, implementation

Problem Statement (short):
An elephant starts at position 0 and wants to reach position x. In one
step he can move 1, 2, 3, 4, or 5 positions forward. Find the minimum
number of steps needed to reach exactly x.

Approach:
To minimize the number of steps, always take the largest step (5)
whenever possible. So the minimum number of steps is simply
ceil(x / 5), which in integer arithmetic is (x + 4) // 5.

Time Complexity : O(1)
Space Complexity: O(1)
"""

def solve():
    x = int(input())
    print((x + 4) // 5)

solve()