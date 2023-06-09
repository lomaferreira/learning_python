numeroPrimo = int(input("Digite um numero:\n"))
if (numeroPrimo == 0 or numeroPrimo == 1 or numeroPrimo % 2 == 0 and numeroPrimo != 2):
    print(f"{numeroPrimo} não é primo")
elif (numeroPrimo == 2 or numeroPrimo == 3):
    print(f"{numeroPrimo} é primo")
else:
    divisores = 0
    i = 3
    while (i <= numeroPrimo):
        if numeroPrimo % i == 0:  # ver se o único divisor é ele mesmo
            divisores += 1
        i += 1
    # se somente tiver um divisor é primo (não está considerando o 1)
    if divisores == 1:
        print(f"{numeroPrimo} é primo")
    else:
        print(f"{numeroPrimo} não é primo")


