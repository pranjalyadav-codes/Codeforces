"""
Problem   : A. Amusing Joke
Link      : https://codeforces.com/problemset/problem/141/A
Rating    : 800
Tags      : implementation, strings, sorting

Problem Statement (short):
Given two names (guest and host) and a pile of letters, check if the
pile is exactly a permutation of the combined letters of both names -
no letters missing, no extra letters.

Approach:
Concatenate the guest and host names, sort the combined letters, and
sort the pile letters. If both sorted strings are equal, the pile is
a valid rearrangement, so print "YES". Otherwise print "NO".

Time Complexity : O(n log n) where n = total length of the strings
Space Complexity: O(n) for the sorted strings
"""

def solve():
    guest = input()
    host = input()
    pile = input()
    
    combined = sorted(guest + host)
    pile_sorted = sorted(pile)
    
    if combined == pile_sorted:
        print("YES")
    else:
        print("NO")

solve()