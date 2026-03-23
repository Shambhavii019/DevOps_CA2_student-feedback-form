from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

print("Starting test...")

driver = webdriver.Chrome()

file_path = "file://" + os.path.abspath("index.html")
print("Opening:", file_path)

driver.get(file_path)

time.sleep(3)

print("Filling form...")

driver.find_element(By.ID, "name").send_keys("John Doe")
driver.find_element(By.ID, "email").send_keys("john@gmail.com")
driver.find_element(By.ID, "mobile").send_keys("9876543210")

driver.find_element(By.ID, "dept").send_keys("CSE")
driver.find_element(By.XPATH, "//input[@value='Male']").click()

driver.find_element(By.ID, "feedback").send_keys(
    "This is a very good platform for learning and improving skills daily"
)

time.sleep(2)

print("Submitting form...")
driver.find_element(By.XPATH, "//button[text()='Submit']").click()

time.sleep(2)

try:
    alert = driver.switch_to.alert
    print("Alert message:", alert.text)
    alert.accept()
except:
    print("No alert found")

time.sleep(2)

driver.quit()

print("Test completed!")