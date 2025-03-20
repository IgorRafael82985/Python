frase = str(input("Digite uma Frase: "))
frase2 = frase.strip()
frase_final = frase2.replace(" ", "")
tamanho = len(frase_final)

for c in range(1, 2):
    frase_invertida = frase_final[::-1]
    if frase_final == frase_invertida:
        print(f'\033[34mA Frase {frase} é um Palíndromo')
    else:
        print(f'\033[32mA frase {frase} não é palíndromo')
    