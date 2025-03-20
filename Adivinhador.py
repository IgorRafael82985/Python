import random

computador = random.randint(1,10)
jogador = int(input("Digite um número entre 1 e 10: "))

while computador != jogador:
    jogador = int(input("Você não acertou tente novamente: "))

print("\033[36mVocê Acertou")
