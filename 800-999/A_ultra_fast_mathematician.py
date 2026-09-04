"""
Problem   : A. Ultra-Fast Mathematician
Link      : https://codeforces.com/problemset/problem/61/A
Rating    : 800
Tags      : implementation, strings

Problem Statement (short):
Given two binary strings of equal length, produce a new string where
the i-th digit is 1 if the i-th digits of the two inputs differ, and 0
if they are the same (essentially digit-wise XOR).

Approach:
Read both strings. For each position i, compare the characters:
- if they differ: output '1'
- if they are the same: output '0'
Build the result character by character and print it, preserving
leading zeros.

Time Complexity : O(n) where n = length of the strings
Space Complexity: O(n) for the result string
"""

def solve():
    a = input()
    b = input()
    
    result = []
    for i in range(len(a)):
        if a[i] != b[i]:
            result.append('1')
        else:
            result.append('0')
    
    print(''.join(result))

solve()