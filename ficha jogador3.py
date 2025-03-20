jogador = dict()
qnt_gols = list()
jogador['Nome'] = input("Digite o nome do jogador: ")
partidas = int(input("Quantas partidas ele Jogou: "))
total_gols = 0
for p in range(0,partidas):
    gols = int(input(f"Quantos gols ele fez na partida {p+1}?: "))
    jogador['Gols'] = gols
    qnt_gols.append(gols)
    total_gols += gols
    jogador['total'] = total_gols

print('-='*30)
print(f"O campo jogador tem o valor {jogador['Nome']}")
print(f"O campo gols tem o valor {qnt_gols}")
print(f"O campo total tem o valor {jogador['total']}")
print('-='*30)

for c,j in enumerate(qnt_gols):
    print(f"===> Na partida {c+1}, fez {j} Gols")