time = 'Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco','Vitória','Atlético Mineiro', 'Fluminense', 'Grêmio', 'Juventude', 'RB Bragantino', 'Athletico Paranaense', 'Criciúma', 'Atlético Goianiense', 'Cuiabá'

print('-='*15)
print(f'Os cinco primeiros do campeonato são {time[1:6]}')
print('-='*15)
print(f'Os quatros últimos colocados do campeonato são {time[17:]}')
print('-='*15)
print(f'{sorted(time)}')
print('-='*15)
print(f'O Atlétio Goianiense está na  {time.index('Atlético Goianiense') +1 }° colocação do campeonato')
print('-='*15)