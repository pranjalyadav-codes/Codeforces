"""
Problem   : A. Nearly Lucky Number
Link      : https://codeforces.com/problemset/problem/121/A
Rating    : 800
Tags      : implementation, strings

Problem Statement (short):
A lucky number is a positive integer whose digits are only 4 and 7.
Given n (up to 10^18), count how many of its digits are lucky digits
(4 or 7). Print "YES" if that count itself is a lucky number,
otherwise print "NO".

Approach:
Count how many characters in n are '4' or '7'.
Since n has at most 19 digits, count can only range from 0 to 19.
Within that range, the only possible lucky numbers are single-digit:
4 and 7 (two-digit lucky numbers like 44, 47 are impossible since
count can never reach 44). So it's enough to directly check if
count == 4 or count == 7.

Time Complexity : O(d) where d = number of digits in n (at most 19)
Space Complexity: O(1)
"""

s = input()
count = 0
for ch in s:
    if ch == '4' or ch == '7':
        count += 1

if count == 4 or count == 7:
    print("YES")
else:
    print("NO")