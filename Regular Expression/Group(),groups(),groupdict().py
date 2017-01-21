"""
You are given a string S . 
Your task is to find the first occurrence of an alphanumeric character in S (read from left to right) that has consecutive repetitions.

Sample Input

..12345678910111213141516171820212223
Sample Output

1

"""

import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)
