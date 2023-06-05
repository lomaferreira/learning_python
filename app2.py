'''mult=int(input("Escreva um número:"))
j=mult
i=mult
print(f"Os 10 primeiros multiplos de {j} são:")
while i<=j*10:
    print(i)
    i=i+j
'''
'''
n = int(input("Tabuada com começo em:"))
v= int(input("até:"))
j=1
while j <= v:
   print(f"{n}x{j}={n*j}")
   j+=1
'''
'''
#multiplicação com soma e subtração
number1=int(input("escreva um número:"))
number2=int(input("escreva um número:"))
mult=0
sub=0
while sub<number1*number2:
    mult=mult+number1+number1
    sub=mult-number1
print(sub)    
'''
'''
#divisão com soma e subtração
number1=int(input("escreva um número:"))
number2=int(input("escreva um número:"))
divisao=0
quociente=0
while quociente<number1//number2:
    divisao=number1-number2
    quociente+=1
print(quociente)   
'''

'''
#Juros em 
deposito=int(input("Digite o deposito inicial:"))
depositoMensal=int(input("Digite o deposito mensalmente:"))
txJuros=int(input("Digite a taxa de juros por mês:"))
totalComJuros=0
depositoMensal2=0
i=1
while i<=3:
    totalComJuros+=(deposito+depositoMensal2)*txJuros
    depositoMensal2+=depositoMensal
    print(totalComJuros)
    i+=1
print(f"Total ganho com juros em 24 meses é:{totalComJuros+deposito+depositoMensal2}")
'''

'''
total=0
while True:
    code=int(input("Digite o código do produto:"))
    quantidadeComprada=int(input("Digite a quantidade comprada e 0 para sair:"))
    if quantidadeComprada==0:
        break
    elif code==1:
     total+= quantidadeComprada*0,50
    elif code==2:
     total+= quantidadeComprada*1
    elif code==3:
     total+= quantidadeComprada*4
    elif code==5:
     total+= quantidadeComprada*7
    elif code==9:
     total+= quantidadeComprada*8
    else:
       print("Código inválido")


print(total)  
'''
# PAGINA 93
