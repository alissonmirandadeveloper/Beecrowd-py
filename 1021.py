cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um_r = 0
cinquenta_c = 0
vintec_c = 0
dez_c = 0
cinco_c = 0
um_c = 0

valor = float(input())

print('NOTAS:')
cem = valor // 100
resto = valor % 100
print(f'{cem:,.0f} nota(s) de R$ 100.00')

cinquenta = resto // 50
resto = resto % 50
print(f'{cinquenta:,.0f} nota(s) de R$ 50.00')

vinte = resto // 20
resto = resto % 20
print(f'{vinte:,.0f} nota(s) de R$ 20.00')

dez = resto // 10
resto =  resto % 10
print(f'{dez:,.0f} nota(s) de R$ 10.00')

cinco = resto // 5
resto = resto % 5
print(f'{cinco:,.0f} nota(s) de R$ 5.00')


dois = resto // 2
resto = resto % 2
print(f'{dois:,.0f} nota(s) de R$ 2.00')

print('MOEDAS:')
um_r = resto // 1
resto = resto % 1
print(f'{um_r:,.0f} moeda(s) de R$ 1.00')

resto = resto * 100

cinquenta_c = resto // 50
resto = resto % 50
print(f'{cinquenta_c:,.0f} moeda(s) de R$ 0.50')

vintec_c = resto // 25
resto = resto % 25
print(f'{vintec_c:,.0f} moeda(s) de R$ 0.25')

dez_c = resto // 10
resto = resto % 10
print(f'{dez_c:,.0f} moeda(s) de R$ 0.10')


cinco_c = resto // 5
resto = resto % 5
print(f'{cinco_c:,.0f} moeda(s) de R$ 0.05')


um_c = resto // 1
resto = resto % 1
print(f'{um_c:,.0f} moeda(s) de R$ 0.01')
