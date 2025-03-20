nome = str(input("Digite seu nome: "))

if nome == 'Igor' :
    print("Que nome lindo o segundo mais lindo que já ouviu")
elif nome == 'Inácio' or nome == 'Luciano' or nome == 'Matheus':
    print("Puxa que nome extraordinario")
elif nome in 'Ana claudia jussara lula mlusco bob esponja':
    print("O nome mais normal que já ouvi")
else:
    print("Seu nome é tão nomal que eu nunca ouvi falar")

print("Tenha um bom dia {}!".format(nome))
