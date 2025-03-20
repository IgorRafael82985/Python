def metade(n,sit=True):
    if sit:
        return (f'R$ {n / 2}')
    else:
        return n / 2
    
def dobro(n,sit=True):
    if sit:
        return (f'R$ {n * 2}')
    else:
        return n * 2

def aumentar(n,sit=True):
    if sit:
        return (f'R$ {n + (n * 10/100)}')
    else:
        return n + (n * 10/100)

def reduzir(n,sit=True):
    if sit:
        return (f'R$ {n - (n * 13/100)}')
    else:
        return n - (n * 13/100)

def moeda(n,sit=True):
    if sit:
        return (f'R$ {n}')
    else:
        return (f'{n}')
    
def resumo(n=0,a=10,r=13):
    print('-'*40)
    print(f'Resumo da análise de R$ {n}')
    print('-'*40)
    print(f'a metade é R$ {n / 2}')
    print(f'o dobro é R$ {n * 2}')
    print(f'o aumento de {a}% em R$ {n} é R$ {n + (n * a/100)}')
    print(f'a redução de {r}% em R$ {n} é R$ {n - (n * r/100)}')
    print('-'*40)