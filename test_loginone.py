import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.dirname(__file__))

from loginpage import loginpage

class TestLogin:

    def setup_method(self):
        serv_obj = Service("chrome_driver_location")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def teardown_method(self):
        self.driver.quit()

    def test_valid_login(self):
        lgin = loginpage(self.driver)
        lgin.enter_username("student")
        lgin.enter_password("Password123")
        lgin.clicklog()

        success_message = self.driver.find_element(By.TAG_NAME, "h1").text
        assert success_message == "Logged In Successfully"

    def test_invalid_username(self):
        lgin = loginpage(self.driver)
        lgin.enter_username("incorrectUser")
        lgin.enter_password("Password123")
        lgin.clicklog()

        error_text = self.driver.find_element(By.ID, "error").text
        assert "Your username is invalid!" in error_text

    def test_invalid_password(self):
        lgin = loginpage(self.driver)
        lgin.enter_username("student")
        lgin.enter_password("incorrectPassword")
        lgin.clicklog()

        error_text_pass = self.driver.find_element(By.ID, "error").text
        assert "Your password is invalid!" in error_text_pass


    

        self.driver.quit() 
