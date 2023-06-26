totalDays = int(input())

year = totalDays // 365
month = (totalDays % 365) // 30
days = ((totalDays % 365) % 30)

print(f'{year} ano(s)')
print(f'{month} mes(es)')
print(f'{days} dia(s)')
