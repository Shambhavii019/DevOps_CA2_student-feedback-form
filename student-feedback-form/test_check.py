# test_check.py

from selenium import webdriver

print("Opening browser...")

driver = webdriver.Chrome()
driver.get("https://www.google.com")

input("Press Enter to close browser...")

driver.quit()