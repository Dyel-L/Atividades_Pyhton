expr = str(input('Digite Sua expressão:  '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) > 0:
    print('Sua expressão está valida!')
else:
    pilha'Sua expressao esta invalida'