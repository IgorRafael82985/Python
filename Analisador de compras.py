total = produtos_comprados = preco_mais_barato = mais_de_mil = 0
produto_barato = ' '
while True:
    nome = str(input("Digite o nome do produto: "))
    valor = float(input("Digite o preço do produto: "))
    total += valor
    produtos_comprados += 1

    if valor > 1000:
        mais_de_mil += 1

    if produtos_comprados == 1:
        produto_barato = nome
        preco_mais_barato = valor
    else:
        if preco_mais_barato > valor:
            produto_barato = nome
            preco_mais_barato = valor
    
    continuar = str(input("Deseja continuar? [S/N]")).upper()

    if continuar != 'S' and continuar != 'N':
        print("Erro tente novamnte")
    if continuar == 'S':
        pass
    if continuar == 'N':
        break

print(f"O total gasto foi R$ {total:.2f}")
print(f"{mais_de_mil} custam mais de R$ 1000")
print(f"{produto_barato} é o produto mais barato da compra e custa {preco_mais_barato:.2f}")