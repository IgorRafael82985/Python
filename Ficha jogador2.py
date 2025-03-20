time = list()
jogador = dict()
qnt_gols = list()
total_gols = 0
while True:
    jogador.clear()
    jogador['Nome'] = input("Digite o nome do jogador: ")
    partidas = int(input(f"Quantas partidas {jogador['Nome']} Jogou: "))
    for p in range(0,partidas):
        gols = int(input(f"Quantos gols ele fez na partida {p+1}?: "))
        jogador['Gols'] = gols
        qnt_gols.append(gols)
        total_gols += gols
        jogador['total'] = total_gols
        time.append(jogador.copy())
    while True:
        continuar = input("Deseja continuar [S/N]: ").upper()
        if continuar in 'SN':
            break
        print("Erroooooooooo digite apenas sim ou não sua anta: ")
    if continuar == 'N':
        break

print(time)

print('-='*30)
print(f"O campo jogador tem o valor {jogador['Nome']}")
print(f"O campo gols tem o valor {qnt_gols}")
print(f"O campo total tem o valor {jogador['total']}")
print('-='*30)

for c,j in enumerate(qnt_gols):
    print(f"===> Na partida {c+1}, fez {j} Gols")

for k, v in enumerate(time):
    print(f"{k:>3}", end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end=' ')
    print()
print()