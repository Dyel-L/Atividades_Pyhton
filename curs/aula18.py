lista = []
pessoas = []
lista.append('mario')
lista.append(23)
pessoas.append(lista[:])#Copia de 1 lista
galera = [['joao', 15], ['maria', 25], ['pedrin', 32]]
print(pessoas[0][0])#Escolhendo na lista dentro de uma lista
print(galera[2][0])#exemplo
for i in galera:#Essa parada do 'i' Se liga ao in de galera
    print(f'{i[0]} Tem {i[1]} anos de idade')#assim o [0] é o primeiro a ser printado que é o nome que ta na lista
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade ')
    else:
        print(f'{p[0]} é menor de idade')