"""
Problem   : A. Word
Link      : https://codeforces.com/problemset/problem/59/A
Rating    : 800
Tags      : implementation, strings

Problem Statement (short):
Given a word with mixed uppercase/lowercase letters, convert it to all
lowercase or all uppercase - whichever requires changing fewer letters.
If uppercase count is strictly greater than lowercase count, output the
word in uppercase; otherwise (including ties), output it in lowercase.

Approach:
Count how many characters in the string are uppercase using isupper().
- if uppercase_count > len(s) - uppercase_count (i.e. more than half):
    print the word in uppercase
- else:
    print the word in lowercase (covers both "more lowercase" and "tie")

Time Complexity : O(n) where n = length of the word
Space Complexity: O(n) for the converted string
"""

def solve():
    s = input()
    upper_count = sum(1 for ch in s if ch.isupper())
    lower_count = len(s) - upper_count
    
    if upper_count > lower_count:
        print(s.upper())
    else:
        print(s.lower())

solve()