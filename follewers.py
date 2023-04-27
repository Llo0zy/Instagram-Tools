#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#

nombre = 'USERNAME'
contra = "PASSWORD"

tofllw = 'INFLUNSER' # Will follow all followers of tofllw

#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

import time
from time import sleep as wait
from bs4 import BeautifulSoup
 
#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#
def macro_lista(name, psswd, infu):
    second_plane = Options()
    second_plane.add_argument('--headless')

    driver = webdriver.Chrome()

    driver.get('https://www.instagram.com/accounts/login/?next=https%3A%2F%2Fwww.instagram.com%2Flogin%2F%3F__coig_login%3D1'); wait(0.5)
    driver.find_element(By.CLASS_NAME, '_a9--._a9_1').click(); wait(0.5)

    driver.find_element(By.NAME, 'username').send_keys(name)
    driver.find_element(By.NAME, 'password').send_keys(psswd); wait(0.15)
    driver.find_element(By.CLASS_NAME, '_acan._acap._acas._aj1-').click(); wait(7)
    driver.get(f'https://www.instagram.com/{infu}/followers/'); wait(5)

    #-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#

    try:
        box_fllw = driver.find_element(By.CLASS_NAME, '_aano')
    except:
        print('Test 1 FAiled')

    try:
        box_fllw = driver.find_element(By.CSS_SELECTOR, '._aano')
    except:
        print('Test 4 FAiled')

    #-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#


    soup = BeautifulSoup(driver.page_source, 'html.parser')
    seguidores = soup.find_all('span', {'class':'_ac2a'})
    lista_seguidores = [seguidor.text for seguidor in seguidores]; seguidores=lista_seguidores[1]

    scroll = 0

    while scroll < int(int(seguidores)//6):
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', box_fllw)
        time.sleep(1)
        scroll += 1
        print(scroll)

        soup2 = BeautifulSoup(driver.page_source, 'html.parser')
        divs = soup2.find_all('div', {'class': 'x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1'})

        for div in divs:
            with open('fllw22.txt', 'r') as r:
                if div.text not in r:
                    with open('fllw22.txt', 'a') as f:
                        if '9' not in div.text:
                            f.write(div.text+'\n')
    driver.close()

macro_lista(nombre, contra, nombre)

def seguirlistita(name, psswd): 

    with open('a.txt', 'r') as r:
        # Login
        second_plane = Options()
        second_plane.add_argument('--headless')

        driver = webdriver.Chrome()
        driver.get('https://www.instagram.com/accounts/login/?next=https%3A%2F%2Fwww.instagram.com%2Flogin%2F%3F__coig_login%3D1'); wait(0.5)

        driver.find_element(By.CLASS_NAME, '_a9--._a9_1').click(); wait(0.5)
        driver.find_element(By.NAME, 'username').send_keys(name)
        driver.find_element(By.NAME, 'password').send_keys(psswd)
        driver.find_element(By.CLASS_NAME, '_acan._acap._acas._aj1-').click(); wait(7)
        for user in r:
            # Follow
            driver.get(f'https://www.instagram.com/{user}'); wait(1)

            try: # Cuenta solicitada o siguiendo
                driver.find_element(By.CSS_SELECTOR, '._acan._acap._acat._aj1-')

            except:
                try: # Cuenta privada
                    driver.find_element(By.CLASS_NAME, '_aa_u')
                    with open('priv2fllw.txt', 'a') as f:
                        f.write(user)

                except NoSuchElementException: # Cuenta publica
                    with open('public2fllw.txt', 'a') as f:
                        f.write(user)

                try:
                    driver.find_element(By.CSS_SELECTOR, '._acan._acap._acas._aj1-').click()
                except:
                    print('Failed :(')

            #-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#
    
    driver.close()
