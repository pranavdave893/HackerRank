/*

Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
Sample Output

206

link : https://www.hackerrank.com/challenges/maximize-it

*/

N,M = map(int,raw_input().split(" "))
lst = []
for _ in range(N):
    lst.append([int(x) for x in raw_input().split()][1:])
from itertools import product
combinations = list(product(*lst))

def func(nums):
    return sum(x*x for x in nums) % M

print max(list(map(func,combinations)))
