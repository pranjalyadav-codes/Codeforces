"""
Problem   : A. Sum of Round Numbers
Link      : https://codeforces.com/problemset/problem/1352/A
Rating    : 800
Tags      : math, implementation

Problem Statement (short):
A round number has the form d00...0 (only its leftmost digit is
non-zero). Given n, represent it as a sum of round numbers using the
minimum number of summands.

Approach:
Each non-zero digit of n, when placed at its original position (i.e.
multiplied by the correct power of 10), is itself a round number.
For example, 5009 has non-zero digits 5 (thousands place) and 9
(units place), giving terms 5000 and 9. So:
- Convert n to a string, go through each digit with its position.
- For each non-zero digit, compute digit * 10^(position from right)
  and add it as a term.
- The count of these terms is the minimum number of summands (this is
  optimal since each term must be introduced by a distinct non-zero
  digit - no round number spans multiple original digit positions).

Time Complexity : O(d) per test case, where d = number of digits in n
Space Complexity: O(d) for storing the terms
"""

def solve():
    n = input().strip()
    length = len(n)
    terms = []
    
    for i, digit in enumerate(n):
        if digit != '0':
            power = length - i - 1
            terms.append(digit + '0' * power)
    
    print(len(terms))
    print(' '.join(terms))

t = int(input())
for _ in range(t):
    solve()