import pickle

# Biblioteca nativa do python para serializar objetos, podendo salvar eles em arquivos, ou usar em outras situações (sockets, ...)

# Salvar objetos
with open('objs.pkl', 'w') as f:  # Python 3: open(..., 'wb')
    pickle.dump([obj0, obj1, obj2], f)

# Carregar objetos do arquivo
with open('objs.pkl') as f:  # Python 3: open(..., 'rb')
    obj0, obj1, obj2 = pickle.load(f)