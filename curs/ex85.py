numeros = [[], []]
for i in range(1, 8):
    n = (int(input(f'Digite o {i} Numero : ')))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares foram {numeros[0]}')
print(f'Os valores impares foram {numeros[1]}')
