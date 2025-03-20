lista = []
while True:
    numeros = (int(input("Digite um valor: ")))

    if numeros not in lista: 
        print("Valor Adicionado com sucesso")
        lista.append(numeros)
    else:
        print("Esse número já está na lista")

    continuar = input(f"Deseja continuar[S/N]: ").upper()

    if continuar == 'N':
        break
    if continuar == "S":
        pass

lista.sort()
print(f"Os valores digitados são: {lista}")