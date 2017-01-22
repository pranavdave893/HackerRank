"""
Input Format

The first line contains the space separated values of N and M. 
The next N lines contains the space separated elements of M columns.

Output Format

First, print the transpose array and then print the flatten.

Sample Input

2 2
1 2
3 4
Sample Output

[[1 3]
 [2 4]]
[1 2 3 4]

"""
import numpy
N,M= map(int,input().split())
list1=[list(map(int,input().split())) for _ in range(N)]
print (numpy.transpose(list1))
print (numpy.array(list1).flatten())
