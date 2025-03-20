lista = []

for c in range(1,6):
    peso = str(input("Digite um KG o peso da {}° Pessoa: ".format(c)))

    lista+=[peso]
    lista.sort()

print(f'O maior peso é {lista[4]} e o menor é {lista[0]}')
