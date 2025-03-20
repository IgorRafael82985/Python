cadastro = []
while True:   
    nome = str(input("Digite o nome do aluno: "))
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    mediacalc = (nota1 + nota2) / 2
    cadastro.append([nome, [nota1, nota2], mediacalc])

    continuar = input("Deseja continuar [S/N]: ").upper()

    if continuar == "N":
        break

print(f'{"N°     Nome    Média"}')
for i,c in enumerate(cadastro):
    print(f"{i:<4} {c[0]:<10} {c[2]:8>}")
while True:
    aluno = int(input('Escolha um aluno para mostrar as notas separadamente: '))
    print(f'Aluno: {cadastro[aluno-1][0]}. Notas: {cadastro[aluno-1][1]} e média {cadastro[aluno-1][2]}')
    continuar = input("Deseja continuar [S/N]: ").upper()
    if continuar == "N":
        break