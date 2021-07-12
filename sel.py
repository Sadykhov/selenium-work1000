from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pandas as pd
import random

nomera = {'nomer': []}
nomera = pd.DataFrame(data=nomera)

for i in range(1000):
    nomer1 = ''
    for j in range(7):
        nomer1 = nomer1 + str(random.randint(0, 9))

    nomera.loc[i] = '926' + nomer1

for i in range(1000):
    driver = webdriver.Chrome(executable_path="C:\\Users\\PC\\Downloads\\selenium\\chromedriver.exe")
    driver.get(
        "https://oauth.telegram.org/auth?bot_id=1738693759&origin=http%3A%2F%2Fkarambamba.pythonanywhere.com&embed=1&request_access=write")

    elem2 = driver.find_element_by_xpath('//*[@id="login-phone"]')
    elem2.send_keys(int(nomera[i]))
    elem2.send_keys(Keys.ENTER)
    driver.quit()






