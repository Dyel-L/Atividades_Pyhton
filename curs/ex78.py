lista = []
cont = 0
while True:
    lista.append(int(input('Digite um Numero: ')))
    cont = cont + 1
    parada = input('Quer continuar? [S/N]')
    if parada in 'Nn':
        break
lista.sort(reverse=True)
print(f'Foram digitados {cont} Numeros')
print(f'A lista é {lista}')
if 5 in lista:
    print('O numero 5 esta na lista')
else:
    print('O numero 5 não esta na lista')


