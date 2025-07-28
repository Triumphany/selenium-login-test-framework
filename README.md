# selenium-login-test-framework

This project is a simple Selenium-based automation framework for testing login functionality using the **Practice Test Automation** website. It is built using Python and Pytest, and follows the **Page Object Model (POM)** design pattern.

## Features

- Automates login flow using Selenium WebDriver
- Structured using Page Object Model (`loginpage.py`)
- Includes Pytest test suite with:
  - ✅ Valid login test
  - ❌ Invalid username test
  - ❌ Invalid password test
- Supports Chrome browser (via chromedriver)
- Generates readable output and ready for extension with HTML reports

---

## 📁 Project Structure
selenium-login-test-framework/
│
├── base_one.py # Standalone script: direct login + logout
├── loginpage.py # Page Object Model for login page
├── test_loginone.py # Pytest test suite
├── README.md # Project documentation
└── requirements.txt # (Optional) dependencies list

## 🔧 Prerequisites

- Python 3.7+
- Google Chrome
- ChromeDriver (placed in `C:\drivers\chromedriver-win64\chromedriver.exe`)
- Python packages:
  ```bash
  pip install selenium pytest

  pytest test_loginone.py

