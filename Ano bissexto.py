ano = int(input("Digite o ano que vc quer analisar: "))

if ano %100==0: 
    if ano %400==0:
        print("Esse ano é bissexto")
    else:
        print("Esse ano Não é bissexto")
else:
    if ano %4 == 0:
        print("Esse ano é bissexto")
    else:
        print("Esse ano não é bissexto")
