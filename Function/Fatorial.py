def Fatorial(num):
 Resultado_fatorial=1
 for i in range(num,0,-1): #inicia com num; termina quando num for 0; diminiu a cada loop 1 de num
    Resultado_fatorial= Resultado_fatorial * i 
 return Resultado_fatorial
num= int(input('Escreva um número:\n'))
print(Fatorial(num))        