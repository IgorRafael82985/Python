primeirotermo = int(input("Digite o primeiro termo da razão: "))
razao = float(input("Digite a razão do termo: "))
contador = 0

print("Os dez primeiros termos da razão são")

resposta = primeirotermo

while contador < 10:
    print('{:.2f}'.format(resposta))
    resposta = resposta + razao
    contador +=1
