from random import randint
numeros = tuple(randint(1,10) for i in range(1,6))

print('-='*15)
print(f'Os números sorteados foram {numeros}')
print('-='*15)
print(f'O maior número é {max(numeros)}')
print('-='*15)
print(f'O menor Número é {min(numeros)}')
print('-='*15)