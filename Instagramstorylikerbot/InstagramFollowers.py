from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
bot_username = 'mohammaduzair361'
bot_password = 'uzair021'
chrome_options = Options()
# chrome_options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)
# chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:8000")
S=Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=S,options=chrome_options)
# browser.get('https://www.instagram.com')
# wait = WebDriverWait(browser, 60)
# element = wait.until(EC.element_to_be_clickable((By.NAME,"username")))
# username=browser.find_element(By.NAME,"username")
# username.clear()
# username.send_keys(bot_username)
# password=browser.find_element(By.NAME,"password")
# password.clear()
# password.send_keys(bot_username)
# password.send_keys(Keys.ENTER)
profiles = ['gunther.super']
amount = 100
# try:
#  notn = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button']")))
#  browser.execute_script("arguments[0].click();", notn)
# except:
#         pass
all_followers=[]
# for user in profiles:
#     browser.get('https://instagram.com/' + user)
wait = WebDriverWait(browser, 60)
#     element = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@href,'followers')]")))
#     followers=browser.find_element(By.XPATH,"//a[contains(@href,'followers')]//span")
#     count = int(followers.get_attribute('title').replace(",",""))
#     if amount > count:
#             print(f'You set amount = {amount} but there are {count} followers, then amount = {count}')
#             amount = count
#     browser.execute_script("arguments[0].click();", followers)
#     wait = WebDriverWait(browser, 60)
#     element = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@role='dialog']//ul/div/li")))
#     while True:
#         FOLLOWERS=browser.find_elements(By.XPATH,"//div[@role='dialog']//ul/div/li")
#         if len(FOLLOWERS) >=count:
#             break
#         browser.execute_script("arguments[0].scrollIntoView();", FOLLOWERS[-1])
#     for follower in FOLLOWERS: 
#         userName=follower.find_elements(By.TAG_NAME,"a")[-1].text
#         userProfileLink=follower.find_elements(By.TAG_NAME,"a")[-1].get_attribute("href")
#         if userProfileLink not in all_followers:
#             all_followers.append(userProfileLink)

# element = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@href,'followers')]")))
# followers=browser.find_element(By.XPATH,"//a[contains(@href,'followers')]//span")
# count = int(followers.get_attribute('title').replace(",",""))
# if amount > count:
#         print(f'You set amount = {amount} but there are {count} followers, then amount = {count}')
#         amount = count
# browser.execute_script("arguments[0].click();", followers)
# wait = WebDriverWait(browser, 60)
# element = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@role='dialog']//ul/div/li")))
# print(count)
# end1=0
# end2=0
# while True:

#     try:
#         FOLLOWERS=browser.find_elements(By.XPATH,"//div[@role='dialog']//ul/div/li")

#         if end1==len(FOLLOWERS):
#            end2+=1
#         else:
#             end2=0
#         end1=len(FOLLOWERS)
#         if len(FOLLOWERS) >=count or end2>=10:
#             break
#         browser.execute_script("arguments[0].scrollIntoView();", FOLLOWERS[-1])
#         time.sleep(4)
#         print(len(FOLLOWERS))
#     except:

#         pass

# for follower in FOLLOWERS: 
#     userName=follower.find_elements(By.TAG_NAME,"a")[-1].text
#     userProfileLink=follower.find_elements(By.TAG_NAME,"a")[-1].get_attribute("href")
#     if userProfileLink not in all_followers:
#         if(len(all_followers)==0):
#             all_followers.append('https://www.instagram.com/anum16_/')
#         all_followers.append(userProfileLink)
i=0

# print(all_followers)
# while(i<=1):
#     # browser.get('https://www.instagram.com/anum16_/')
#     img1=wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@class='_aa8j']")))
#     browser.execute_script("arguments[0].click();", img1)
#     try:
#         try:
#          leng=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='_ac3r']")))
#          leng= browser.find_elements(By.XPATH,"//div[@class='_ac3r']")
#          lengt=len(leng)
#          print(lengt)
#         except:
#             break
            
#         j=0
#         while (j<=lengt):
            
#             try:
#              noti=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='_a9-- _a9_1']")))
#              noti= browser.find_element(By.XPATH,"//button[@class='_a9-- _a9_1']")
#              browser.execute_script("arguments[0].click();", noti)
#             except:
#                 pass
#     ##        element=WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "open-elastic")))
#     ##        cgrome.execute_script("arguments[0].click();", element)
#             try:
#                 like=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='_abm0 _abl_']")))
#                 like=browser.find_element(By.XPATH,"//div[@class='_abm0 _abl_']")
#                 browser.execute_script("arguments[0].click();", like)
#                 j+=1

#             except:
#                 j+=1
#                 pass
#     except:
#             pass
    # i+=1
while(i<1):
    try:
     img=wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='_aa8h']")))
     browser.execute_script("arguments[0].click();", img)
     length=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='_ac3r']")))
     play_butt=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@aria-label='Play']")))
     browser.execute_script("arguments[0].click();", play_butt) 
     nex_butt=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@aria-label='Next']")))
     browser.execute_script("arguments[0].click();", nex_butt)

    except:
        pass
    i+=1