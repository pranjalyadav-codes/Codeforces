"""
Problem   : A. Tram
Link      : https://codeforces.com/problemset/problem/116/A
Rating    : 800
Tags      : implementation, brute force

Problem Statement (short):
A tram travels through n stops. At each stop, a[i] passengers exit
first, then b[i] passengers enter. Find the minimum tram capacity
needed so the passenger count never exceeds it at any point.

Approach:
Simulate the passenger count stop by stop, starting at 0:
- at each stop, subtract a[i] (exits), then add b[i] (entries)
- track the maximum passenger count seen after each stop
The final maximum value is the minimum required capacity.

Time Complexity : O(n)
Space Complexity: O(1) (process input on the fly, no need to store all stops)
"""

def solve():
    n = int(input())
    current = 0
    max_capacity = 0
    
    for _ in range(n):
        a, b = map(int, input().split())
        current -= a
        current += b
        max_capacity = max(max_capacity, current)
    
    print(max_capacity)

solve()