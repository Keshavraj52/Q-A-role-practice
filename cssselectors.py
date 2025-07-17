from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window() ## maximize the browser window
#driver.find_element(By.CSS_SELECTOR,'input#email').send_keys("keshavraj pore") #### we can search using the tag#name and id
driver.find_element(By.CSS_SELECTOR,'input.inputtext').send_keys("rada rada") ## tagname.classname
driver.find_element(By.CSS_SELECTOR,'input[type=password]').send_keys(12345678)## tagname[attribute=value]
#we can also pass like  tagname.classname[attribute=value]
