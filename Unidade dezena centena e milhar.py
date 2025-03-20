num = int(input("Digite um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("Analisando o número {}".format(num))

print("Unidade é {}".format(u))
print("dezena é {}".format(d))
print("centena é {}".format(c))
print("milhar é {}".format(m))
