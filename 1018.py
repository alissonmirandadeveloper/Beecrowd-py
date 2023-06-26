numero = int(input())

cem = numero // 100
cinquenta = (numero % 100) // 50
vinte = ((numero % 100) % 50) // 20
dez = (((numero % 100) % 50) % 20) // 10
cinco = ((((numero % 100) % 50) % 20) % 10) // 5
dois = (((((numero % 100) % 50) % 20) % 10) % 5) // 2
um = ((((((numero % 100) % 50) % 20) % 10) % 5) % 2) // 1

print(numero)
print(f'{cem} nota(s) de R$ 100,00')
print(f'{cinquenta} nota(s) de R$ 50,00')
print(f'{vinte} nota(s) de R$ 20,00')
print(f'{dez} nota(s) de R$ 10,00')
print(f'{cinco} nota(s) de R$ 5,00')
print(f'{dois} nota(s) de R$ 2,00')
print(f'{um} nota(s) de R$ 1,00')



