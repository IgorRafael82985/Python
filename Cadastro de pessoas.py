contador_maior = 0
homens = 0
mulheres = 0
while True:
    nome = str(input("Digite o nome de uma pessoa: "))
    idade = int(input("Digite a idade de uma pessoa: "))
    sexo = int(input("""Digite o sexo da pessoa: 
    [1] Masculino
    [2] Feminino
    Sua escolha: """))

    if idade > 18:
        contador_maior += 1
    if sexo == 1:
        homens += 1
    if sexo == 2 and idade < 20:
        mulheres += 1

    continuar = str(input("Deseja continuar? [S/N]")).upper()

    if continuar == 'S':
        pass
    if continuar == 'N':
        break

print(f"Foram cadastrados {contador_maior} pessoas abaixo de 18 anos")
print(f"Foram cadastrados {homens} Homens")
print(f"Foram cadastradas {mulheres} mulheres com menos de 20 anos")