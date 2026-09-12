"""
Problem   : A. Game with Integers
Link      : https://codeforces.com/problemset/problem/1899/A
Rating    : 800
Tags      : math, game theory

Problem Statement (short):
Given n, Vanya and Vova alternate adding/subtracting 1, Vanya moves
first. If after Vanya's move the number is divisible by 3, Vanya wins.
If 10 moves pass without that happening, Vova wins. Determine the
winner assuming optimal play.

Approach:
- If n % 3 != 0: Vanya can immediately move +1 or -1 to make it
  divisible by 3 on his very first move -> "First" wins.
- If n % 3 == 0: n is already divisible by 3, but that doesn't count
  (only counts right after Vanya's move). Vanya's first move takes n
  away from being divisible by 3, and from there Vova can always
  move it back to a multiple of 3 on his turn, preventing Vanya from
  winning within the move limit -> "Second" wins.

So the answer is simply:
    "Second" if n % 3 == 0 else "First"

Time Complexity : O(1) per test case
Space Complexity: O(1)
"""

def solve():
    n = int(input())
    if n % 3 == 0:
        print("Second")
    else:
        print("First")

t = int(input())
for _ in range(t):
    solve()