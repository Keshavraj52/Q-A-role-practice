from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep 

driver= webdriver.Chrome()
driver.get("https://keshavrajpore.netlify.app/")
driver.maximize_window()  # Maximize the browser window
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/button').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/input').send_keys("project")
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/button[1]').click()
sleep(17)