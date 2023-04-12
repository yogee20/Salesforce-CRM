import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://grofersindiapvtltd3.my.salesforce.com/")

driver.maximize_window()

print(driver.title)

time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='forgot_password_link']").click()

time.sleep(1)
