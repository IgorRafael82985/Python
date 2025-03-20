cadastro = dict()
pessoas = list()
soma = média =  0
while True:
    cadastro.clear()
    cadastro['nome'] = input("Digite o nome: ")
    cadastro['Idade'] = int(input("Digite a idade: "))
    soma +=   cadastro['Idade']
    cadastro['sexo'] = input("Digite o sexo [F/M]").upper()
    continuar = input("Deseja continuar cadastrando [S/N]: ").upper()
    pessoas.append(cadastro.copy())
    if continuar == 'N':
        break

print(f"Ao todo foram {len(pessoas)} cadastradas")
média = soma / len(pessoas)
print(f"A média de idades foram {média}")
print(f"As mulheres cadastradas foram ", end=' ')
for p in pessoas:
    if p["sexo"] == 'F':
        print(f"{p["nome"]}", end=' ')
print()
print(f"As seguntes pessoas tem idade acima da média: ",end=' ')
for p in pessoas:
    if p["Idade"] >= média:
        print(f"{p["nome"]}", end='')
print()