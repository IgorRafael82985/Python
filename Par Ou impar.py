par = []
impar = []
for c in range(0,8):
    verificador = int(input(f"Digite o {c+1}° valor inteiro: "))

    if verificador % 2 == 0:
        par.append(verificador)
    else:
        impar.append(verificador)

print(f"os valores impares digitados são {impar}")
print(f"Os valores pares digitados são {par}")