"""
Sample Input

4  
4.0O0
-1.00
+4.54
SomeRandomStuff
Sample Output

False
True
True
False

"""
import re
for _ in range(int(input())):
    print(bool(re.search(r"^[+|-]?[0-9]*[.][0-9]+$",input())))
