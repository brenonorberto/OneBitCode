from openpyxl import Workbook
from openpyxl.chart import AreaChart, Reference, Series

wb = Workbook()
ws = wb.active

data = [
    ['Ano', 'Lucro', 'Custos'],
    [2010, '25%', '10%'],
    [2011, '30%', '15%'],
    [2012, '35%', '20%'],
    [2013, '10%', '10%'],
    [2014, '45%', '30%'],
    [2015, '50%', '35%']
]

for d in data:
    ws.append(d)
    
    # Criação do grafico
    chart = AreaChart()
    chart.title = 'Lucro x Custos por ano'
    chart.style = 12
    chart.x_axis.title = 'Ano'
    chart.y_axis.title = 'Porcentagem'
    
    # Criação das referências
    categorias = Reference(ws, min_col=1, min_row=1, max_row=7)
    dados = Reference(ws, min_col=2, min_row=1, max_col=3, max_row=7)
    
    # Adicionando os dados ao grafico
    chart.add_data(dados, titles_from_data=True)
    chart.set_categories(categorias)
    ws.add_chart(chart, 'A10')
    
    
wb.save('files/chart.xlsx')