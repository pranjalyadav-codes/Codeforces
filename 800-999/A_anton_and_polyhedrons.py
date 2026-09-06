"""
Problem   : A. Anton and Polyhedrons
Link      : https://codeforces.com/problemset/problem/785/A
Rating    : 800
Tags      : implementation, strings

Problem Statement (short):
Given n polyhedron names (Tetrahedron, Cube, Octahedron, Dodecahedron,
Icosahedron), find the total number of faces across all of them.
Face counts: Tetrahedron=4, Cube=6, Octahedron=8, Dodecahedron=12,
Icosahedron=20.

Approach:
Store the face count for each shape name in a dictionary. For each of
the n input lines, look up the shape name and add its face count to a
running total. Print the total at the end.

Time Complexity : O(n)
Space Complexity: O(1) (fixed-size dictionary)
"""

def solve():
    faces = {
        "Tetrahedron": 4,
        "Cube": 6,
        "Octahedron": 8,
        "Dodecahedron": 12,
        "Icosahedron": 20
    }
    
    n = int(input())
    total = 0
    for _ in range(n):
        name = input().strip()
        total += faces[name]
    
    print(total)

solve()