name = input('Qual seu nome?\n')

# r - leitura
# w - escrita
# a - append

# Alternativa 1
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

# Alternativa 2
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
