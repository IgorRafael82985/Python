anonasc = int(input("Digite seu ano de nascimento: "))

categoria = 2025 - anonasc

if categoria <= 10:
    print("Você tem {} anos sua categoria será Mirim".format(categoria))
elif categoria <= 15:
    print("Você tem {} anos sua categoria será infantil".format(categoria))
elif categoria <= 20:
    print("Você tem {} anos sua categoria será Junior".format(categoria))
elif categoria <= 21:
    print("Você tem {} anos sua categoria será senior".format(categoria))
else:
    print("Você tem {} anos sua categoria será master".format(categoria))
