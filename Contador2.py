lista = []
contador = 1
n1 = 0
continuar = 's'
while continuar in 's':
    n1 = int(input("Digite um número: "))
    continuar = input("Deseja contnuar [S/N]").lower()
    lista.append(n1)
    n1 += n1
    contador += 1
    if continuar == 'N':
        break

print(f"Você digitou {len(lista)} Número\n e soma entre eles é {sum(lista)}\n e média foi\n {sum(lista)/len(lista)} e o maior valor é {max(lista)} e o menor valor é {min(lista)}")