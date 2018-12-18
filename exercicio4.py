def maiorNumero(colecao):
    colecao = max(colecao)
    print('O maior número é: ',colecao)


def menorNumero(colecao):
    colecao = min(colecao)
    print('O menor número é: ',colecao)


colecao = []
for i in range(5):
    colecao.append(int(input('Informe um numero: ')))
maiorNumero(colecao)
menorNumero(colecao)