valores = []
for c in range(0,5):
    valores.append(int(input(f"Digite o valor da posição {c}: ")))

maior = [i for i,v in enumerate(valores) if v == max(valores)]
menor = [i for i,v in enumerate(valores) if v == min(valores)]

print(f"O maior valor é {max(valores)} na posição: {maior} ")
print(f"O menor valor é {min(valores)} na posição: {menor}")