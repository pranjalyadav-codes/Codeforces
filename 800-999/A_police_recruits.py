"""
Problem   : A. Police Recruits
Link      : https://codeforces.com/problemset/problem/427/A
Rating    : 800
Tags      : implementation, greedy

Problem Statement (short):
Given a sequence of events (positive number = that many officers
hired, -1 = a crime occurs), track available officers over time. Each
crime uses up one available officer if one exists; otherwise it goes
untreated. Count the number of untreated crimes.

Approach:
Maintain a counter of currently available (free) officers, starting
at 0. Process events in order:
- if event > 0: add that many officers to the counter
- if event == -1: if counter > 0, decrement counter (crime handled);
  otherwise increment the untreated count
Print the total untreated count at the end.

Time Complexity : O(n)
Space Complexity: O(n) for storing the events (or O(1) if processed on the fly)
"""

def solve():
    n = int(input())
    events = list(map(int, input().split()))
    
    available = 0
    untreated = 0
    
    for e in events:
        if e == -1:
            if available > 0:
                available -= 1
            else:
                untreated += 1
        else:
            available += e
    
    print(untreated)

solve()