cont = 0
while True:
    tabuada = int(input("Digite um número para saber sua tabuada (digite um número negativo para parar): "))
    if tabuada < 1:
        break
    while cont < 10:
        cont+=1
        print(f"{tabuada} X {cont} = {tabuada * cont}")
    cont = 0
print("FIm")
