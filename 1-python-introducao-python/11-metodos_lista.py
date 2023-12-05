gameList = ['Resident Evil 4 Remake', 'Star Wars Jedi: Fallen Order',
            'The Legend of Zelda', 'Red Dead Redemption 2', 'Mario Odyssey']

# 1 - Tamanho da lista
print(len(gameList))

# 2 - Recuperar um item da lista pelo indice
print(gameList.index('Mario Odyssey'))

# 3 - Adicionar um item ao final da lista
gameList.append('GTA 5')
print(gameList)

# 4 - Ordenar a lista
gameList.sort()
print(gameList)

# 5 - Copiar os itens de uma lista para outra
gameReset = gameList.copy()
gameReset.remove('Star Wars Jedi: Fallen Order')
print(gameReset)

# 6 - Remove todos os itens de uma lista
gameList.clear()
print(gameList)
