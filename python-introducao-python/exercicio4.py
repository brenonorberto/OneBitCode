# Lançamento do foguete

x = 10
while x >= 0:
    print(x)
    x -= 1

# Tabuada de um número
number = int(input('Tabuada de: \n'))
begin = int(input('De: \n'))
end = int(input('Ate: \n'))

x = begin
while x <= end:
    print(f'Tabuada de {number} x {x} = {number * x}')
    x += 1
