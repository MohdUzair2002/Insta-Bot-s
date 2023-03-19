from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
accounts=[]
file1=open('accounts.csv')
csvreader=csv.reader(file1)
for row in  csvreader:
    accounts.append(row)
file2=open('followers.csv')
csvreader=csv.reader(file2)
for row in  csvreader:
    accounts.append(row)
email='markusabbott58'
password='A8vJRtD'
# https://www.instagram.com/zanebradshawofficial/
chrome_options =webdriver.ChromeOptions()
s=Service(ChromeDriverManager().install())
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=s,options=chrome_options)
wait=WebDriverWait(driver, 60)
a = ActionChains(driver)
url='https://www.instagram.com/'
driver.get(url)
email1= wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@aria-label='Phone number, username, or email']")))
email1=driver.find_element(By.XPATH,"//input[@aria-label='Phone number, username, or email']")
email1.send_keys(email)
password1=driver.find_element(By.XPATH,"//input[@aria-label='Password']")
password1.send_keys(password)
time.sleep(3)
login=driver.find_element(By.XPATH,"//button[@class='_acan _aiit _acap _aijb _acas _aj1-']")
driver.execute_script("arguments[0].click();", login)
time.sleep(5)

driver.get('https://www.instagram.com/itszanebradshaw/')
try:
    follow_button=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='_acan _aiit _acap _aijb _acas _aj1-']")))
    follow_button=driver.find_element(By.XPATH,"//button[@class='_acan _aiit _acap _aijb _acas _aj1-']")
    driver.execute_script("arguments[0].click();", follow_button)
except:
    pass
message_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o  _abb0 _ab9s _abcm']")))
message_button=driver.find_element(By.XPATH,"//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o  _abb0 _ab9s _abcm']")
# driver.execute_script("arguments[0].click();", message_button)
message_button.click()
not_now_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='_a9-- _a9_1']")))
not_now_button=driver.find_element(By.XPATH,"//button[@class='_a9-- _a9_1']")
driver.execute_script("arguments[0].click();", not_now_button)


# inbox_profile=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9k _ab9p _abcm']")))
# inbox_profile=driver.find_elements(By.XPATH,"//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9k _ab9p _abcm']")[0]
# driver.execute_script("arguments[0].click();", inbox_profile)
message_profile=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd']")))
message_profile=driver.find_elements(By.XPATH,"//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd']")[-1]
a.move_to_element(message_profile).perform()
time.sleep(5)
menu=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='_abm0 _abl_']")))
menu=driver.find_element(By.XPATH,"//div[@class='_abm0 _abl_']")
# driver.execute_script("arguments[0].click();", menu)
menu.click()
# menu.click()
forward_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='_acan _aiit _acao _aija _acau _aj1-']")))
forward_button=driver.find_elements(By.XPATH,"//button[@class='_acan _aiit _acao _aija _acau _aj1-']")[1]
driver.execute_script("arguments[0].click();", forward_button)
# forward_button.click()
input_profiile_name=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='queryBox']")))
input_profiile_name=driver.find_element(By.XPATH,"//input[@name='queryBox']")
input_profiile_name.send_keys("zanetrillion")
click_profile=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='_aacl _aaco _aacw _aacx _aad6']")))
click_profile=driver.find_elements(By.XPATH,"//div[@class='_aacl _aaco _aacw _aacx _aad6']")[0]
driver.execute_script("arguments[0].click();", click_profile)
send_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='_aagz' ]")))
send_button=driver.find_element(By.XPATH,"//div[@class='_aagz' ]")
driver.execute_script("arguments[0].click();", send_button)
driver.get('https://www.instagram.com/direct/t/')
profile=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class=' _ab8s _ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p _abcm']")))
profile=driver.find_elements(By.XPATH,"//div[@class=' _ab8s _ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p _abcm']")[0]
driver.execute_script("arguments[0].click();", profile)
profile.click()
text_message=wait.until(EC.element_to_be_clickable((By.XPATH,"//textarea[@placeholder='Message...']")))
text_message=driver.find_element(By.XPATH,"//textarea[@placeholder='Message...']")
# text_message.send_keys("You probably won’t believe this…\nBut @leadsfolio has helped literally thousands of people scale their Instagram pages. Some to 20k+, and others to hundreds of thousands.\n If you want to scale your IG page to the next level, message @leadsfolio the keyword “GROW” to book a call with them today! ")
string = f"You probably won’t believe this…\nBut @leadsfolio has helped literally thousands of people scale their Instagram pages. Some to 20k+, and others to hundreds of thousands.\n If you want to scale your IG page to the next level, message @leadsfolio the keyword “GROW” to book a call with them today!"
action = ActionChains(driver)
for part in string.split('\n'):
            action.send_keys(part)
            action.key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).perform()
            action.key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).perform()
text_message.send_keys(Keys.ENTER)
# send_button1=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='_acan _acao _acas _aj1-']")))
# send_button1=driver.find_elements(By.XPATH,"//button[@class='_acan _acao _acas _aj1-']")[2]
# driver.execute_script("arguments[0].click();", send_button1)
# send_button1.click()

time.sleep(20)



