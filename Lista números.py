lista = []
while True:
    numeros = int(input(f"Digite um valor: "))
    lista.append(numeros)

    continuar = input(f"Deseja continuar[S/N]: ").upper()

    if continuar == 'N':
        break
    if continuar == "S":
        pass

print("-=" *15)
print(f"Foram digitados {len(lista)} números")
print("-=" *15)
lista.sort(reverse=True)
print(f"A lista em ordem decrescente {lista}")
print("-=" *15)

if 5 in lista:
    print("O 5 está na lista")
    print("-=" *15)
else:
    print("O 5 não está na lista")
    print("-=" *15)