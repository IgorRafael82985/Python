soma = 0
for c in range(0, 6):
    numero = int(input("Digite Um número: "))
    if numero %2 == 0:
        soma += numero

print("A somatoria dos números pares digitados é {}".format(soma))
