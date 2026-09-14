"""
Problem   : B. Soft Drinking
Link      : https://codeforces.com/problemset/problem/41/B
Rating    : 800
Tags      : implementation, math

Problem Statement (short):
n friends want to make toasts. Each toast needs nl ml of drink, one
lime slice, and np grams of salt. Given total drink (k bottles of l
ml each), limes (c limes cut into d slices each), and p grams of
salt, find how many toasts each friend can make equally.

Approach:
Calculate the maximum number of toasts possible from each resource
independently:
- from drink: (k * l) // nl
- from limes: (c * d)  (each slice makes 1 toast, no division needed
  since a slice can't be split further, but the count itself is just
  c*d slices)
- from salt: p // np
Take the minimum of these three values (that's the max total toasts
possible), then divide by n since all friends must make the same
number of toasts, using integer division.

Time Complexity : O(1)
Space Complexity: O(1)
"""

def solve():
    n, k, l, c, d, p, nl, np_ = map(int, input().split())
    
    drink_toasts = (k * l) // nl
    lime_toasts = c * d
    salt_toasts = p // np_
    
    max_total_toasts = min(drink_toasts, lime_toasts, salt_toasts)
    print(max_total_toasts // n)

solve()