from random import randint
qtdsorteio = int(input('Quantos jogos devem ser sorteados: '))
for i in range(1, qtdsorteio + 1):
    print(f'Jogo {i}:  {randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)}')