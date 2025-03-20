num = int(input("Digite um número entre 0 e 20: "))

while num > 20:
    num = str(input("Fora do intervalo, Digite um número entre 0 e 20: "))

num_extenso = 'Zero', 'Um', 'Dois','Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'

print(f'Você digitou {num_extenso[num]}')