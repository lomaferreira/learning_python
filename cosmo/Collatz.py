n = int(input("Escreva um número:\n"))
print(n)
while n != 1:  # testa se n é diferente de 1
    if n % 2 == 0:  # testa se n é par
        n = n//2
        print(n)
    else:
        n = 3*n+1
        print(n)
