def cadastro(nome):
    cadastro = dict()
    pessoas = list()
    cadastro.clear()
    cadastro['nome'] = input("Digite o nome: ")
    cadastro['Idade'] = int(input("Digite a idade: "))
    soma +=   cadastro['Idade']
    cadastro['sexo'] = input("Digite o sexo [F/M]").upper()
    pessoas.append(cadastro.copy())