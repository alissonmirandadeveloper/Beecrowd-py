v = input()
d = v.split(" ")
code = int(d[0])
qtd = int(d[1])

if code == 1:
    price = 4.00
elif code == 2:
    price = 4.50
elif code == 3:
    price = 5.00
elif code == 4:
    price = 2.00
elif code == 5:
    price = 1.50

print(f'Total: R$ {qtd*price:.2f}')
