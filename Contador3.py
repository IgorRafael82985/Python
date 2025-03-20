contador = resultado = n2 = n1 = 0

while n1 != 999:
    n1 = int(input("Se deseja continuar digite outro número se não digite 999: "))
    if n1 != 999:
        resultado += n1
        contador += 1

print(f'Fim a soma total foi {resultado} e foram digitados {contador} Números')