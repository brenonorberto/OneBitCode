# Cálculo do valor a ser pago pela passagem, conforme a distância
distancia = float(input('Qual a distância deseja percorrer?\n'))

if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.35
print(f'O valor a ser pago é de R$ {valor:.2f}\n')

# Calculo do aumento salário funcionário
salario = float(input('Qual o salário do funcionário?\n'))

if salario <= 1250:
    novoSalario = salario + (salario * 0.15)
else:
    novoSalario = salario + (salario * 0.10)

print(f'O novo salário do funcionário é de R$ {novoSalario:.2f}')
