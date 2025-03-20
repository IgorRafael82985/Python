numero = int(input("Digite o número que queira saber o fatorial: "))
cont = numero
fatorial = 1
while cont > 0:
    print(f'{cont}' ,end=' ')
    print(' x ' if cont > 1 else ' = ', end=' ')
    fatorial *=  cont
    cont -= 1

print(f'{fatorial}')
