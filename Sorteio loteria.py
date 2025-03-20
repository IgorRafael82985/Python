from random import randint
jogos = int(input("Quantos jogos serão gerados: "))
sorteio = []
for c in range(1,jogos+1):
    for i in range(0,6):
        numeros = randint(1,60)
        if numeros not in sorteio:
            sorteio.append(numeros)
        else:
            numeros = randint(1,60)
            sorteio.append(numeros)
    print(f"Gerando jogo {c} {sorteio}")
    sorteio.clear()