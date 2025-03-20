def contador(inicio,fim,passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        for c in range(inicio,fim + 1,passo):
            print(c, end=' ')
        print()
    else:
        for c in range(inicio,fim - 1, -passo):
            print(c, end=' ')
        print()
#programa princpal
print("\nContagem de 1 até 10 de 1 em 1: ")
contador(1,10,1)
print("-="*30)
print("\nContagem de 10 até 1 de 1 em 1: ")
contador(10,1,2)
print("-="*30)
contador(1,10,1)
print("-="*30)
inicio = int(input("Digite o início da contagem: "))
fim = int(input("Digite o fim da contagem: "))
passo = int(input("Digite o passo da contagem: "))
contador(inicio, fim, passo)