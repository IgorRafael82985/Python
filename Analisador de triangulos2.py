reta1 = int(input("Digite o comprimento da primeira reta: "))
reta2 = int(input("Digite o comprimento da segunda reta: "))
reta3 = int(input("Digite o comprimento da segunda reta: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("\033[1;33;46mÉ possivel criar um triangulo\033[m")
else:
    print("\033[1;31;40mNão é possível criar um triangulo\033[m")
