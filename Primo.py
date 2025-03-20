nuumero = int(input("\033[34mDigite um número inteiro: "))
contprimo = 0

for c in range(1, nuumero+1):
    if nuumero%c == 0:
        print("\033[33m{} É um divisivel por {}".format(nuumero,c))
        contprimo += 1
    else:
        print("\033[31m{} Não é divisivel por {}".format(nuumero,c))

if contprimo == 2:
    print(f'\033[35mO Número {nuumero} é primo')
else:
    print(f'\033[36mO Número {nuumero} não é um número primo')