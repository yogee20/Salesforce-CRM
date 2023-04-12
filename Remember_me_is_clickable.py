import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://grofersindiapvtltd3.my.salesforce.com/")

driver.maximize_window()

print(driver.title)

rememeber_me = driver.find_element(By.XPATH,"//*[@id='rememberUn']").is_selected()

print(rememeber_me)    ##False as it  was unclicked

time.sleep(3)

rememeber_me = driver.find_element(By.XPATH,"//*[@id='rememberUn']").click()

time.sleep(3)

rememeber_me = driver.find_element(By.XPATH,"//*[@id='rememberUn']").is_selected()

print(rememeber_me)    ##True as it  was clicked

