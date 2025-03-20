valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor1 > valor2:
    print("O Número {} é maior que o {}".format(valor1,valor2))
elif valor1 < valor2:
    print("O Número {} é menor que o {}".format(valor1,valor2))
else:
    print("Os Números são iguais")
