str=raw_input()
l=list(str)
a=b=c=d=e=False
for i in l:
    if i.isalnum():
        a=True
    if i.isalpha():
        b=True
    if i.isdigit():
        c=True
    if i.islower():
        d=True
    if i.isupper():
        e=True
        
print a
print b
print c
print d
print e
