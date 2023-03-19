from mechanize import Browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import re
chrome_options =webdriver.ChromeOptions()
s=Service(ChromeDriverManager().install())
chrome_options.add_argument("user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument("--start-maximized")
browser = webdriver.Chrome(service=s,options=chrome_options)
wait=WebDriverWait(browser, 60)
url='https://www.instagram.com/abdullahadenwala/'
browser.get(url)
followers = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@href,'followers')]//span")))
time.sleep(10)
followers=browser.find_element(By.XPATH,"//a[contains(@href,'followers')]//span")
followers.click()
followers_total_count=browser.find_elements(By.XPATH,"//span[@class='_ac2a']")[1]
print(f"the total no of followers of this profule or page is:-{int(followers_total_count.text)}")
main_count=600
if main_count >int(followers_total_count.text):
    working_count=int(followers_total_count.text)
else:
    working_count=main_count
time.sleep(5)
followers_scraping=browser.find_elements(By.XPATH,"//div[@class='_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm']")
leng=len(followers_scraping)
while(leng  <working_count):

    followers_scraping=browser.find_elements(By.XPATH,"//div[@class='_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm']")
    leng=len(followers_scraping)
    browser.execute_script("arguments[0].scrollIntoView();", followers_scraping[-1])
    print(leng)
    
user_names=browser.find_elements(By.XPATH,"//div[@class='_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm']")
i=0
usernames_list=[]
while(i< len(user_names)):
    usernames_list.append(user_names[i].text)
    # print(user_names[i].text)
    print(user_names[i].text.split('\n')[0])
    i+=1
time.sleep(10)