/*

Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)

*/

from __future__ import print_function
from itertools import groupby
a = raw_input()
for key, group in groupby(a):
    print ((len(list(group)), int(key)), end=' ')

