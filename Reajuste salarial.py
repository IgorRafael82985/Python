salario = float(input("Digite seu salário: "))

if salario > 1250.00:
    print("Seu reajuste salarial ficou em {}".format((salario * 10/100) + salario))
else:
    print("seu reajuste salarial ficou em {}".format((salario * 15/100) + salario))
