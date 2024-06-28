from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1 - Utilizando o WebDriver

browser = webdriver.Firefox()
browser.get('http://registro.br')

# 2 - Lista de domínios

dominios = [
    'brenorberto.com.br',
    'breno.com.br',
    'breno.norberto.com.br',
    'brenonc.com.br',
]

file = open('domains.txt', 'w', encoding='utf-8')

# 3 - Manipulando elementos

for dominio in dominios:
    elem = browser.find_element(By.ID, 'is-avail-field')
    elem.clear()
    elem.send_keys(dominio)
    elem.send_keys(Keys.ENTER)
    time.sleep(5)

# 4 - Buscando informações
    results = browser.find_elements(By.TAG_NAME, 'strong')
    text = f'Domínio {results[1].text} está {"Disponível" if results[2].text == "disponível" else "indisponível"}{" e o valor por um ano é " + results[3].text + " reais" if results[2].text == "disponível" else ""}\n'
    print(text)
    file.write(text)
    
file.close()
browser.close()
    