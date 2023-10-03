import pprint

gamesDict = {
    'Resident Evil 4 Remake': {
        'yarLaunch': 2023,
        'classification': 9.8,
        'genre': ['Aventura', 'Ação']
    },
    'Star Wars Jedi: Fallen Order': {
        'yearLaunch': 2022,
        'classification': 8.8,
        'genre': ['Aventura', 'si-fi']
    },
    'The Legend of Zelda': {
        'yearLaunch': 1986,
        'classification': 9.2,
        'genre': ['Aventura', 'Plataforma']
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

# 1 - Buscar informação dentro de um dicionário aninhado
print(gamesDict['Resident Evil 4 Remake']['genre'])

# 2 - Adicionar novo item ao dicionário
gamesDict['The Legend of Zelda']['players'] = 2
print(gamesDict['The Legend of Zelda'])

# 3 - Remover item do dicionário
del gamesDict['Resident Evil 4 Remake']
pprint.pprint(gamesDict)
