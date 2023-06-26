import math
a, b, c = float(input()), float(input()), float(input())

PI = 3.14159

triangle = (a*c) / 2
circle = PI * math.pow(c, 2)
trapeze = ((a + b)*c) / 2
squere = b * b
rectangle = a * b

print('TRIANGULO: %.3f' % triangle)
print('CIRCULO: %.3f' % circle)
print('TRAPEZIO: %.3f' % trapeze)
print('QUADRADO: %.3f' % squere)
print('RETÂNGULO: %.3f' % rectangle)



