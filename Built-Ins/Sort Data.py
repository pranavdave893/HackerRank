'''
https://www.hackerrank.com/challenges/python-sort-sort

Sample Input

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
Sample Output

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
'''
from operator import itemgetter
n,m = map(int, input().split())
mylist = [list(map(int,input().split())) for _ in range(n)]
k = int(input()) 
[print(*element) for element in sorted(mylist,key=itemgetter(k))]
