matriz = []
coluna3 = pares = linha2 = 0
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite um valor para a posição [{i+1},{j+1}]: "))
        if valor % 2 == 0:
            pares += valor           
        linha.append(valor)
    matriz.append(linha)

linha2 = max(matriz[1])

for i in range(3):
    coluna3 += matriz[i][2]

for linha in matriz:
    print(linha)

print(f"A soma de todos os valores pares é {pares}")
print(f"A soma de todos os valores da coluna 3 é {coluna3}")
print(f"O maior valor da linha 2 é {linha2}")