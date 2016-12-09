"""
No Idea!

Sample Input

3 2
1 5 3
3 1
5 7

Sample Output

1

You gain 1 unit of happiness for elements 3 and 1 in set A. You lose 1 unit for 5 in set B. The element 7 in set does not exist in the array so it is not included in the calculation.

Hence, the total happiness is 2-1=1.

"""
n,m=raw_input().split()
arr=raw_input().split()
A=set(raw_input().split())
B=set(raw_input().split())
CA=0
for i in arr:
    if (i in A):
        CA+=1
    elif (i in B):
        CA-=1
print CA
