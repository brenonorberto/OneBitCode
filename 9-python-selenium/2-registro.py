from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1 - acessando o site
browser = webdriver.Firefox()
browser.get('http://registro.br')

# 2 - Buscando elementos
elem = browser.find_element(By.ID, 'is-avail-field')
elem.clear()
elem.send_keys('brenonorberto')
elem.send_keys(Keys.ENTER)
time.sleep(5)
browser.save_screenshot('dominio.png')

# 3 - Buscando informações
results = browser.find_elements(By.TAG_NAME, 'strong')
# import pdb # debugger com python
# pdb.set_trace()
print(f'Domínio {results[1].text} está {"Disponível" if results[2].text == "disponível" else "indisponível"}{" e o valor por um ano é " + results[3].text + " reais" if results[2].text == "disponível" else ""}')

# browser.quit()