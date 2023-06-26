name = input()
salary = float(input())
salesAmount = float(input())

commission = salesAmount * 0.15
totalSalary = salary + commission

print('TOTAL = R$ %.2f' % totalSalary)
