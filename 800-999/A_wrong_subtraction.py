"""
Problem   : A. Wrong Subtraction
Link      : https://codeforces.com/problemset/problem/977/A
Rating    : 800
Tags      : implementation

Problem Statement (short):
Given a number n, apply the following operation k times: if the last
digit is non-zero, subtract 1 from n; if the last digit is zero,
remove the last digit (i.e. divide n by 10). Print the result after
k operations.

Approach:
Simulate the process directly in a loop that runs k times:
- check n % 10 (last digit)
- if non-zero: n -= 1
- if zero: n //= 10
Since k <= 50, direct simulation is fast enough - no need for any
optimization.

Time Complexity : O(k)
Space Complexity: O(1)
"""

def solve():
    n, k = map(int, input().split())
    
    for _ in range(k):
        if n % 10 != 0:
            n -= 1
        else:
            n //= 10
    
    print(n)

solve()