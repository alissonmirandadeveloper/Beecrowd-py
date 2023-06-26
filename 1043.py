v = input().split()
a = float(v[0])
b = float(v[1])
c = float(v[2])
perimetro = 0.0
area = 0.0
if (abs(b-c) < a and a < (b+c)) or  (abs(a-c) < b and b < (a+c)) or (abs(a-b) < c and c < (a+b)):
    perimetro = (a+b+c)
    print(f'Perimetro = {perimetro}')            
else:
    area = (a+b)/2 * c
    print(f'Area = {area}') 
