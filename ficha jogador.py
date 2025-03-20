def ficha(n='<Desconhecido>', g=0):
    return print(f"O jogador {n} fez {g} gol(s) no campeonato")
nome = str(input("Digite o nome do jogador: "))
gols = str(input(f"Digite a quantidade de gols marcados por {nome}: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome,gols)