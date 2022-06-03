from random import randint
joao = randint(0, 1)
maria = randint(0, 1)
pedrinho =randint(0, 1)

if (joao == maria == pedrinho):
    print("empatou")
else:
    if (joao == maria):
        print("Pedrinho ganhou")
    else:
        if (joao == pedrinho):
            print("Maria ganhou")
        else:
            print("joao ganhou")