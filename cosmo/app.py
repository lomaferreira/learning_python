sal = float(input())
# Funcionários com o salário de R$400.00 a R$800.00, devem receber um aumento de 15%
if (sal <= 400.00 or sal <= 800.00):
    cal1 = (sal*15/100)
    print(f"{cal1:.2f}")
# aumento de 12%
elif (sal == 800.01 or sal <= 1500.00):
    cal2 = (sal*12/100)
    print(f"{cal2:.2f}")
# aumento de 8%
elif (sal == 1500.01 or sal <= 2000.00):
    cal3 = (sal*8/100)
    print(f"{cal3:.2f}")
# aumento de 6% salário maior que R$2000.00
else:
    cal4 = (sal*6/100)
    print(f"{cal4:.2f}")
