/*

Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK

*/

from __future__ import print_function
from itertools import combinations
s,n=raw_input().split()
for i in range (1,int(n)+1):
    print (*[''.join(i) for i in combinations(sorted(s),int(i))],sep='\n')
