from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

# Start browser
driver = webdriver.Chrome()

# Go to the Quiz Generator page
driver.get("https://keshavrajpore.netlify.app/quiz-generator")
sleep(2)  # Allow the page to load

# Pass the key (assuming it's a text input)
key_input = driver.find_element(By.ID, "key")  # Change to correct ID or NAME
key_input.send_keys("AIzaSyCxNcku_m8WcYpvlvaxzXlW3jX8T7xjwt0")         # Replace with your actual key

# Select topic from dropdown
topic_dropdown = Select(driver.find_element(By.ID, "topic"))  # Change to correct ID or NAME
topic_dropdown.select_by_visible_text("Python")               # Replace with actual topic

# Select difficulty level
difficulty_dropdown = Select(driver.find_element(By.ID, "difficulty"))  # Again, confirm ID
difficulty_dropdown.select_by_visible_text("Medium")                    # Replace with desired level

# Click Create Quiz button
create_quiz_btn = driver.find_element(By.ID, "create-quiz")  # Confirm actual ID or use another selector
create_quiz_btn.click()

# Optional: wait to see the result or scrape content
sleep(5)

# Close browser
driver.quit()