import random
vitorias = 0
while True:
    jogador = int(input("Digite um número: "))
    parimpar = str(input("Par ou Ímpar [P/I]: ")).upper()
    computador = random.randint(1,10)
    soma = jogador + computador
    if parimpar == 'P':
        if soma %2 == 0:
            print("-=" *15)
            print("\033[34mVocê ganhou\033m")
            print(f"Você jogou {jogador} e o computador jogou {computador} a soma deu {soma} portando par")
            print("-=" *15)
            vitorias += 1
        else:
            print("-=" *15)
            print("\033[35mVocê perdeu\033m")
            print(f"Você jogou {jogador} e o computador jogou {computador} a soma deu {soma} portando impar")
            print(f"Seu recordes de vitorias é {vitorias}")
            print("-=" *15)
            break
    if parimpar == 'I':
        if soma %2 == 1:
            print("-=" *15)
            print("\033[34mVocê ganhou\033m")
            print(f"Você jogou {jogador} e o computador jogou {computador} a soma deu {soma} portando deu impar")
            print("-=" *15)
            vitorias +=1
        else:
            print("-=" *15)
            print("\033[35mVocê perdeu\033m")
            print(f"Você jogou {jogador} e o computador jogou {computador} a soma deu {soma} portando deu par")
            print(f"Seu recordes de vitorias é {vitorias}")
            print("-=" *15)
            break