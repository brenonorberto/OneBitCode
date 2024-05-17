from openpyxl import Workbook

# 1 - Criando o workbook
wb = Workbook()
name = 'files/teste.xlsx'

# 2 - Utilizando o worksheet
ws1 = wb.active
ws1.title = 'Planilha1'

# 3 - Adicionando dados na planilha
data = [
    ['Ano', 'Lucro', 'Custos'],
    [2010, '25%', '10%'],
    [2011, '30%', '15%'],
    [2012, '35%', '20%']
]

for line in data:
    ws1.append(line)
    
ws2 = wb.create_sheet(title='Pi')
ws2['D1'] = 3.14
    
wb.save(filename=name)