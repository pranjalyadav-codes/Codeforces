"""
Problem   : A. Helpful Maths
Link      : https://codeforces.com/problemset/problem/339/A
Rating    : 800
Tags      : implementation, sorting, strings

Problem Statement (short):
Given a sum expression made of digits 1, 2, 3 separated by '+' signs,
rearrange the summands in non-decreasing order and print the new sum.

Approach:
Split the input string on '+' to get individual number strings, sort
them (since they're single-digit 1/2/3, string sort == numeric sort),
then join them back together with '+' in between.

Time Complexity : O(n log n) where n = number of summands (due to sort)
Space Complexity: O(n) for storing the split summands
"""

def solve():
    s = input()
    numbers = s.split('+')
    numbers.sort()
    print('+'.join(numbers))

solve()