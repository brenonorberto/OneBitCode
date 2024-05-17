from openpyxl import load_workbook

# 1 - Lendo workbook e buscando planilha
wb = load_workbook(filename='files/teste.xlsx')
planilha1 = wb['Planilha1']

# 2 - Acessando um determinado valor
# print(planilha1['B2'].value)

# 3 - Iterando por meio de loop
for i in range(2, 5):

    ano = planilha1['A%s' % i].value
    lucro = planilha1['B%s' % i].value
    custos = planilha1['C%s' % i].value

    print('{0} teve {1} de lucro e {2} de custos'.format(ano, lucro, custos))