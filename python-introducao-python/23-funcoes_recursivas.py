'''
Fatorial de um número
1 -> 1
3 -> 3 * 2 * 1
5 -> 5 * 4 * 3 * 2 * 1

'''

# 1 - Fatorial de um número


def fatorial(num):
    if num == 1:
        return 1
    else:
        return num * fatorial(num - 1)


number = int(input('Digite um número para o fatorial\n'))
print(f'O fatorial de {number} é {fatorial(number)}')

# 2 - Soma total de um número
'''
1 -> 1 + 0
3 -> 3 + 2 + 1
5 -> 5 + 4 + 3 + 2 + 1

'''


def total_sum(num):
    if num == 1:
        return 1
    else:
        return num + total_sum(num - 1)


num = int(input('Digite um número para soma\n'))
print(f'A soma total de {num} é {total_sum(num)}')
