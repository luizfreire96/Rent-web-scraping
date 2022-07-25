from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv

driver = webdriver.Chrome('/home/luiz/Documents/awari/WebScrapping/chromedriver')
driver.implicitly_wait(10)
driver.get('https://www.vivareal.com.br/aluguel/ceara/fortaleza/')
sleep(10) #tempinho pra clicar pra fechar uma abinha que aparece
resultados = []
k = 0
while len(resultados) <=7500:
    k = k+1
    sleep(2)
    driver.get('https://www.vivareal.com.br/aluguel/ceara/fortaleza/?pagina={}'.format(k))
    descricoes = driver.find_elements(By.CLASS_NAME, 'property-card__content')

    for i in range(0, len(descricoes)):
        descricoes = driver.find_elements(By.CLASS_NAME, 'property-card__content')
        descricoes[i].click()
        sleep(1)
        p = driver.current_window_handle
        chwd = driver.window_handles
        for w in chwd:
            if(w!=p):
                driver.switch_to.window(w)
                detalhes = []
                tamanho = driver.find_element(By.XPATH, "//*[@id='js-site-main']/div[2]/div[1]/div[2]/ul/li[1]").text
                quartos = driver.find_element(By.XPATH, "//*[@id='js-site-main']/div[2]/div[1]/div[2]/ul/li[2]").text
                banheiros = driver.find_element(By.XPATH, "//*[@id='js-site-main']/div[2]/div[1]/div[2]/ul/li[3]").text
                vagas = driver.find_element(By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/div[2]/ul/li[4]').text
                endereco = driver.find_element(By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/div[1]/section/div/div/p').text
                aluguel = driver.find_element(By.XPATH, '//*[@id="js-site-main"]/div[2]/div[2]/div[1]/div/div[1]/div/h3').text
                detalhes.append([tamanho, quartos, banheiros, vagas, endereco, aluguel])
                resultados.append(detalhes)
                sleep(2)
                driver.close()
                sleep(2)
                driver.switch_to.window(p)
                with open("out.csv", "a") as f:
                   writer = csv.writer(f)
                   writer.writerow(detalhes)


print(len(resultados))