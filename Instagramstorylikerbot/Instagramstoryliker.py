from selenium import webdriver
from instabot import Bot
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
from bs4 import BeautifulSoup as bs
import requests
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
username = 'mohammaduzair361'
password = 'uzair021'
w=['imrankhan.pti','mercedesbenz']
i=0
chrome_options = Options()
##chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:8000")
s=Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s,options=chrome_options)
url='https://www.instagram.com/'
chrome.get(url)
time.sleep(4)
usern = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.NAME,"username")))
usern.send_keys(username)
passw =WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//input[@aria-label='Password']")))
passw.send_keys(password)
time.sleep(5.5)
log_in=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
log_in=log_in.click()
time.sleep(5)
try:
 notn = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button']")))
 notn.click()
except:
   pass
time.sleep(25)
for i in range (len(w)):
    url='https://www.instagram.com/'+w[i]+'/'
    chrome.get(url)
    time.sleep(10)
    img=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH, "//img[@crossorigin='anonymous']")))
    img.click()
    try:
        leng= chrome.find_elements(By.XPATH,"//div[@class='_ac3r']/div")
        lengt=len(leng)
        print(lengt)

        i=0
        while (i<=lengt):
            
            try:
             noti=WebDriverWait(chrome, 2).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='_a9-- _a9_1']")))
             noti.click()
            except:
                pass
    ##        element=WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "open-elastic")))
    ##        cgrome.execute_script("arguments[0].click();", element)
            
            like=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='_abm0 _abl_']")))
            like.click()
            time.sleep(1)
            i+=1
        time.sleep(5)
    except:
            pass
