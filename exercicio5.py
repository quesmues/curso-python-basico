'''
Exercício: Crie um software de gerenciamento bancário
Esse software poderá ser capaz de criar clientes e contas
Cada cliente possui nome, cpf, idade
Cada conta um cliente, saldo, limite, sacar, depositar, e consultar saldo
'''

class Cliente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

class Conta:
    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
    def sacar(self, quantidade):
        if quantidade < self.limite + self.saldo:
            self.saldo = self.saldo - quantidade
        else:
            print('Você não possui saldo ou limite para esta operação!')
    def depositar(self, quantidade):
        if
        self.saldo = self.saldo + quantidade
    def consultarSaldo(self):
        print('Seu saldo: ', self.saldo)

cliente = Cliente('Eduardo', '012.345.678-00', 24)
conta = Conta(cliente, 1000, 5000)

print(conta.cliente.nome)