code1, quantity1, value1 = int(input()), float(input()), float(input())
code2, quantity2, value2 = int(input()), float(input()), float(input())

amountPay = quantity1 * value1 + quantity2 * value2
print('VALOR À PAGAR = %.2f' % amountPay)
