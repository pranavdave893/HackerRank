/*
The input consists of three lines. The first line contains the integer N , denoting the length of the list. The next line consists of N space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer K , denoting the number of indices to be selected.

Output Format

Output a single line consisting of the probability that at least one of the K indices selected contains the letter:'a'.

Sample Input

4 
a a c d
2

Sample Output

0.8333

*/

from __future__ import print_function,division
from itertools import combinations
N=int(raw_input().strip())
lst=raw_input().strip().split()
K=int(raw_input().strip())
c=0
t=0
for i in combinations(lst,K):
    t+=1
    if 'a' in i:
        c=c+1
print (c/t)
