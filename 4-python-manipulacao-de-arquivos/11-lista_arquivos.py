import glob
import os
import zipfile

# 1 - Diretório de trabalho atual
print(os.getcwd())

# 2 - Lista todos os arquivos .txt
for file in glob.glob("dados/*.txt"):
    print(file)

# 3 - Lista todos os arquivos .csv
for file in glob.glob("dados/*.csv"):
    print(file)

# 4 - Compactando arquivos .txt
with zipfile.ZipFile('names.zip', 'w') as zip:
    for file in glob.glob('dados/*.txt'):
        zip.write(file)

# 5 - Compactando arquivos .csv
with zipfile.ZipFile('languagens.zip', 'w') as zip:
    for file in glob.glob('dados/*.csv'):
        zip.write(file)

# 6 - Compactando todos os arquivos
with zipfile.ZipFile('code.zip', 'w') as zip:
    for file in glob.glob('*'):
        zip.write(file)
