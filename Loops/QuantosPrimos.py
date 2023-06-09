N = int(input("Quantos números primos você quer?"))
primo = 2  # número que será testado
j = 0  # contador para alcançar os N números
while j < N:
    # testa todos os números não primos
    if primo % 2 == 0 and primo != 2:
        primo += 1
    elif primo % 3 == 0 and primo != 3:
        primo += 1
    elif primo % 5 == 0 and primo != 5:
        primo += 1
    # imprimi o número primo
    else:
        print(primo)
        primo += 1
        j += 1
