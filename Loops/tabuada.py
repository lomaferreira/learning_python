
i="N"
while i == "N":
    opcoes = int(input(
    "Escolha a operação:\n Adição[0]\n Subtração[1] \n Divisão[2]\n Multipliação[3] \n "))

    if opcoes == 0:
        tabuada = 1
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print(f"{tabuada} + {numero}={tabuada + numero}")
                numero += 1
            tabuada += 1
   
    if opcoes == 1:
        tabuada = 1
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print(f"{tabuada} - {numero}={tabuada - numero}")
                numero += 1
            tabuada += 1
   
    if opcoes == 2:
        tabuada = 1
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print(f"{tabuada} / {numero}={tabuada // numero}")
                numero += 1
            tabuada += 1
   
    if opcoes == 3:
        tabuada = 1
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print(f"{tabuada} X {numero}={tabuada * numero}")
                numero += 1
            tabuada += 1
    sair =input(
     "Deseja sair? \nsim[Y]\n não[N]\n")
    i=sair
    