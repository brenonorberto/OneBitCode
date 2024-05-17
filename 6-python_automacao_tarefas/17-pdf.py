import PyPDF2 as pdf
from PyPDF2 import PdfReader

# 1 - Versão e método dessa biblioteca
print(pdf.__version__)
print(dir(pdf))

# 2 - Importando PDF
file = open('files/teste.pdf', 'rb') 
reader = PdfReader(file)
print(reader)
# print(reader.metadata)
info = reader.metadata

# 3 - Extraindo algumas informações
print(info.title)
print(info.author)
print(info.subject)
print(info.creator)
print(info.producer)
print(info.creation_date)
print(info.modification_date)
print(len(reader.pages))
print(reader.pages[0].extract_text())