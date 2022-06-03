maior = menor = 0
n = int(input('Digite um valor para a posição [0,0]:'))
n1 = int(input('Digite um valor para a posição [0,1]:'))
n2 = int(input('Digite um valor para a posição [0,2]:'))
n3 = int(input('Digite um valor para a posição [1,0]:'))
n4 = int(input('Digite um valor para a posição [1,1]:'))
n5 = int(input('Digite um valor para a posição [1,2]:'))
n6 = int(input('Digite um valor para a posição [2,0]:'))
n7 = int(input('Digite um valor para a posição [2,1]:'))
n8 = int(input('Digite um valor para a posição [2,2]:'))
print(f'''
[ {n} ]  [ {n1} ]  [ {n2} ]
[ {n3} ]  [ {n4} ]  [ {n5} ]
[ {n6} ]  [ {n7} ]  [ {n8} ]''')
pares = []
if n % 2 == 0:
    pares.append(n)
if n1 % 2 == 0:
    pares.append(n1)
if n2 % 2 == 0:
    pares.append(n2)
if n3 % 2 == 0:
    pares.append(n3)
if n4 % 2 == 0:
    pares.append(n4)
if n5 % 2 == 0:
    pares.append(n5)
if n6 % 2 == 0:
    pares.append(n6)
if n7 % 2 == 0:
    pares.append(n7)
if n8 % 2 == 0:
    pares.append(n8)
if n3 == 0:
    maior = n3
    menor = n3
else:
    if maior < n3:
        maior = n3
    if menor > n3:
        menor = n3
if n4 == 0 :
    maior = n4
    menor = n4
else:
    if maior < n4:
        maior = n4
    if menor > n4:
        menor = n4
if n5 == 0 :
    maior = n5
    menor = n5
else:
    if maior < n5:
        maior = n5
    if menor > n5:
        menor = n5
soma = sum(pares)
print(f'A soma dos Valores pares é igual a {soma} ')
print(f'A soma dos valores da 3 coluna é igual a {n2 + n5 + n8}')
print(f'O maior valor da 2 linha é {maior}')
