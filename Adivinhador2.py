import random

num = int(input("Digite um número entre 0 e 5: "))
num2 = random.randint(0,5)

if num == num2: 
    print("Parabéns!!!!!!! Você acertou o número")
else:
    print("Infelizmente Você não acertou o número")

print("O número sorteado foi {}".format(num2))
