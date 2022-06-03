temp = []
princ = []
cadas = maior = menor = 0
while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if maior < temp[1]:
            maior = temp[1]
        if menor > temp[1]:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    cadas = cadas + 1
    parada = input('Quer continuar?[S/N]')
    if parada in 'Nn':
        break
print(f'Foram registradas no total {cadas} pessoas')
print(f'A pessoa mais pesada pesa {maior}kg')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'A pessoa mais leve pesa {menor}kg')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}')