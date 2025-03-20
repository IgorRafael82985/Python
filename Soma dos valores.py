soma = total = n = 0
while n != 999:
    n = int(input("Digite um número inteiro (999 para parar): "))
    if n == 999:
        break
    total += 1
    soma += n
print(f"A soma dos {total} valores foi {soma}")