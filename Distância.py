distancia = int(input("Digite a distancia da sua viagem: "))

if distancia == 200:
    print("Sua passagem vai custar R$ {:.2f}".format(distancia * 0.50))
else: 
    print("Sua passagem vai custar R$ {:.2f}".format(distancia * 0.45))
