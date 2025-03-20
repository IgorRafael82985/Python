n = tuple(int(input(f"Digite o {cont}° Número: "))  for cont in range(1,5))

print('-='*15)
print(f'O número 9 apareceu {n.count(9)} Vezes')
print('-='*15)
print(f'O número 3 apareceu na {n.index(3) + 1}°' if 3 in n else "Não foi digitado valor 3" )
print('-='*15)
print("Os valores pares digitados saõ:",end='')
print({c for c in n if c % 2 == 0}, end=' ')