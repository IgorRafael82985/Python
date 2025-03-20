num = int(input("digite um número inteiro: "))

print('''Selecione uma das opções abaixo
      [1] Para converter para Binario
      [2] Para converter para Hexadecimal
      [3] Para converter para Octal''')
opcao = int(input("Digite sua opção: "))

if opcao == 1:
    print("O número {} convertido em binario fica {}".format(num, bin(num)))
elif opcao == 2:
    print("o numero {} convertido para Hexadecimal fica {}".format(num, hex(num)))
elif opcao == 3:
    print("o número {} convertido para Octal fica {}".format(num,oct(num)))
else:
    print("Opção invalida")
