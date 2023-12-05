'''
*args - Utilizamos ele quando não temos certeza de quantos argumentos 
queremos ter em uma função
- Os argumentos são passados em uma tupla

**kwargs: Além dos valores, podemos passar também as respectivas
chaves para cada argumento.
- Os argumentos são passados como um dicionário.

'''

# 1 - Soma de números


def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f'A soma é: {sum_total}')


sum(7)
sum(7, 9)
sum(7, 9, 5)


print('')


def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")


print("###### Curso ######\n")
presentation(name="Python", category="Backend", level="Iniciante")
