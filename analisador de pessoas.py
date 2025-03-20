soma_idade = 0
mulheres = 0
homens = 0
homem_mais_velho = ' '

for c in range(1,5):
    nome = str(input("Digite o nome da {}° pessoa: ".format(c)))
    idade = int(input("Digite a idade da {}° pessoa: ".format(c)))
    sexo = int(input("Digite o genero da {}° pessoa \n [1] Feminino \n [2] Masculino \n Sua Opção: ".format(c)))
    print('-='*20)
    
    soma_idade +=idade
    media = soma_idade/4

    if c == 1 and sexo == 2:
            homens = idade
            homem_mais_velho = nome
    if sexo == 2 and idade > homens:
            homens = idade
            homem_mais_velho = nome     
    if sexo == 1 and idade < 20:
            mulheres += 1    

print(f'A media de idade do grupo é {media}')
print(f'A quantidade de mulheres abaixo dos vinte anos é {mulheres}')
print(f'O Homem mais velho tem {homens} anos e seu nome é {homem_mais_velho}')
