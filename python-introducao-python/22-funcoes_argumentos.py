# 1 - Crie uma função que receba dois argumentos: o primeiro nome e o segundo nome.
def full_name(fname, lname):
    print(f'{fname} {lname}')


full_name('João', 'Silva')

# 2 - Crie uma função que some dois números via parâmetros.


def sum_numbers(num1, num2):
    return num1 + num2


print(sum_numbers(10, 20))

# 3 - Argumentos default numa função


def address(country='Brasil'):
    print(f'Eu moro no {country}')


address()
address('Canadá')

# 4 - Avaliação do jogo


def rating_game(qtdRating):
    game_name = input('Digite o nome do jogo\n ')
    sum = 0
    for i in range(qtdRating):
        note = float(input(f'Digite a nota para o jogo\n '))
        sum += note
    print(f'A média de avaliações do jogo {game_name} é {sum/qtdRating :.2f}')


rating = int(input('Digite quantas avaliações deseja fazer no jogo?\n '))
rating_game(rating)
