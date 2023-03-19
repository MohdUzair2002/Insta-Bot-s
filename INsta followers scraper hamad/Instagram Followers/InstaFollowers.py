import requests
from requests.structures import CaseInsensitiveDict
from Creds import *
import csv
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
NumberofFollowers=NUMBER_OF_FOLLOWERS
username=[]
try:
    r=requests.Session()
    user_id=USER_ID
    url = f"https://i.instagram.com/api/v1/friendships/{user_id}/followers/?count=100&search_surface=follow_list_page"
    with open(f"InstaFollowers.csv","w", newline='' , encoding='UTF8') as A:
        writer = csv.DictWriter(A, fieldnames=["User id","User Name","Profile URL"])
        writer.writeheader()
        for i in range((NumberofFollowers//100)+1):

            headers = CaseInsensitiveDict()
            headers["authority"] = "i.instagram.com"
            headers["accept"] = "*/*"
            headers["accept-language"] = "en-US,en;q=0.9"
            headers["cookie"] = COOKIES
            headers["origin"] = "https://www.instagram.com"
            headers["referer"] = "https://www.instagram.com/"
            headers["sec-ch-ua"] = '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"'
            headers["sec-ch-ua-mobile"] = "?0"
            headers["sec-ch-ua-platform"] = "Windows"
            headers["sec-fetch-dest"] = "empty"
            headers["sec-fetch-mode"] = "cors"
            headers["sec-fetch-site"] = "same-site"
            headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
            headers["x-asbd-id"] = "198387"
            headers["x-csrftoken"] = CSRF_TOKEN
            headers["x-ig-app-id"] = "936619743392459"
            headers["x-ig-www-claim"] = X_IG_WWW_CLAIM



            resp = r.get(url, headers=headers)
            if resp.status_code == 200:
                for f in resp.json()['users']:
                 print(f['username'])
                 username.append(f['username'])
                Data=[{"User id":f"{u['pk']}","User Name" : f"{u['username']}","Profile URL":f"https://www.instagram.com/{u['username']}"}  for u in resp.json()["users"]]
                writer.writerows(Data)
                try:
                    id=resp.json()["next_max_id"]
                except:
                    break

                url = f"https://i.instagram.com/api/v1/friendships/{user_id}/followers/?count=100&max_id={id}&search_surface=follow_list_page"
                
                print(i+1)
            else:
                print("Limit Reached ;( Please use Another Account to Scrape More Followers....")
                break
except KeyboardInterrupt:
    print("Program Exited ;(")
except Exception as E:
    print("Error ;(")
    print(E)
else:
    print("Done :D")
chrome_options =webdriver.ChromeOptions()
s=Service(ChromeDriverManager().install())
chrome_options.add_argument("user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument("--start-maximized")
chrome = webdriver.Chrome(service=s,options=chrome_options)
wait=WebDriverWait(chrome, 60)
i=0
while(i<len(username)):
    url=f'https://www.instagram.com/{username[i]}/'
    chrome.get(url)
    try:
     message_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(text(),'Message')]")))
     message_button=chrome.find_element(By.XPATH,"//div[contains(text(),'Message')]")
     chrome.execute_script("arguments[0].click();", message_button)
     message_sending=wait.until(EC.element_to_be_clickable((By.XPATH,"//textarea[@placeholder='Message...']")))
     message_sending=chrome.find_element(By.XPATH,"//textarea[@placeholder='Message...']")
     message_sending.send_keys("WA")
     message_sending.send_keys(Keys.ENTER)
     
    except:
        print("The account message feature is off")
 
    i+=1