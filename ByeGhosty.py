#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#

name = 'USERNAME'
psswd = "PASSWORD"

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

#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#s
second_plane = Options()
second_plane.add_argument('--headless')
driver = webdriver.Chrome()

driver.get('https://www.instagram.com/accounts/login/?next=https%3A%2F%2Fwww.instagram.com%2Flogin%2F%3F__coig_login%3D1'); wait(0.5)
driver.find_element(By.CLASS_NAME, '_a9--._a9_1').click(); wait(0.5)

driver.find_element(By.NAME, 'username').send_keys(name)
driver.find_element(By.NAME, 'password').send_keys(psswd); wait(0.15)
driver.find_element(By.CLASS_NAME, '_acan._acap._acas._aj1-').click(); wait(7)
driver.get(f'https://www.instagram.com/{name}/following/?next=%2F'); wait(2)

#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#

try:
    box_fllw = driver.find_element(By.CLASS_NAME, '_aano')
except:
    print('Test 1 FAiled')

try:
    box_fllw = driver.find_element(By.CSS_SELECTOR, '._aano')
except:
    print('Test 4 FAiled')

soup = BeautifulSoup(driver.page_source, 'html.parser')
seguidores = soup.find_all('span', {'class':'_ac2a'})
lista_seguidores = [seguidor.text for seguidor in seguidores]; seguidos=lista_seguidores[2]

scroll = 0

while scroll < int(int(seguidos)//6):
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', box_fllw)
    time.sleep(1)
    scroll += 1
    print(scroll)

    soup2 = BeautifulSoup(driver.page_source, 'html.parser')
    divs = soup2.find_all('div', {'class': 'x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1'})

    with open('seguidos.txt', 'a') as f:
        for div in divs:
            f.write(div.text+'\n')
driver.close()

with open('seguidos.txt', 'r') as r:
    for line in r:
        with open('seguidos_limpio.txt', 'r') as r2:
            if line not in r2:
                with open('seguidos_limpio.txt', 'a') as a:
                    a.write(line)

with open('seguidos_limpio.txt', 'r') as r3:
    driver = webdriver.Chrome(chrome_options=second_plane)
    driver.get('https://www.instagram.com/accounts/login/?next=https%3A%2F%2Fwww.instagram.com%2Flogin%2F%3F__coig_login%3D1'); wait(0.5)
    driver.find_element(By.CLASS_NAME, '_a9--._a9_1').click(); wait(0.5)

    driver.find_element(By.NAME, 'username').send_keys(name)
    driver.find_element(By.NAME, 'password').send_keys(psswd); wait(0.15)
    driver.find_element(By.CLASS_NAME, '_acan._acap._acas._aj1-').click(); wait(7)

    for line in r3: # Line == User name
        driver.get(f'https://www.instagram.com/{line}/following/?next=%2F'); wait(2)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        div = soup.find('div', {'class': 'x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1'})
        try:
            div = div.text

            if div != name:
                driver.get(f'https://www.instagram.com/{line}/?next=%2F'); wait(1)
                driver.find_element(By.CSS_SELECTOR, '._acan._acap._acat._aj1-').click(); wait(1)
                try:
                    elementos = driver.find_elements(By.CSS_SELECTOR, '.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1cy8zhl.x1oa3qoh.x1nhvcw1')
                    elemento = elementos[-1]; elemento.click()
                except:
                    elementos = driver.find_elements(By.CSS_SELECTOR, '.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1cy8zhl.x1oa3qoh.x1nhvcw1')
                    elemento = elementos[-1]; elemento.click()
        except:
            pass

        wait(1)
