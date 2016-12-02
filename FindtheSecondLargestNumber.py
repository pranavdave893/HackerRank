/* 

Sample Input

5
2 3 6 6 5
Sample Output

5

*/

x=int(raw_input())
nums=map(int, raw_input().split())
print sorted(list(set(nums)))[-2]
