import Moedas

numeros = float(input("Digite um número:R$ "))

print(f"A metade de {numeros} é {Moedas.metade(numeros)}")
print(f"O dobro de {numeros} é {Moedas.dobro(numeros)}")
print(f"Aumentado 10% de {numeros} fica {Moedas.aumentar(numeros)}")
print(f"diminuindo 13% de {numeros} fica {Moedas.reduzir(numeros)}")