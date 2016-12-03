/*

Sample Input

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output

56.00

*/

x=int(raw_input())
abc={}
for i in xrange(x):
    info=raw_input().split(" ")
    score=map(float,info[1:])
    abc[info[0]]=sum(score)/float(len(score))  
print "%.2f" % abc[raw_input()]
