velocidade = int(input("Digite a Velocidade do carro em Km/h: "))
multa = (velocidade - 80)*7


if velocidade > 80:
    print("Limite de velocidade {}km/h excedido sua multa será de R${}".format(velocidade,multa))
else:
    print("Você não excedeu a velocidade continue sua jornada")
