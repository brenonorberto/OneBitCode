num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

# Aritméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2
print(f'A soma é {sum} \na subtração é {sub} \na divisão é {div} \na multiplicação é {mult} \no módulo é {mod} \na exponenciação é {exp}')

# Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
diferent = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2
print(f'Os números {num1} e {num2} são iguais? {equal}')
print(f'O número {num1} é maior ou igual a {num2}? {bigger_equal}')

# Atribuição
num1 += 1
num1 -= 1
num1 *= 1
num1 /= 1
num1 **= 1
