def left_rotation(a, d):
    return a[d:] + a[:d]

a = []


quantidade = int(input("Quantos valores serão inseridos: "))

for j in range(quantidade):
    valor = input(f"Digite o valor {j + 1}: ")
    a.append(valor)

print (left_rotation(a, 2))
