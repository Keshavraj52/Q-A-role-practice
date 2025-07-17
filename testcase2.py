from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/ref=nav_logo")
assert "Amazon" in driver.title
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("laptop")
driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()
## getting the product names and prices
product_names = driver.find_elements(By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"]')
product_prices = driver.find_elements(By.XPATH, '//span[@class="a-price-whole"]')
# Extracting text from the elements
names = [name.text for name in product_names]
prices = [price.text for price in product_prices]
# Creating a DataFrame
data = pd.DataFrame({
    'Product Name': names,
    'Price': prices
})
# Saving the DataFrame to a CSV file
data.to_csv('amazon_laptops.csv', index=False)
sleep(6)
driver.close()