import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set the path to your ChromeDriver
chrome_driver_path = "C:/Users/Admin1/OneDrive/Desktop/chromedriver-win64/chromedriver.exe"

# Ensure the executable is found in the PATH
os.environ["PATH"] += os.pathsep + os.path.dirname(chrome_driver_path)

# Create a Service object
service = Service(chrome_driver_path)

# Initialize the WebDriver variable
driver = None

try:
    # Initialize the WebDriver using the Service
    driver = webdriver.Chrome(service=service)
    driver.get("https://demo.testfire.net/")
    driver.maximize_window()

    # Logout Test
    def logout_test():
        # Wait for the logout button to be clickable
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "MenuHyperLink3"))
        )
        logout_button.click()

        time.sleep(2)  # Wait for logout to complete

        # Verify the user is back on the login page
        assert "Login" in driver.title

    # Run the logout test
    logout_test()
    print("Logout Test Passed: User logged out successfully.")

except Exception as e:
    print("Logout Test Failed: ", e)

finally:
    if driver is not None:
        driver.quit()  # Ensure the browser is closed after the test
