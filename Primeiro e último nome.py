nome = str(input("Digite seu nome completo: ")).strip()
n = nome.split()

print("Seu primeiro nome é {}".format(n[0]))
print("Seu ùltimo nome é {}".format(n[len(n)-1]))
