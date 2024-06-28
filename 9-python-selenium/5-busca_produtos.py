from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 0 - Termo de pesquisa
term = input('Digite o que deseja pesquisar:\n')

# 1 - Utilizando o WebDriver
browser = webdriver.Firefox()
browser.get('https://www.amazon.com.br')

# 2 - Acessando elementos de pesquisa
elem = browser.find_element(By.ID, 'twotabsearchtextbox')
elem.clear()
elem.send_keys(term)
elem.send_keys(Keys.ENTER)
time.sleep(2)

# 3 - Encontrando os elementos de todos os resultados
element = browser.find_element(By.CSS_SELECTOR,
                                'div.s-main-slot.s-result-list.s-search-results.sg-row'
                                )
print(element)
time.sleep(2)

# 4 - Encontrar informações dos produtos
items = element.find_elements(
    By.XPATH,
    '//div[@data-component-type="s-search-result"]'
)
print(len(items))

for item in items:
    title = item.find_element(By.TAG_NAME, 'h2').text
    price = ""
    link = item.find_element(
        By.CLASS_NAME, 'a-link-normal'
    ).get_attribute('href')
    img = ""

    try:
        price = item.find_element(
            By.CLASS_NAME,
            'a-price'
        ).text.replace('\n', '.')
    except:
        pass   
     
    try:
        img = item.find_element(
            By.CLASS_NAME,
            's-image'
        ).get_attribute('src')
    except:
        pass
    
    print(f"Título: {title}")
    print(f"Preço: {price}")
    print(f"Link: {link}")
    print(f"Imagem: {img}")
    

browser.quit()