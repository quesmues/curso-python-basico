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
i += 1


# Listas, dicionários, tuplas
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
teste(com, ou, sem, argumento)


# Argumentos de linha de comando
import sys
# Mostra os argumentos passados ao executar o arquivo python
sys.argv















