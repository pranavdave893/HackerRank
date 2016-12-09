""" 

Input : hello world
Output : Hello World

"""

x=raw_input()
list=x.strip().split(" ")
for i in range(len(list)):
    a=list[i]
    print a.capitalize(),
