alunos = [[[]]]
cont = 0
while True:
    nome = alunos[0][0].append(input('Nome: '))
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    alunos[0].append(nota1)
    alunos[0].append(nota2)
    media = (nota1 + nota2) / 2
    alunos.append(media)
    cont = cont + 1
    parada = input('Quer continuar?[S/N]')
    if parada in 'Nn':
        break
for nomes in alunos[0][0]:
    print(f'Nome: {nomes} ')
for medias in alunos:
    print(f'Media: {medias}')



