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


class Instagram():
	def __init__(self, username, password):
		self.username = username
		self.password = password
		options = Options()
		options.add_experimental_option("excludeSwitches", ["enable-logging"])
		self.browser = web.Chrome("chromedriver",options=options)
		self.browser.set_window_size(400, 900)

	def close_browser(self):
		self.browser.close()
		self.browser.quit()

	def login(self):
		browser = self.browser
		try:
			browser.get('https://www.instagram.com')
			time.sleep(random.randrange(3, 5))
			# Enter username:
			username_input = browser.find_element_by_name('username')
			username_input.clear()
			username_input.send_keys(self.username)
			time.sleep(random.randrange(2, 4))
			# Enter password:
			password_input = browser.find_element_by_name('password')
			password_input.clear()
			password_input.send_keys(self.password)
			time.sleep(random.randrange(1, 2))
			password_input.send_keys(Keys.ENTER)
			time.sleep(random.randrange(3, 5))
			print(f'[{self.username}] Successfully logged on!')
		except Exception as ex:
			print(f'[{self.username}] Authorization fail')
			self.close_browser()

	def xpath_exists(self, url):
		browser = self.browser
		try:
			browser.find_element_by_xpath(url)
			exist = True
		except NoSuchElementException:
			exist = False
		return exist

	def get_followers(self, users, amount):
		browser = self.browser

		followers_list = []
		for user in users:
			browser.get('https://instagram.com/' + user)
			time.sleep(random.randrange(3, 5))
			followers_button = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/ul/li[2]/a/div/span')
			count = followers_button.get_attribute('title')
			if ',' in count:
				count = int(''.join(count.split(',')))
			else:
				count = int(float(count))
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
					all_div = followers_ul.find_elements_by_tag_name("li")
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
			
                            url='https://www.instagram.com/'+followers_list[i]+'/'
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
                               i+=1
                               time.sleep(5)
                           except:
                              pass
                                
                           self.close_browser()
                        
    


bot = Instagram(bot_username, bot_password)
bot.login()
followers = bot.get_followers(profiles, amount)
