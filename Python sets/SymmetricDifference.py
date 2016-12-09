"""
Sample Input

4
2 4 5 9
4
2 4 11 12

Sample Output
5
9
11
12

"""

raw_input()
s1=set(map(int, ((raw_input().split()))))
raw_input()
s2=set(map(int, ((raw_input().split()))))
ss = sorted(s1 ^ s2)
for i in ss:
    print(i)
