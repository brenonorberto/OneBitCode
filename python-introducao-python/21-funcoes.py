# 1 - Função para imprimir hello world
def welcome():
    print('Hello World!')


welcome()

# 2 - Função para somar dois números


def sum():
    return 5 + 4


print(sum())

# 3 - Função para cadastrar um jogo


def create_game():
    name = input('Qual o nome do jogo\n? ')
    yearLaunch = int(input('Qual o ano de lançamento\n? '))
    gamePrice = float(input('Qual o preço do jogo\n? '))
    noteRating = float(input('Digite a nota de avaliação\n? '))

    print(f'{name} - R$ {gamePrice}')


create_game()
