from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random

# Definindo o local do driver do Chrome


time.sleep(2)
for i in range(10):
    PATH = r"C:/Program Files/Google/Chrome/Application/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    # Acessando o link
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfv-UDdxCPuvaABPUoL4ej9jJdpCHmvPYHihvdxhga8Px1liQ/viewform")


    # Questão 0
    mapQuest0 = ['i5', 'i8']
    posQuest0 = [0, 1]
    pesosQuest0 = [4, 1]
    aleatorioQuest0 = random.choices(mapQuest0, pesosQuest0, k=1)[0]
    driver.find_element(By.ID, aleatorioQuest0).click()
    time.sleep(1)
    
    if aleatorioQuest0 == 'i5':
        # Botão Próxima
        botao_proxima_pagina_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
        botao_proxima_pagina = driver.find_element(By.XPATH,botao_proxima_pagina_xpath)
        botao_proxima_pagina.click()
        time.sleep(1)

        # Questão 1
        mapQuest1 = ['i6', 'i9', 'i12', 'i15', 'i18', 'i21', 'i24']
        pesosQuest1 = [6.3, 58.3, 2.1, 10.4, 33.3, 18.8, 58.4]
        aleatorioQuest1 = random.choices(mapQuest1, pesosQuest1, k=3)
        r = [0, 1, 2]
        for i in r:
            btn_novosClientes = aleatorioQuest1[i]
            print(btn_novosClientes)
            driver.find_element(By.ID, btn_novosClientes).click()
            aleatorioQuest1.remove(btn_novosClientes)
            r.remove(r[-1])
            time.sleep(1)
            
        # Questão 2
        mapQuest2 = ['i34', 'i37', 'i40']
        posicaoQuest2 = [0, 1, 2]
        pesosQuest2 = [27.1, 41.7, 31.3]
        aleatorioQuest2 = random.choices(posicaoQuest2, pesosQuest2, k=1)[0]
        driver.find_element(By.ID, mapQuest2[aleatorioQuest2]).click()
        time.sleep(1)

        # Questão 3
        q1 = random.choices([1, 2, 3], [45.75, 37.123, 17.123], k=1)[0]
        q1 = random.choices([4, 5, 6, 7, 8], [11.17, 11.17, 44.149, 22.34, 11.17], k=1)[0]
        respQuest3 = '3' if mapQuest2[aleatorioQuest2] == 'i34' else '6' if mapQuest2[aleatorioQuest2] == 'i37' else '9'
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(respQuest3)
        time.sleep(1)


        # Questão 4 //*[@id="i51"]/div[3] - //*[@id="i54"]/div[3]/div
        mapQuest4 = ['i51', 'i54']
        posicaoQuest4 = [0, 1]
        pesosQuest4 = [9.9, 2.6]
        aleatorioQuest4 = random.choices(posicaoQuest4, pesosQuest4, k=1)[0]
        driver.find_element(By.ID, mapQuest4[aleatorioQuest4]).click()
        time.sleep(1)


        # Questão 5, 6, 7 --- NÃO
        if mapQuest4[aleatorioQuest4] == 'i54': 
            listNao = ['i64', 'i74', 'i84']
            for i in listNao:
                driver.find_element(By.ID, i).click()
                time.sleep(1)
                
        # Questão 5, 6, 7 --- SIM
        else:  
            cenarios = [
                ['i61', 'i74', 'i84'], #Sim, Sim, Não, Não
                ['i61', 'i71', 'i84'], #Sim, Sim, Sim, Não
                ['i61', 'i71', 'i81'], #Sim, Sim, Sim, Não
            ]
            for i in cenarios:
                for j in i:
                    driver.find_element(By.ID, j).click()
                    time.sleep(1)

        # Questão 8
        mapQuest8 = ['i91', 'i94']
        posicaoQuest8 = [0, 1]
        pesosQuest8 = [58.3, 41.7]
        aleatorioQuest8 = random.choices(posicaoQuest8, pesosQuest8, k=1)[0]
        driver.find_element(By.ID, mapQuest8[aleatorioQuest8]).click()
        time.sleep(1)

        # Questão 9
        mapQuest9 = ['i101', 'i104']
        posicaoQuest9 = [0, 1]
        pesosQuest9 = [81.7, 18.8]
        aleatorioQuest9 = random.choices(posicaoQuest9, pesosQuest9, k=1)[0]
        driver.find_element(By.ID, mapQuest9[aleatorioQuest9]).click()
        time.sleep(1)

        # Questão 10
        mapQuest10 = ['i111', 'i114']
        posicaoQuest10 = [0, 1]
        pesosQuest10 = [43.8, 56.3]
        aleatorioQuest10 = random.choices(posicaoQuest10, pesosQuest10, k=1)[0]
        driver.find_element(By.ID, mapQuest10[aleatorioQuest10]).click()
        time.sleep(1)

        # Botão Próxima
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span').click()
        time.sleep(2)

        # Questão 11
        mapQuest11 = ['i5', 'i8', 'i11']
        posicaoQuest11 = [0, 1, 2]
        pesosQuest11 = [5, 4, 1]
        aleatorioQuest11 = random.choices(posicaoQuest11, pesosQuest11, k=1)[0]
        driver.find_element(By.ID, mapQuest11[aleatorioQuest11]).click()
        time.sleep(1)

        # Questão 12
        mapQuest12 = ['i18', 'i21', 'i24']
        posicaoQuest12 = [0, 1, 2]
        pesosQuest12 = [22.9, 41.7, 35.4]
        aleatorioQuest12 = random.choices(posicaoQuest12, pesosQuest12, k=1)[0]
        driver.find_element(By.ID, mapQuest12[aleatorioQuest12]).click()
        time.sleep(1)

        # Questão 13
        mapQuest13 = ['i31', 'i34'] 
        posicaoQuest13 = [0, 1]
        pesosQuest13 = [91.7, 8.3]
        aleatorioQuest13 = random.choices(posicaoQuest13, pesosQuest13, k=1)[0]
        driver.find_element(By.ID, mapQuest13[aleatorioQuest13]).click()
        time.sleep(1)

        # Questão 14
        mapQuest14 = ['i41', 'i44'] 
        posicaoQuest14 = [0, 1]
        pesosQuest14 = [22.4, 77.6]
        aleatorioQuest14 = random.choices(posicaoQuest14, pesosQuest14, k=1)[0]
        driver.find_element(By.ID, mapQuest14[aleatorioQuest14]).click()
        time.sleep(1)

        # Questão 15
        mapQuest15 = ['i51', 'i54'] 
        posicaoQuest15 = [0, 1]
        pesosQuest15 = [69.4, 30.6]
        aleatorioQuest15 = random.choices(posicaoQuest15, pesosQuest15, k=1)[0]
        driver.find_element(By.ID, mapQuest15[aleatorioQuest15]).click()
        time.sleep(1)

        # Questão 16
        mapQuest16 = ['i61', 'i64'] 
        posicaoQuest16 = [0, 1]
        pesosQuest16 = [32.7, 67.3]
        aleatorioQuest16 = random.choices(posicaoQuest16, pesosQuest16, k=1)[0]
        driver.find_element(By.ID, mapQuest16[aleatorioQuest16]).click()
        time.sleep(1)

        # Questão 17
        mapQuest17 = ['i71', 'i74'] 
        posicaoQuest17 = [0, 1]
        pesosQuest17 = [22.4, 77.6]
        aleatorioQuest17 = random.choices(posicaoQuest17, pesosQuest17, k=1)[0]
        driver.find_element(By.ID, mapQuest17[aleatorioQuest17]).click()
        time.sleep(1)

        # Botão Próxima
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span').click()
        time.sleep(2)

        # Questão 18
        mapQuest18 = ['i5', 'i8'] 
        posicaoQuest18 = [0, 1]
        pesosQuest18 = [81.6, 18.4]
        aleatorioQuest18 = random.choices(posicaoQuest18, pesosQuest18, k=1)[0]
        driver.find_element(By.ID, mapQuest18[aleatorioQuest18]).click()
        time.sleep(1)

        # Questão 19
        mapQuest19 = ['i15', 'i18'] 
        posicaoQuest19 = [0, 1]
        pesosQuest19 = [83.7, 16.3]
        aleatorioQuest19 = random.choices(posicaoQuest19, pesosQuest19, k=1)[0]
        driver.find_element(By.ID, mapQuest19[aleatorioQuest19]).click()
        time.sleep(1)

        # Questão 20
        mapQuest20 = ['i25', 'i28'] 
        posicaoQuest20 = [0, 1]
        pesosQuest20 = [30.6, 69.4]
        aleatorioQuest20 = random.choices(posicaoQuest20, pesosQuest20, k=1)[0]
        driver.find_element(By.ID, mapQuest20[aleatorioQuest20]).click()
        time.sleep(1)

        # Questão 21
        mapQuest21 = ['i35', 'i38', 'i41'] 
        posicaoQuest21 = [0, 1, 2]
        pesosQuest21 = [38.3, 51.1, 10.6]
        aleatorioQuest21 = random.choices(posicaoQuest21, pesosQuest21, k=1)[0]
        driver.find_element(By.ID, mapQuest21[aleatorioQuest21]).click()
        time.sleep(1)

        # Botão Próxima
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span').click()
        time.sleep(2)

        # Botão Enviar
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span').click()
        time.sleep(2)
        
        driver.quit()
        print("Formulário enviado com sucesso! - Prestador")
    
    else:
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
        time.sleep(2)       # Botão Próxima
        
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span').click()
        time.sleep(1)
        print("Formulário enviado com sucesso! - Não Prestador")
