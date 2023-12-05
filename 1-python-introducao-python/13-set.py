gameSet = {'Resident Evil 4 Remake', 'Star Wars Jedi: Fallen Order',
           'The Legend of Zelda', 'Red Dead Redemption 2', 'Mario Odyssey'}

print(gameSet)

# 1 - Buscar o tamanho do set
print(len(gameSet))

# 2 - True e 1 são considerados o mesmo valor
exampleSet = {'Fifa 23', True, 1, 59.99, }
print(exampleSet)

# 3 - Adicionar um item de outro set
gameSet.update(exampleSet)
print(gameSet)

# 4 - Remover um item no set
gameSet.remove(True)
gameSet.remove(59.99)
print(gameSet)
# - Não possibilita recuperar valores via fatiamento ou slice
