from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set the path to your ChromeDriver
chrome_driver_path = "C:/Users/Admin1/OneDrive/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe"
# Create a Service object
service = Service(chrome_driver_path)

# Initialize the WebDriver using the Service
driver = webdriver.Chrome(service=service)

# Open the fintech app
driver.get("https://demo.testfire.net/login.jsp")

# Maximize the window
driver.maximize_window()

# Test valid login
def valid_login():
    username_field = driver.find_element(By.ID, "uid")
    password_field = driver.find_element(By.ID, "passw")
    
    username_field.clear()
    password_field.clear()

    username_field.send_keys("admin")  # valid username
    password_field.send_keys("admin")  # valid password
    password_field.send_keys(Keys.RETURN)

    # Wait for the page to load
    time.sleep(2)

    # Verify successful login by checking the page title or presence of a logout button
    assert "Altoro Mutual" in driver.title

# Test invalid login
def invalid_login():
    driver.get("https://demo.testfire.net/login.jsp")
    username_field = driver.find_element(By.ID, "uid")
    password_field = driver.find_element(By.ID, "passw")
    
    username_field.clear()
    password_field.clear()

    username_field.send_keys("wrong_user")  # invalid username
    password_field.send_keys("wrong_pass")  # invalid password
    password_field.send_keys(Keys.RETURN)

    # Use WebDriverWait to wait for the error message to appear
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "LoginError"))
        ).text  # Waits for the error message to be visible and gets its text
        assert "Login Failed" in error_message
    except Exception as e:
        print("Error occurred:", e)
        driver.quit()  # Ensure the browser is closed if an error occurs

# Run both tests
valid_login()
invalid_login()

# Close the browser
driver.quit()
