aluno = dict()

aluno['aluno'] = str(input("Digite o nome do aluno: "))
aluno['Média'] = float(input(f"Digite a média de {aluno['aluno']}: "))

print(f"Nome é igual a {aluno['aluno']}")
print(f"Média é igual a {aluno['Média']}")
if aluno['Média'] >= 7:
    print(f"A situação é igual a aprovado")
else:
    print(f"A situação é igual a reprovado")