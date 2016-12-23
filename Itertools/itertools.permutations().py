/*

Sample Input

HACK 2
Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
*/

from __future__ import print_function
from itertools import permutations
s,n=raw_input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')
