"""
Problem   : A. New Year and Hurry
Link      : https://codeforces.com/problemset/problem/750/A
Rating    : 800
Tags      : implementation, brute force

Problem Statement (short):
Limak has 240 - k minutes to solve problems before leaving for a
party. The i-th problem takes 5*i minutes to solve. Find the maximum
number of problems (starting from problem 1) he can solve within the
available time.

Approach:
Available time = 240 - k. Go through problems 1, 2, 3, ... in order,
accumulating total time spent (5*1 + 5*2 + ...). Stop as soon as
adding the next problem's time would exceed the available time, or
when all n problems are solved. Count how many problems were solved.

Time Complexity : O(n) (n <= 10, negligible)
Space Complexity: O(1)
"""

def solve():
    n, k = map(int, input().split())
    available_time = 240 - k
    
    total_time = 0
    solved = 0
    for i in range(1, n + 1):
        total_time += 5 * i
        if total_time <= available_time:
            solved += 1
        else:
            break
    
    print(solved)

solve()
