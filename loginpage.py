from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class loginpage:
    textbox_username_id = "username"
    textbox_password_id = "password"
    submit_button_id ="XPATH"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, utext):    
        username = self.driver.find_element(By.XPATH, "//input[@id='username']")
        username.send_keys(utext)

    def enter_password(self, ptext):    
        username = self.driver.find_element(By.XPATH, "//input[@id='password']")
        username.send_keys(ptext)

    def clicklog(self):
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()