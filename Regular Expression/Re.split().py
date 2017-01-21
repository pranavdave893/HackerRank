"""
Sample Input

100,000,000.000
Sample Output

100
000
000
000

"""
import re
[print(i) for i in re.split("[,.]",input()) if not i == "" ]

import re
[print(i) for i in re.split("[,.]",input()) if i ]
