lista_par = []
lista_impar = []
lista_numeros = []
while True:
    numeros = int(input(f"Digite um valor: "))
    lista_numeros.append(numeros)

    if numeros % 2 == 0:
        lista_par.append(numeros)
    else:
        lista_impar.append(numeros)

    continuar = input(f"Deseja continuar[S/N]: ").upper()

    if continuar == 'N':
        break
    if continuar == "S":
        pass

print("-=" *15)
print(f"Os números digitados foram: {lista_numeros}")
print("-=" *15)
print(f"A lista dos números pares são {lista_par}")
print("-=" *15)
print(f"A lista dos números Ímpares são {lista_impar}")
print("-=" *15)