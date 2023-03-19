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
profile_name=input("Enter the profile/page name who's followers you want DM:- ")
message=input("Enter the mesage you want to search")
chrome_options =webdriver.ChromeOptions()
s=Service(ChromeDriverManager().install())
chrome_options.add_argument("user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=s,options=chrome_options)
wait=WebDriverWait(driver, 60)
url=f'https://www.instagram.com/{profile_name}/'
driver.get(url)
followers = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@href,'followers')]//span")))
followers=driver.find_element(By.XPATH,"//a[contains(@href,'followers')]//span")
followers.click()
followers_total_count=driver.find_elements(By.XPATH,"//span[@class='_ac2a']")[1]
print(f"the total no of followers of this profule or page is:-{str(followers_total_count.text)}")
main_count=49
if "M" in followers_total_count.text:
 ss=followers_total_count.text.split("M")[0]
 followers_total_count=float(ss)*100000
elif "K" in followers_total_count.text:
    ss=followers_total_count.text.split("K")[0]
    followers_total_count=float(ss)*1000

if main_count >int(followers_total_count):
    working_count=int()
else:
    working_count=main_count
followers_scraping=driver.find_elements(By.XPATH,"//div[@class='_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm']")
leng=len(followers_scraping)
while(leng  <working_count):

    followers_scraping=driver.find_elements(By.XPATH,"//div[@class='_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm']")
    leng=len(followers_scraping)
    try:
     driver.execute_script("arguments[0].scrollIntoView();", followers_scraping[-1])
    except:
        pass
    print(leng)
    
user_names=driver.find_elements(By.XPATH,"//div[@class='_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm']")
i=0
usernames_list=[]
while(i< len(user_names)):
    usernames_list.append(user_names[i].text.split('\n')[0])
    # print(user_names[i].text)
    print(user_names[i].text.split('\n')[0])
    i+=1


i=0
j=0
while(i<len(usernames_list)):
    print(f"the work is progressing on profile{usernames_list[i]} now")
    print("...........................")
    url=f'https://www.instagram.com/{usernames_list[i]}/'
    driver.get(url)
    try:
     message_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(text(),'Message')]")))
     message_button=driver.find_element(By.XPATH,"//div[contains(text(),'Message')]")
     driver.execute_script("arguments[0].click();", message_button)
     message_sending=wait.until(EC.element_to_be_clickable((By.XPATH,"//textarea[@placeholder='Message...']")))
     message_sending=driver.find_element(By.XPATH,"//textarea[@placeholder='Message...']")
     message_sending.send_keys(message)
     message_sending.send_keys(Keys.ENTER)
     j+=1
     if message_button:
      print(f"The total number of messages send uptil now are {j}")
    except:
        print("The account message feature is off")
    
    i+=1
    print(f"The total number of profiles opened till now {i}")