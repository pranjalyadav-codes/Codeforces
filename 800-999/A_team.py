"""
Problem   : A. Team
Link      : https://codeforces.com/problemset/problem/231/A
Rating    : 800
Tags      : implementation, brute force

Problem Statement (short):
Three friends (Petya, Vasya, Tonya) solve n problems together. For each
problem, we know which friends are sure about the solution (1) and which
aren't (0). They will write a solution only if at least 2 of the 3 friends
are sure about it. Count how many problems they will solve.

Approach:
For each of the n lines, read three integers (0 or 1). If their sum is
>= 2, it means at least two friends are sure -> count this problem.
Sum a counter over all n lines and print it.

Time Complexity : O(n)
Space Complexity: O(1)
"""

def solve():
    n = int(input())
    count = 0
    for _ in range(n):
        a, b, c = map(int, input().split())
        if a + b + c >= 2:
            count += 1
    print(count)

solve()