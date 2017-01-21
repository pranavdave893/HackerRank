"""
https://www.hackerrank.com/challenges/re-findall-re-finditer

Sample Input

rabcdeefgyYhFjkIoomnpOeorteeeeet
Sample Output

ee
Ioo
Oeo
eeeee

"""

import re

a = input()
b = "AEIOUaeiou"
c = "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})(?=[%s])" % (c, b, c), a)
if m:
    [print(z) for z in m]
else:
    print("-1")
