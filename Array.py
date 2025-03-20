def reverseArray_1(a):
    b = []
    for i in a:
        b.insert(0,i)
    return b

def reverseArray_2(a):
    return a [::-1]

def reverseArray_3(a):
    a = a.reverse()
    return a
a = []

quantidade = int(input("Quantos valores serão inseridos: "))

for j in range(quantidade):
    valor = input(f"Digite o valor {j + 1}: ")
    a.append(valor)


print (reverseArray_1(a))
print (reverseArray_2(a))

reverseArray_3(a)
print (a)

reverseArray_3(a)
print (a)
