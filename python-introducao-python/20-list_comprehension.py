# 1 - Liste valores de 0 a 10 que sejam menor do que 4.
# for i in range(10):
#     if i < 4:
#         print(i)
listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

# 2 - jogos que possuam a letra a
gamesList = ['Mario Odyssey', 'DK Country', 'Luigis Mansion', 'Kirby']

newList = [x for x in gamesList if 'a' in x]
print(newList)

# 3 - Jogos que eu zerei
gamesFinished = [x for x in gamesList if x != 'Kirby']
print(gamesFinished)
