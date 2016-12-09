"""
Sample Input

10
161 182 161 154 176 170 167 171 170 174

O/p

169.375

"""

from __future__ import division
plant=int(raw_input())
height=map(int,raw_input().split())
print sum(set(height))/len(set(height))
