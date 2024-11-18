while True:
    print('-='*40)
    print('Qual caractere deseja que seu triângulo-retângulo seja feito?')
    caractere = str(input('Resposta: ')).strip()[0]
    print('Qual o número de caracteres deseja na base?')
    base = int(input('Resposta: '))

    for c in range(1, base+1):
        print(caractere * c)

    print('Deseja recomeçar? (S/N)')
    reiniciar = str(input('Resposta: ')).strip().lower()[0]

    if reiniciar == 'n':
        print('\033[31mFIM DO PROGRAMA\033[m')
        print('-='*40)
        break