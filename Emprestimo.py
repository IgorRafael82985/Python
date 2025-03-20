casa = int(input("Digite o valor da casa: "))
salario = int(input("Digite o seu salario: "))
anos = int(input("Digite em quantoa anos você vai pagar o emprestimo: "))

pagamento = salario / anos

if salario * 30/100 > 30:
    print("Seu emprestimo foi negado")
else:
    print("Seu emprestimo foi aprovado")

print("sua parcela mensal vai ficar em R$ {:.2f}".format(pagamento))
