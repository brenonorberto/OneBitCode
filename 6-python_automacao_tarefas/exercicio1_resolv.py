import os

# 1 - Diretorio raiz
base_dir = os.path.expanduser('~')
print(base_dir)

# 2 - Navega no diretorio teste
path = os.path.join(base_dir, 'teste')
print(path)
work_dir = os.chdir(path)

# 3 - Lista arquivos do diretorio
file_list = os.listdir(work_dir)
print(file_list)

# 4 - Criar pastas
type_files = ['pdf', 'pptx', 'html', 'png', 'app', 'zip', 'dmg', 'jpg', 'ISO']
for type in type_files:
    if type not in os.listdir():
        os.mkdir(type)
        
# 5 - Organizando arquivos
for file in file_list:
    for type in type_files:
        if '.' + type in file:
            old_path = os.path.join(path, file)
            new_path = os.path.join(path, type, file)
            os.replace(old_path, new_path)