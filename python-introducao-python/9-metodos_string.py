gameName = 'Fifa23'
gameDescription = '''
Fifa 23 é um jogo de futebol, desenvolvido pela Electronic Arts,
e que possibilita jogar localmente ou online.
'''

print(gameName.upper())  # Retorna uma string com todas as letras maiúsculas
print(gameName.lower())  # Retorna uma string com todas as letras minúsculas
print(gameName.title())  # Apenas a primeira letra em maiúscula
print(gameName.capitalize())  # Apenas a primeira letra em maiúscula
print(gameName.center(10, '-'))
# Retorna a string centralizada com caracteres de prenchimento
print(gameName.find('a'))  # Retorna a posição de um determinado caractere
print(gameDescription.count('a'))
# Conta quantas vezes um determinado caractere aparece
print(gameDescription.replace('Fifa', 'Pes'))
# Substitui um determinado caractere por outro
print(gameDescription.split(','))
