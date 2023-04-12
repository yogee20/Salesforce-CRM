import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://grofersindiapvtltd3.my.salesforce.com/")

driver.maximize_window()

print(driver.title)

username = driver.find_element(By.XPATH, "//*[@id='username']").send_keys("yogee.dhotre1-zl44@force.com")

time.sleep(1)

password = driver.find_element(By.XPATH, "//*[@id='password']").send_keys("Neera@123")

time.sleep(1)

remember_me = driver.find_element(By.XPATH,"//*[@id='rememberUn']").click()

time.sleep(1)


logIn = driver.find_element(By.XPATH,"//*[@id='Login']").click()    ###XPATH should be capital.
                                                                    ##By and by is different.
time.sleep(2)

leads = driver.find_element(By.XPATH, "//*[@text()='slds-icon']")
leads.click()

time.sleep(2)






