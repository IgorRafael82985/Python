def ajuda(com):
    help(com)

#programa principal
comando = ''
while True:
    comando = str(input("biblioteca ou Função: "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
print("Até Logo")