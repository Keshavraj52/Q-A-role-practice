from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get("http://automationpractice.com/index.php")
driver.maximize_window() ## maximize the browser window
sliders=driver.find_elements(By.CLASS_NAME,"homeslider-container")## finding elements by class name
print(sliders)# it will return a list of elements
