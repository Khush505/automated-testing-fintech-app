from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up your driver as before
chrome_driver_path = "C:/Users/Admin1/OneDrive/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

def field_validation_test():
    try:
        driver.get("https://demo.testfire.net/bank/transfer.jsp")

        # Wait for the transfer button to be clickable
        submit_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "transfer"))
        )
        submit_btn.click()

        time.sleep(2)

        # Check for error messages
        error_message = driver.find_element(By.ID, "ErrorMessage").text
        assert "All fields are required" in error_message
        print("Field Validation Test Passed")

    except Exception as e:
        print(f"Field Validation Test Failed: {e}")

# Run the validation test
field_validation_test()

# Ensure the browser is closed
driver.quit()
