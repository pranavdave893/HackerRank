"""
Input Format

A single line of input containing  space separated integers.

Output Format

Print the 3X3 NumPy array.

Sample Input

1 2 3 4 5 6 7 8 9
Sample Output

[[1 2 3]
 [4 5 6]
 [7 8 9]]

"""


import numpy
a = numpy.array(list(map(int,input().split())))
a.shape = (3,3)
print(
