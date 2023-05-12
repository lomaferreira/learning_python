def Triangulo(lado1, lado2, lado3):
    if (lado1 == lado2 and lado1 == lado3):  # Todos os lados iguais
        return' Equilátero'
    elif (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):  # Só um lado igual
        return'Isósceles'
    else:
       return'Escaleno'  #Nenhum lado igual

print(Triangulo(1, 2, 3))
