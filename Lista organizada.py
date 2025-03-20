lista = []
for c in range(5):
    numeros = int(input(f"Digite o valor {c}: "))

    if c == 0 or c > lista[-1]:
        lista.append(numeros)
    else:
        pos = 0
        while pos < len(lista):
            if numeros <= lista[pos]:
                lista.insert(pos, numeros)
                break
        pos += 1

print(f"A lista organizada fica: {lista}")