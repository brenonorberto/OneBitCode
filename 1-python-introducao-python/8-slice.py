gameName = 'Fifa 23'
gameDescription = '''
Fifa 23 é um jogo de futebol desenvolvido pela Electronic Arts
e que possibilita jogar localmente ou online.
'''
# string[início:fim] - inicia na posição 0 | indice final -1

# 1 - Busque toda string a partir da primeira posição
print(gameName[0:])

# 2 - Busque toda string a partir da última posição
print(gameName[:7])

# 3 - Busque toda string da terceira posição até a última
print(gameName[2:])

'''
string[início:fim:passo] - inicia na posição 0 | indice final -1
passo - determina o incremento de posição. Por padrão passo é 1
'''

# 4 - Busque toda string de 2 em 2 caracteres
print(gameName[::2])

# 5 - Busque toda string nos índices ímpares
print(gameName[1::2])

# 6 - Inverte uma string de trás para frente
print(gameName[::-1])
