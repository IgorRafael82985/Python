frase = str(input("Digite sua frase: ")).upper().strip()

print("A Letra a aparececeu {} vezes na frase".format(frase.count("A")))
print("A primeira letra a apareceu pela primeira vez na posição {}".format(frase.find('A') + 1))
print("A Última letra A apareceu na posição {}".format(frase.rfind('A') + 1))
