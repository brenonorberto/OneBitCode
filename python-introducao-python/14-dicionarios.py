gameFifa = {
    'name': 'Fifa 23',
    'yearLaunch': 2022,
    'gamePrice': 59.99,
    'classification': 8.5,
    'genre': ['Esportes', 'família']
}
print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# 1 - Recuperar um item do dicionário
print(gameFifa['genre'])
print(gameFifa.get('classification'))

# 2 - Buscar apenas as chaves do dicionário
print(gameFifa.keys())

# 3 - Buscar apenas os valores do dicionário
print(gameFifa.values())

# 4 - Buscar itens do dicionário com chaves e valores
print(gameFifa.items())

# 5 - Adicionar itens ao dicionário
gameFifa['players'] = 2
print(gameFifa)

# 6 - Atualizar itens no dicionário
gameFifa['players'] = 1
print(gameFifa)

# 7 - Remover itens do dicionário
gameFifa.pop('players')
print(gameFifa)
