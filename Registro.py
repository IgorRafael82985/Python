sexo = str(input("Digite seu sexo [M] Masculino ou [F] Feminino: ")).upper()

while sexo not in 'MF' :
     sexo = str(input("Você digitou errado, digite novamente [M] Masculino ou [F] Feminino: ")).upper()
      
print("Registro concluido com sucesso")