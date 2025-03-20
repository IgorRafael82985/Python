def notas(*num,sit=False):
    ficha = dict()
    ficha['total'] = len(num)
    ficha['max'] = max(num)
    ficha['min'] = min(num)
    ficha['media'] = sum(num) / len(num)

    if sit:
        if ficha['media'] <+ 6:
            ficha['sit'] = 'terrivél'
        else:
            ficha['sit'] = 'Ótima'
    return ficha

#programaprincipal
resp = notas(6.5, 7 , 8,sit=False)
print(resp)