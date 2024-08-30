v = True
while v == True:
    print('-='*20)
    base = int(input('Quantos asterísticos terá a base de seu triângulo retângulo? '))
    caracteres = '*'
    for i in range(1, base+1):
        print(caracteres * i)
    pergunta = input('Deseja continuar? [S/N]: ').strip().lower()[0]
    if pergunta == 's':
        v = True
    else:
        v = False
print('-=-=-=-= FIM DO PROGRAMA -=-=-=-=')