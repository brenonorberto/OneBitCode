name = input('Qual o nome do jogo\n? ')
yearLaunch = int(input('Qual o ano de lançamento\n? '))
gamePrice = float(input('Qual o preço do jogo\n? '))
planIncluded = input('O jogo inclui plano de assinatura\n? ')

print('')
print('### Dados do jogo ###')
print('=====================')
print('')

# Alternativa 1
# print('Nome do jogo:', name)
# print('Ano do jogo:', yearLaunch)
# print('Preço do jogo:', gamePrice)
# print('Está incluído no jogo:', planIncluded)

# Alternativa 2
# print('Nome do jogo:', name, '\nAno do jogo:', yearLaunch,
#       '\nPreço do jogo:', gamePrice, '\nEstá incluído no jogo:', planIncluded)


# Alternativa 3 (Mais usada)
print(f'Nome do jogo: {name} \nAno do jogo: {yearLaunch} \nPreço do jogo: {gamePrice} \nEstá incluído no jogo: {planIncluded}')
