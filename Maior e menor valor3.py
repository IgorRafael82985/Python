numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

lista = [numero1,numero2,numero3]
lista.sort()

print(f"O maior número é {lista[2]} e o menor número é {lista[0]}")
