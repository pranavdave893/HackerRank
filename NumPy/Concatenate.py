"""
Problem Statement : https://www.hackerrank.com/challenges/np-concatenate

Sample Input

4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 
Sample Output

[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
 
 """
import numpy
print(numpy.array([list(map(int,input().split())) for _ in range(sum(list(map(int,input().split()))[:2]))]))
