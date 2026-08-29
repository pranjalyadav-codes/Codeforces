"""
==================================================
Problem: A. Watermelon
Platform: Codeforces
Problem Link: https://codeforces.com/problemset/problem/4/A
==================================================

PROBLEM:
--------
Given an integer w representing the weight of a watermelon.

We need to determine whether the watermelon can be divided
into two parts such that:

1. Both parts have positive integer weights.
2. Both parts have the same weight.

If possible, print "YES", otherwise print "NO".


KEY OBSERVATION: 
----------------
Suppose the two parts have equal weight x.

Then:

    w = x + x
    w = 2 * x

Therefore, w must be EVEN.

So:

    w % 2 == 0  ->  YES
    w % 2 != 0  ->  NO

Important:
w = 2 is also valid because:

    2 = 1 + 1

Both parts are positive and equal.


APPROACH:
---------
1. Read the value of w.
2. Check whether w is divisible by 2.
3. If w is even, print "YES".
4. Otherwise, print "NO".


EXAMPLE 1:
----------
Input:
8

Explanation:
8 can be divided into:

    4 + 4

Both parts are positive and equal.

Output:
YES


EXAMPLE 2:
----------
Input:
5

Explanation:
5 cannot be divided into two equal positive integers.

Output:
NO


TIME COMPLEXITY:
----------------
O(1)

We perform only one modulo operation.


SPACE COMPLEXITY:
-----------------
O(1)

We use only one variable.


IMPORTANT THING TO REMEMBER:
----------------------------
The condition is simply:

    w % 2 == 0

Do NOT use:

    w > 2

because w = 2 is a valid answer.


==================================================
SOLUTION
==================================================
"""

w = int(input())
if w % 2 == 0:
    print("YES")
else:
    print("NO")

