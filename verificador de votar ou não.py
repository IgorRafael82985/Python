from datetime import datetime
def votar(anonasc):
    voto = ano_atual - anonasc
    if voto < 18:
        return print(f"Com {voto} anos o voto é opcional")
    if voto >= 18 and voto < 65:
        return print(f"Com {voto} anos o voto é obrigatório")
    if voto > 65:
        return print(f"Com {voto} anos o voto é opcional")
anonasc = int(input("Digite seu ano de nascimento: "))
anoatual = datetime.now()
ano_atual = int(anoatual.strftime("%Y"))
votar(anonasc)