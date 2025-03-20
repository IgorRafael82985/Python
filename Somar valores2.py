numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite um número inteiro: "))
print("""
[1] Somar
[2] Multiplicar
[3] maior
[4] novos valores
[5] sair do programa
""")
opcao = 0
while opcao != 5:

    opcao = int(input("Digite sua Opção: "))

    if opcao == 1:
        resultado = numero1 + numero2
        print("O resultado da soma foi {}".format(resultado))

    if opcao == 2:
        resultado = numero1 * numero2
        print("O resultado da multiplicação foi {}".format(resultado))

    if opcao == 3:
        if numero1 > numero2:
            print(f'O número {numero1} é maior que {numero2}')
        elif numero1 < numero2:
            print(f'O número {numero2} é maior que {numero1}')
        else:
            print("Ambos os números são iguais")

    if opcao == 4:
        numero1 = int(input("Digite novamente um número inteiro: "))
        numero2 = int(input("Digite novamente um número inteiro: "))