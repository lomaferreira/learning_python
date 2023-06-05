cigarros=int(input("Quantos cigarros fuma por dia?\n"))
anos=int(input("Quantos anos já fumou?\n"))
reducaoDeVida= ((cigarros*10)*(anos*365))//1440
print(f"Você já perdeu {reducaoDeVida} dias de vida")