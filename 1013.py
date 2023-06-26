import math
a = int(input())
b = int(input())
c = int(input())

maiorAB = (a + b + math.fabs(a-b))/2
maiorABC = (maiorAB + c + math.fabs(maiorAB - c)) / 2

print(f'{maiorABC} é maior')
