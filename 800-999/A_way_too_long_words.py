"""
Problem   : A. Way Too Long Words
Link      : https://codeforces.com/problemset/problem/71/A
Rating    : 800
Tags      : strings, implementation

Problem Statement (short):
Given n words, if a word's length is greater than 10, replace it with an
abbreviation: first letter + (count of letters between first and last) +
last letter. Otherwise, leave the word unchanged.

Approach:
For each word:
- If len(word) > 10: output first char + str(len(word) - 2) + last char
- Else: output the word as is

Time Complexity : O(n * L) where n = number of words, L = average word length
Space Complexity: O(1) extra (excluding input/output storage)
"""

def solve():
    word = input()
    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[-1])
    else:
        print(word)

n = int(input())
for _ in range(n):
    solve()