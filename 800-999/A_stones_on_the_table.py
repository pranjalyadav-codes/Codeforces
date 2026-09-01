"""
Problem   : A. Stones on the Table
Link      : https://codeforces.com/problemset/problem/266/A
Rating    : 800
Tags      : implementation, strings

Problem Statement (short):
Given a row of n stones, each colored R, G, or B, find the minimum
number of stones to remove so that no two neighboring stones have the
same color.

Approach:
Scan the string from left to right, comparing each stone to the
previous one. Whenever two adjacent stones have the same color, count
it as one removal (removing the current stone), since removing it
makes the next comparison continue against the earlier, still-kept
stone. This greedy count of "same as previous" pairs gives the minimum
removals needed.

Time Complexity : O(n)
Space Complexity: O(1)
"""

def solve():
    n = int(input())
    s = input()
    
    count = 0
    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1
    print(count)

solve()