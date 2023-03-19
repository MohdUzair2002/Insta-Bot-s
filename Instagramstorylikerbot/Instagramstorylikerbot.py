from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
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
bot_username = 'mohammaduzair361'
bot_password = 'uzair021'

profiles = ['gunther.super']
amount = 100

# 'usernames' or 'links'
result = 'usernames'

us = ''
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:8000")

# options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = web.Chrome("chromedriver",options=options)
# browser.set_window_size(400, 900)
browser.get('https://www.instagram.com')
time.sleep(random.randrange(3, 5))
# Enter username:
username_input = browser.find_element_by_name('username')
username_input.clear()
username_input.send_keys(bot_username)
time.sleep(random.randrange(2, 4))
# Enter password:
password_input = browser.find_element_by_name('password')
password_input.clear()
password_input.send_keys(bot_password)
time.sleep(random.randrange(1, 2))
password_input.send_keys(Keys.ENTER)
time.sleep(random.randrange(3, 5))
followers_list = []
try:
 notn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button']")))
 notn.click()
except:
        pass
for user in profiles:
    browser.get('https://instagram.com/' + user)
    time.sleep(random.randrange(3, 5))
    followers_button = browser.find_element(By.XPATH,"//a[contains(@href,'followers')]//span")
    count = int(followers_button.get_attribute('title').replace(",",""))
#     if ',' in count:
#             count = int(''.join(count.split(',')))
#     else:
#             count = int(count)
    if amount > count:
            print(f'You set amount = {amount} but there are {count} followers, then amount = {count}')
            amount = count
    followers_button.click()
    loops_count = int(amount / 12)
    print(f'Scraping. Total: {amount} usernames. Wait {loops_count} iterations')
    time.sleep(random.randrange(8,10))
    followers_ul = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul")
    time.sleep(random.randrange(5,7))
    try:		
        for i in range(1, loops_count + 1):
                browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_ul)
                time.sleep(random.randrange(8, 10))
                all_div = followers_ul.find_elements(By.TAG_NAME,"li")
                for us in all_div:
                        us = us.find_element_by_tag_name("a").get_attribute("href")
                        if result == 'usernames':
                                us1 = us.replace("https://www.instagram.com/", "")
                                us = us1.replace("/", "")
                        followers_list.append(us)
                time.sleep(1)
                f3 = open('userlist.txt', 'w')
                for list in followers_list:
                        print(list)
    except:
            pass
j=0
while(j<len(followers_list)):
    url='https://www.instagram.com/'+followers_list[j]+'/'
    browser.get(url)
    time.sleep(10)
    img=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//img[@crossorigin='anonymous']")))
    img.click()
    try:
        leng= browser.find_elements(By.XPATH,"//div[@class='_ac3r']/div")
        lengt=len(leng)
        print(lengt)

        i=0
        while (i<=lengt):

            try:
             noti=WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='_a9-- _a9_1']")))
             noti.click()
            except:
                pass
        ##        element=WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "open-elastic")))
        ##        cgrome.execute_script("arguments[0].click();", element)
     
            like=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='_abm0 _abl_']")))
            like.click()
            time.sleep(1)
            next=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/div[1]/div/section/div/button/div')))
            next.click()
            i+=1
            time.sleep(5)
    except:
        pass
    j+=1                   
followers_button = browser.find_element(By.XPATH,"//a[contains(@href,'followers')]//span")
count = int(followers_button.get_attribute('title').replace(",",""))