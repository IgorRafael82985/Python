from datetime import datetime
dados = dict()
ano = 0

dados['Nome'] = str(input("Digite o nome da pessoa: "))
dados['nascimento'] = int(input("Digite o ano de nascimento da pessoa: "))
dados['CTPS'] = int(input("Digite o número de sua carteira de trabalho(0 Não possui carteira de trabalho): "))
dados['Salário'] = float(input("Digite o seu salário R$: "))
dados['Contratação'] = int(input("Digite o ano de sua contratação: "))
ano_aposentadoria = dados['Contratação'] + 35
dados['Aposentadoria'] = ano_aposentadoria - dados['nascimento']
anoatual = datetime.now()
ano_atual = anoatual.strftime("%Y")
ano = int(ano_atual)
dados['Idade'] = ano - dados["nascimento"]

print(f"O nome tem o valor {dados['Nome']}")
print(f"A idade tem o valor de {dados['Idade']}")
print(f"O CTPS tem o valor de {dados['CTPS']}")
print(f"O salário tem o valor de {dados['Salário']}")
print(f"Contratação tem o valor de {dados['Contratação']}")

if dados['CTPS'] == 0:
    pass
else:
    print(f"A Aposentedoria tem o valor de {dados['Aposentadoria']}")