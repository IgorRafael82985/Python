import Moedas

numeros = float(input("Digite um número:R$ "))

print(f"A metade de {Moedas.moeda(numeros)} é {Moedas.moeda(Moedas.metade(numeros))}")
print(f"O dobro de {Moedas.moeda(numeros)} é {Moedas.moeda(Moedas.dobro(numeros))}")
print(f"Aumentado 10% de {Moedas.moeda(numeros)} fica {Moedas.moeda(Moedas.aumentar(numeros))}")
print(f"diminuindo 13% de {Moedas.moeda(numeros)} fica {Moedas.moeda(Moedas.reduzir(numeros))}")