from lib import *

while True:
    print('\n\t\t\t -- Sistema Matemático -- \n\n')

    print('1. Fatorial')
    print('2. Tabuada')
    print('3. Sair')


    op = int(input('Informe a opção desejada: '))

    if op == 1:
        print('\n\t\t\t -- Calcula Fatorial \n\n')


        num = int(input('Informe um número: '))


        fat = gera_fatorial(num)

        print(f'{num}! = {fat}')
    elif op == 2:
        print('\n\t\t\t -- Tabuada -- ')


        num = int(input('Informe o número: '))


        gerar_tabuada(num)

    elif op == 3:

        print('\nAbraço!\n')
        break
    else:

        print(f'\nOpção {op} incorreta!\n')