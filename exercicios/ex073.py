from operator import index

brasileiro = ('Flamengo', 'Palmeiras', 'Athletico-pr', 'Fluminense', 'Bahia', 'Cruzeiro', 'Atlético-MG',
              'Santos', 'Bragantino', 'São Paulo', 'Coritiba', 'EC Vitoria', 'Botafogo', 'Vasco da Gama',
              'Mirasol', 'Corinthians', 'Internacional', 'Grêmio', 'Remo', 'Chapecoense')
print(brasileiro[:5])
print(brasileiro[-4:])
print(sorted(brasileiro))
print((brasileiro.index('Chapecoense') + 1))