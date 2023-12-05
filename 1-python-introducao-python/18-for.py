gamesList = ['Fifa 23', 'God of War', 'The Legend of Zelda',
             'Red Dead Redemption 2', 'Mario Odyssey']

# 1 - Iterado valores de uma lista
for game in gamesList:
    print(game)

# 2 - Quando a condição for atendida, o loop será encenado
for game in gamesList:
    if game == 'Red Dead Redemption 2':
        break
    print(game)

# 3 - Quando a condição for atendida, o loop vai para a proxima iteração
for game in gamesList:
    if game == 'Red Dead Redemption 2':
        continue
    print(game)

# 4 - Avaliação do jogo
gameName = input('Qual o nome do jogo?\n? ')
gameRating = int(input('Digite quantas avaliações deseja fazer no jogo?\n '))

sum = 0
for i in range(gameRating):
    note = float(input(f'Digite a nota para o jogo\n '))
    sum += note  # sum = sum + note
print(f'A média de avaliações do jogo {gameName} é {sum/gameRating :.2f}')
