import math

a = float(input())
b = float(input())
c = float(input())

delta = b ** 2 - 4 * a * c

if delta == 0:  
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    #print(f'A única raiz é:{raiz1}')
else:
    if delta < 0 or a == 0.0:
        print('Impossível calcular')
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f'R1 =  {raiz1:,.5f}')
        print(f'R2 =  {raiz2:,.5f}')