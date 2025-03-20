def fatorial(fat,show=True):
    """_summary_

    Args:
        fat: Calcula o Fatorial do número
        show: Exibe ou não o calculo de fatorial,_description_. Defaults to True.

    Returns:
        f: retorna o resultado de fatorial
    """
    f = 1
    for c in range(fat, 0, -1):
        if show:
            print(c,end='')
            if c > 1:
                print(" x " ,end='')
            else:
                print(" = ",end='')
        f *= c
    return f
print(fatorial(5,show=True))