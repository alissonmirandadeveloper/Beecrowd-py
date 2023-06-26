v = input().split()
a = int(v[0])
b = int(v[1])
c = int(v[2])

if (a < b) and (a < c):
    if(b < c):
        print(a)
        print(b)
        print(c)
    else:
        print(a)
        print(c)
        print(b)
if (b < a) and (b < c):
    if(a < c):
        print(b)
        print(a)
        print(c)
    else:
        print(b)
        print(c)
        print(a)
if (c < b) and (c < a):
    if(a < b):
        print(c)
        print(a)
        print(b)
    else:
        print(c)
        print(b)
        print(a)
print()   
for n in v:
    print(n)