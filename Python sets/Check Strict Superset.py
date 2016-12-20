/* Check if given set A is superset of other sets N. 

Print True if A is superset of all other sets N, otherwie False.
 
Sample Input

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample Output

False

*/

arr = set(raw_input().split())
ans = True
for i in xrange (int(raw_input())):
    bset = set(raw_input().split())
    if not arr.issuperset(bset):
        ans = False
        break
print ans
