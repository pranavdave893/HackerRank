*/
Probelm statement : https://www.hackerrank.com/challenges/py-collections-namedtuple

*/

from collections import namedtuple
N, Grade = input(), namedtuple('Grade', raw_input())
Avg = sum(float(Grade(*raw_input().split()).MARKS) for _ in xrange(N))/N
print "%.2f" % Avg
