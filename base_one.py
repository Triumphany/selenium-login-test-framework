from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv_obbj = Service('chrome_driver_location')
driver = webdriver.Chrome(service=serv_obbj)

driver.get("https://practicetestautomation.com/practice-test-login/")
username = driver.find_element(By.XPATH, "//input[@id='username']")
username.send_keys("student")

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys("Password123")

submit = driver.find_element(By.XPATH, "//button[@id='submit']")
submit.click()

logout = driver.find_element(By.LINK_TEXT, "Log out")
logout.click()
print("test success")
driver.quit()