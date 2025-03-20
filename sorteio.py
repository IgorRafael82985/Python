from random import randint
def sorteio(lista):
    print("Sorteando os 5 valores:",end=' ')
    for c in range(0,6):
        num = randint(1,10)
        lista.append(num)
        print(f" {num}", end=' ')
def soma(lista):
    soma = 0
    for valores in lista:
        if valores % 2 ==0:
            soma += valores
    print(f"Na lista {lista}, somando os valores pares temos {soma} ", end=' ')
numeros = list()
sorteio(numeros)
print()
soma(numeros)
#Falta finalizar