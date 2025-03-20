import random
jogadas = ('pedra','papel','tesoura')
computador = random.randint(0, 2)

print('''Suas opcções 
      [0] Pedra
      [1] Papel
      [2] Tesoura''')

jogador = int(input("Escolha sua jogada: "))

print("-=" * 15)
print("jogador jogou {}".format(jogadas[jogador]))
print("-=" * 15)
print("Computador jogou {}".format(jogadas[computador]))
print("-=" * 15)

if computador == 0: #computador joga pedra
    if jogador  == 0:
        print("Empate!!!!!!")
    elif jogador == 1:
        print("Jogador Ganhou!!!!!!!")
    elif jogador == 2:
        print("Computador Ganhou!!!!!!")
    else:
        print("Jogada invalida")
elif computador == 1: #computador joga papel
    if jogador  == 0:
        print("Computador Ganhou!!!!!!")
    elif jogador == 1:
        print("Empateeeeeeeeee!!!!!!!")
    elif jogador == 2:
        print("Jogador Ganhou")
    else:
        print("Jogada Invalida")
elif computador == 2: #computador joga tesoura
    if jogador  == 0:
        print("Jogador Ganhou!!!!!!")
    elif jogador == 1:
        print("Computador Ganhou!!!!!!!")
    elif jogador == 2:
        print("Empateeeeeeeeeee!!!!!!!")
    else:
        print("Jogada Invalida")
