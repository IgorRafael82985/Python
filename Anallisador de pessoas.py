temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input("Digite o nome da pessoa: ")))
    temp.append(float(input("Digite o peso KG da pessoa: ")))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    contnuar = input("Deseja continuar [S/N]: ").upper()
    if contnuar == 'N':
        break

print(f"Ao todo foram cadastradas {len(princ)}")
print(f"As pessoas mais pesadas são {maior}", end=' ')
for p in princ:
    if p[1] == maior:
        print(f"[{p[0]}]",end=' ')
print()
print(f"As pessoas mais leves são {menor}", end=' ')
for p in princ:
    if p[1] == menor:
        print(f"[{p[0]}]",end=' ')
print()