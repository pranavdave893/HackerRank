/*

Link to problem : https://www.hackerrank.com/challenges/collections-counter

*/

from collections import Counter
_,shoe,total=raw_input(),Counter(raw_input().split()),0

for i in range(int(raw_input())):
    size,price=raw_input().split()
    if shoe[size]:
               total+=int(price)
               shoe[size]=shoe[size]-1
               
print total
