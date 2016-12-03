/*
Sample Input

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output

Berry
Harry
*/

stu=[[raw_input(),float(raw_input())] for _ in range(int(input()))]
second_highest=sorted(list(set([marks for name,marks in stu])))[1]
print('\n'.join([name for name,marks in sorted(stu) if marks==second_highest]))


