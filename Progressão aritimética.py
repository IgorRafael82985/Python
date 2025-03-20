primeirotermo = int(input("Digite o primeiro termo da razão: "))
razao = float(input("Digite a razão do termo: "))
resposta = primeirotermo
contador = 1
total = 0
mais = 10

print("Os dez primeiros termos da razão são")

while mais != 0:
    total += mais
    while contador <= total:
        print('{:.2f}'.format(resposta))
        resposta += razao
        contador +=1
    print("PAUSA")
    mais = int(input("Quantos termos serão mostrados a mais: "))
print("Fim, ao toto foram {} termos na PA".format(total))
