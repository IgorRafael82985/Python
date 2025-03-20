from random import randint
def maior(valores1,valores2,valores3,valores4,valores5):
    print('-='*30)
    print()
    print(f"{valores1} foram analisados {len(valores1)} e o maior valor é {max(valores1)}",end=' ')
    print()
    print('-='*30)
    print()
    print(f"{valores2} foram analisados {len(valores2)} e o maior valor é {max(valores2)}",end=' ')
    print()
    print('-='*30)
    print()
    print(f"{valores3} foram analisados {len(valores3)} e o maior valor é {max(valores3)}",end=' ')
    print()
    print('-='*30)
    print()
    print(f"{valores4} foram analisados {len(valores4)} e o maior valor é {max(valores4)}",end=' ')
    print()
    print('-='*30)
    print()
    print(f"{valores5} foram analisados {len(valores5)-1} e o maior valor é {max(valores5)}",end=' ')
    print()
    print('-='*30)
    print()
valores1 = [randint(1,20)for c in range(1,9)]
valores2 = [randint(1,20)for c in range(1,11)]
valores3 = [randint(1,20)for c in range(1,21)]
valores4 = [randint(1,20)for c in range(1,15)]
valores5 = [0]
maior(valores1,valores2,valores3,valores4,valores5)