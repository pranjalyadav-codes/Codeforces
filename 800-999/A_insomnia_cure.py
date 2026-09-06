"""
Problem   : A. Insomnia cure
Link      : https://codeforces.com/problemset/problem/148/A
Rating    : 800
Tags      : implementation, brute force

Problem Statement (short):
Given k, l, m, n and d, count how many numbers from 1 to d are
divisible by at least one of k, l, m, n.

Approach:
Loop through every dragon number i from 1 to d. For each i, check if
it's divisible by k, l, m, or n (using modulo). If any condition is
true, count it as damaged. Since d <= 10^5, direct brute force is
fast enough.

Time Complexity : O(d)
Space Complexity: O(1)
"""

def solve():
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())
    d = int(input())
    
    count = 0
    for i in range(1, d + 1):
        if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
            count += 1
    
    print(count)

solve()