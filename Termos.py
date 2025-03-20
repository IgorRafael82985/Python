termos = int(input("Quantos termos serão mostrados: "))

a = 0
b = 1
c = 0
contador = 0

while contador < termos:
    print(f'{c}',end=' ')
    a = b
    b = c
    c = a + b
    contador += 1

print("Fim")