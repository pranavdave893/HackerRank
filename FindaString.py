"""
Input Format

The first line of input contains the original string. The next line contains the substring.

Testing things
Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2

"""

str,sub,count=raw_input(),raw_input(),0
for i in range(len(str)):
    if str[i:i+len(sub)] == sub:
        count+=1
print count
