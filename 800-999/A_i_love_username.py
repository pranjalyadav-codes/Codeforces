"""
Problem   : B. I_love_%username%
Link      : https://codeforces.com/problemset/problem/141/B
Rating    : 800
Tags      : implementation

Problem Statement (short):
Given a sequence of n scores in chronological order, count how many
"amazing" performances occur - a performance is amazing if it's
strictly higher than all previous scores, or strictly lower than all
previous scores. The first score never counts.

Approach:
Track running min and max of scores seen so far, starting with the
first score. For each subsequent score:
- if score > current max: amazing, update max
- elif score < current min: amazing, update min
- else: not amazing
Count all amazing occurrences.

Time Complexity : O(n)
Space Complexity: O(n) for storing scores (or O(1) if processed on the fly)
"""

def solve():
    n = int(input())
    scores = list(map(int, input().split()))
    
    if n == 1:
        print(0)
        return
    
    current_max = scores[0]
    current_min = scores[0]
    count = 0
    
    for i in range(1, n):
        s = scores[i]
        if s > current_max:
            count += 1
            current_max = s
        elif s < current_min:
            count += 1
            current_min = s
    
    print(count)

solve()