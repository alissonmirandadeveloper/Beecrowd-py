x = int(input())
y = int(input())

if x > y:#organiza para ordem crescente
    troca = x
    x = y
    y = troca

soma = 0
for i in range(x+1, y):#para não pegar as extremidades do número
    if i % 2 != 0:
        soma = soma + i
print(soma)
