"""
Problem   : B. Drinks
Link      : https://codeforces.com/problemset/problem/520/B
Rating    : 800
Tags      : math, implementation

Problem Statement (short):
Given n drinks each with a juice percentage p[i], find the resulting
juice percentage when equal parts of all n drinks are mixed together.

Approach:
Mixing equal proportions of n drinks means the resulting juice
percentage is simply the average (arithmetic mean) of all p[i] values:
    answer = sum(p) / n
Print with enough decimal precision (problem allows error up to 1e-4).

Time Complexity : O(n)
Space Complexity: O(n) for storing the input list
"""

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    average = sum(p) / n
    print(f"{average:.12f}")

solve()