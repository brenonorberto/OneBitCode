import hashlib

# 1 - Verificar os algoritimos de hash
print(hashlib.algorithms_available)

# 2 - Acessar o algoritimo de acordo com o SO
print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o algoritimo SHA256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = 'A melhor forma de prever o futuro é criá-lo'.encode()
algorithm.update(message)
print(algorithm.hexdigest())

# 4 - Utilizando o MD5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())
