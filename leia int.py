def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[1;031mErroooooooooo\033[m")
        if ok:
            break
    return valor
n = leiaint(("Digite um número: "))
print(f"você acabou de digitar o número {n}")