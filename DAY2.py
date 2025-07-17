from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window() ## maximize the browser window
## searching for a product
#driver.find_element(By.ID,"small-searchterms").send_keys("laptop")
#driver.find_element(By.XPATH,'//*[@id="small-search-box-form"]/button').click()
#clicking the register link uding LINK_TEXT and PARTIAL_LINK_TEXT

#driver.find_element(By.LINK_TEXT,'Register').click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()

## using the classname and tagname we able to select the multiple items at a time
slideritems=driver.find_elements(By.CLASS_NAME,"sublist first-level")
print(slideritems)
sleep(12)
driver.close()
driver.quit()
