print("----------------------------------------------------------------")
print("Digite 1 caso o pagamento seja à vista em dinheiro/cheque")
print("Digite 2 caso o pagamento seja à vista no cartão")
print("Digite 3 caso o pagamento seja 2x no cartão")
print("Digite 4 caso o pagamento seja 3x no cartão")
print("----------------------------------------------------------------")

opcao = str(input("Digite de 1 a 4 conforme seja seu pagamento: "))

produto = int(input("Digite o valor do seu produto: "))

desconto = produto - (produto * 10/100)

cartao = produto - (produto * 5/100)

juros = produto + (produto * 20/100)


if opcao == "1":
    print("O seu produto com o desconto será de R$ {:.2f}".format(desconto))
elif opcao == "2":
    print("O Seu produto com desconto será de R$ {:.2f}".format(desconto))
elif opcao == "3":
    print("Essa opção de pagamento não possui desconto, portanto o valor final mais a parcela será de R$ {:.2f} nos proximos dois meses".format(produto / 2))
elif opcao == "4":
    parcela = int(input("Digite o tota de parcelas que serão cobradas: "))
    totalparcelado = juros / parcela
    print("O total a ser pago será R$ {:.2f}, parcelado será R$ {:.2f}".format(juros,totalparcelado))
else:
    print("Opção invalida tente novamente")
