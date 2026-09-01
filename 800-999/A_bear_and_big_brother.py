"""
Problem   : A. Bear and Big Brother
Link      : https://codeforces.com/problemset/problem/791/A
Rating    : 800
Tags      : implementation, math, brute force

Problem Statement (short):
Limak weighs a, Bob weighs b (a <= b). Every year, Limak's weight
triples and Bob's weight doubles. Find the minimum number of full years
after which Limak becomes strictly heavier than Bob.

Approach:
Simulate year by year: multiply a by 3 and b by 2, increment a year
counter, and stop as soon as a > b. Since constraints are tiny
(a, b <= 10), the loop runs very few times before a overtakes b.

Time Complexity : O(log(b/a)) - very small in practice since values grow
                   exponentially and constraints are tiny (<=10)
Space Complexity: O(1)
"""

def solve():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        b *= 2
        years += 1
    print(years)

solve()