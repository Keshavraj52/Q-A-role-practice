from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
def test_login(url, username, password):
    driver=webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.ID,"username").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    actual_title= driver.title
    expected_title="The Internet"

    if actual_title == expected_title:
        print("Test Passed")
    else:
        print("Test Failed")

test_login("https://the-internet.herokuapp.com/login", "tomsmith", "SuperSecretPassword!")