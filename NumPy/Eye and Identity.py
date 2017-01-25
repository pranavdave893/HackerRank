"""
Sample Input

3 3
Sample Output

[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
 """
import numpy
N,M = map(int,input().split())
print (numpy.eye(N,M,k=0))
