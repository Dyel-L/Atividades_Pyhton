lista = []
pares = []
impares = []
while True:
    num = (int(input('Digite um numero: ')))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    parada = input('Quer continuar? [S/N]')
    if parada in 'Nn':
        break
print(f'A lista completa é {lista}')
print(f'Os valors pares são {pares} ')
print(f'Os valores impares são {impares}')

