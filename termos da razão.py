primeirotermo = int(input("Digite o primeiro termo da razão: "))
razao = float(input("Digite a razão do termo: "))

print("Os dez primeiros termos da razão são")

resposta = primeirotermo

for c in range(1, 11):
    print('{:.2f}'.format(resposta))
    resposta = resposta + razao
