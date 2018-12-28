# A função type() indica o tipo da variável
name = 'teste'
print(type(name))


# Forma mais fácil de usar o print, sem ter de usar o str()
print(name, name, name, type(name))


# A função input(), pede uma entrada para o user na console
name = input('Qual o seu nome')


# Strings também são listas, e podemos repartir ela, também pulando vários caracteres
# Pula 2 em 2 caracteres steps
name = 'Hello World'
print(name[0:5:2])
# Números negativos contam de trás pra frente, o último é -1
print(name[-2])
# Inverter a frase
print(name[::-1])


# Listas
name = ['hello', 'world']
# Adicionar e remover
name.append('teste')
name.remove('teste')
# Limpar lista
name.clear()
# Inserir em determinada posição
name.insert(1, 'teste')
# Ou
name[0] = 'dia'
# Contagem de elementos, todos ou algum em específico
name.count('teste')
# Remover o ultimo adicionado, e imprime o removido
name.pop()


# Passar string para maiusculo ou minusculo
name = 'teste'
name.lower()
name.upper()


# Range pulando 2 ou mais números
range(0, 100, 2)
# Outros usos
range(len(name))


# Interações
i = 0
i += 1


# Listas, dicionários, tuplas
nome = 'nome'
outros = 'outros'
lista_de_nomes = ['nome', '...'] # Mutável                                      (List)
dicionario_de_nomes = {'nome':nome, '...':outros} # Não é ordenado              (Dict)
tupla_de_nomes = ('nome', '...') # Não mutável (não remove ou adiciona objetos) (Tuple)
conjunto_de_nomes = {'nome', '...'} # Não é ordenado, não possui índice         (Set)
# Verificar se existe algo nos valores do dicionário:
dicionario_de_nomes.values()
# Verificar se existe alguma key:
dicionario_de_nomes.keys()
# Adicionar elementos no conjunto, não salva dados duplicados
conjunto_de_nomes.add('teste')
# Um conjunto, e um dicionário, são mais rápidos para procurar elementos
# Definindo
lista = []
tupla = ()
dicionario = {} # dict()
conjunto = set()


# Funções
def teste(com, ou, sem, argumento):
    print('essa é uma função')


com = ou = sem = argumento = 'teste'
teste(com, ou, sem, argumento)


# Argumentos de linha de comando
import sys
# Mostra os argumentos passados ao executar o arquivo python
sys.argv


# Exemplo de Objeto em Orientação a Objetos
class Nome():
    # Construtor
    def __init__(self, primeiro, ultimo):
        self.primeiro = primeiro
        self.ultimo = ultimo
    # Métodos
    # def metodo(self, ...):
    #   ...

# Chamada do Objeto
nome = Nome # Chamada de classe não precisa (), já função/método precisa de ()
nome.primeiro = 'teste'
nome.ultimo = 'teste'
print(nome)

# Exemplo OOO com hereditariedade
# Classe pai
class Veiculo:
    def __init__(self, cor, rodas, marca, tanque):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque
    def abastecer(self, litros):
        self.tanque += litros

#Classe filha, com sobreposição de método
class Carro(Veiculo):
    def __init__(self, cor, marca, tanque, placa):
        Veiculo.__init__(self, cor, 4, marca, tanque)
        self.placa = placa
    def abastecer(self, litros):
        self.tanque +=litros

temp = Carro('azul', 'fiat', 50, 'III0000')
print(temp.cor, temp.marca, temp.placa, temp.rodas, temp.tanque)
temp.abastecer(100)
print(temp.tanque)


# Trabalhando com arquivos
arquivo = open('arquivo.txt', 'a') # b para arquivos binários, w r+ + a para texto
arquivo.write('teste\n')
arquivo = open('arquivo.txt', 'r')
type(print(arquivo))
for linha in arquivo:
    print(linha)


# Tratamento de exceções
try:
    a = 1200 / 0
except ZeroDivisionError:           # Erro em expecifico, pode capturar o erro com 'as var'
    print(e)
except Exception as e:              # Todos os erros, podemos capturar o erro para printar
    print(e)
except:                             # Todos os erros
    print('error')




















