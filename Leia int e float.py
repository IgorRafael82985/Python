def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError,ValueError):
            print('O valor digitado não confere com o tipo de dado que deveria ser inserido')
        else:
            return n
def leiafloat(msg):
    while True:
        try:
            f = float(input(msg))
        except (TypeError,ValueError):
            print('O valor digitado não confere com o tipo de dado que deveria ser inserido')
        else:
            return f
        
n = leiaint(("Digite um número inteiro: "))
f = leiafloat(("Digite um número float: "))


print(f"você acabou de digitar o número inteiro {n} e o número float {f}")
