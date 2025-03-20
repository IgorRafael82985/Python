import Moedas

numeros = float(input("Digite um número:R$ "))

print(f"A metade de {Moedas.moeda(numeros)} é {Moedas.metade(numeros,sit=False)}")
print(f"O dobro de {Moedas.moeda(numeros)} é {Moedas.dobro(numeros,sit=True)}")
print(f"Aumentado 10% de {Moedas.moeda(numeros)} fica {Moedas.aumentar(numeros,sit=True)}")
print(f"diminuindo 13% de {Moedas.moeda(numeros)} fica {Moedas.reduzir(numeros,sit=True)}")