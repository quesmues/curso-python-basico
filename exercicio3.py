while True:
    quantidade = input('Insira a quantidade de pessoas a ser convidada: ')
    lista_convidados = []
    for i in range(int(quantidade)):
        convidado = input('Insira o convidado de número '+str(i+1)+':')
        lista_convidados.append(convidado)
    print('\n' + 'Lista de convidados:')
    for l in lista_convidados:
        print(l)
    break
