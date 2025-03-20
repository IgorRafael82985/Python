from random import randint
from time import sleep
from operator import itemgetter
raking = list()
jogo = {'Jogador1': randint(1,6),
        'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),
        'Jogador4': randint(1,6)}
for v,k in jogo.items():
    print(f"{v} tirou {k} no dado")
    sleep(1)
raking = sorted(jogo.items(),key=itemgetter(1),reverse=True)
print("RAKING DOS JOGADORES")
for i,v in enumerate(raking):
    print(f"{i+1}° Lugar {v[0]} com {v[1]} ")
    sleep(1)