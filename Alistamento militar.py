anonasc = int(input("Digite su ano de nascimento: "))

resposta = 2025 - anonasc

print("Sua idade é {}".format(resposta))

if resposta < 18:
    print("Você ainda vai poder se alistar no serviço militar. Faltam {} anos para o alistamento".format(18 - resposta))
elif resposta == 18:
    print("Você já está na idade de se alistar no serviço militar")
else:
    print("Você já passou da hora de se alistar no serviço militar. Inclusive Já esta {} anos atrasados" .format(resposta - 18))
