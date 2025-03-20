from datetime import date
menores = 0
maiores = 0
ano_atual = date.today().year

for c in range (1,8):
    anonascimento = int(input("Digite seu ano de nascimento da {}° pessoa: ".format(c)))

    if  ano_atual - anonascimento >= 18:
        maiores += 1
    else:
        menores += 1

print(f'{maiores} Já atingiram a maioridade,enquanto {menores} ainda não atingiram a maioridade')
