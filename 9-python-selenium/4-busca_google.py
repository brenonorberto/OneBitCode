from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1 - Termo de pesquisa
term = input('Digite o que deseja pesquisar:\n')

# 2 - Iniciando o WebDriver
browser = webdriver.Firefox()
browser.get('https://google.com.br')

# 3 - Encontrando elementos na página
elem = browser.find_element(By.XPATH, "//textarea[@aria-label='Pesquisar']")

# 4 - Enviando o termo de pesquisa
elem.send_keys(term)
elem.send_keys(Keys.ENTER)

# 5 - Retornando a qtd de registros encontrados
time.sleep(2)
results = browser.find_element(By.ID, 'result-stats').text

# Aguarde até que a página de resultados seja carregada
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.ID, "search")))

# Clique no botão de ferramentas (se necessário)
tools_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button'][contains(text(),'Ferramentas')]")))
tools_button.click()

# Aguarde até que o elemento com a quantidade de resultados esteja visível
results = wait.until(EC.presence_of_element_located((By.ID, "result-stats")))

print(f'Foram encontrados {results.text}')

# 6 - Retornando o Número de Páginas
qtd_results = int(results.text.split('Aproximadamente ')[1].split(' resultados')[0].replace('.',''))
tot_pages = qtd_results / 10
print(f'Número de páginas {tot_pages}')

# 7 - Navegando entre páginas
# url_page = browser.find_element(
#     By.XPATH,
#     '//a[@aria-label="Page 2"]').get_attribute('href')

# current_page = 0
# start = 10
# list_results = []

# while current_page <= 10:
#     if not current_page == 0:
#         url_page = url_page.replace(
#             "start=%s" %start,
#             "start=%s" %(start + 10),
#         )
#         start += 10
#     current_page += 1
#     browser.get(url_page)


    
# 8 - Recuperando informações
list_results = []
divs = browser.find_elements(
    By.XPATH,
    '//div[@class="yuRUbf"]'
)
for div in divs:
    name = div.find_element(By.TAG_NAME, 'h3')
    link = div.find_element(By.TAG_NAME, 'a')
    result = "%s,%s" %(name.text, link.get_attribute('href'))
    print(result)
    list_results.append(result)
    
# 9 - Salvando em arquivo txt
with open('results_term.txt', 'w', encoding='utf-8') as file:
    for result in list_results:
        file.write("%s\n" %result)

print(f'Foram encontrados {len(list_results)} resultados na pesquisa')

browser.close()

