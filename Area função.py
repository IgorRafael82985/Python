def area(largura,comprimento):
    area_total = largura * comprimento
    print(f"A área do terreno {largura}x{comprimento} é de {area_total} M²")
#programa principal
print("Controle de terreno")
print("-"*25)
largura = float(input("largura do terreno (M): "))
comprimento = float(input("comprimento do terreno (M): "))
area(largura,comprimento)