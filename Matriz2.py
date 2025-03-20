matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = (int(input(f"Digite um valor para [{i+1},{j+1}]: ")))
        linha.append(valor)
    matriz.append(linha)

print("\nA matriz ficou:")
for linha in matriz:
    print(linha)