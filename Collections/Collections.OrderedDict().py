/*
 Problem Statement : https://www.hackerrank.com/challenges/py-collections-ordereddict
*/

from __future__ import print_function
from collections import OrderedDict
number_ = int(raw_input())
odict = OrderedDict()
for i in range(number_):
    litem = raw_input().split(' ')
    price = int(litem[-1])
    item_name = " ".join(litem[:-1])
    if odict.get(item_name):
        odict[item_name] += price
    else:
        odict[item_name] = price

for i,v in odict.items():
    print(i,v)
   
/* Another briliant and Short Method */

/* 

from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)
    
    */
