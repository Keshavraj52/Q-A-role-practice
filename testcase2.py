from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from time import sleep
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/ref=nav_logo")
assert "Amazon" in driver.title
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("laptop") ## accessing the search box using the ID

driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click() ## accessing the search button using xpath

sleep(6)
driver.close()
