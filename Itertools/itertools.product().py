/*
This tool computes the cartesian product of input iterables. 
It is equivalent to nested for-loops. 

Example

A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]

Sample Input

 1 2
 3 4
Sample Output

 (1, 3) (1, 4) (2, 3) (2, 4)
 
 */
from itertools import product
print " ".join(map(str,list(product(map(int,raw_input().split()),map(int,raw_input().split())))))
