from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set the path to your ChromeDriver
chrome_driver_path = "C:/Users/Admin1/OneDrive/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Create a Service object
service = Service(chrome_driver_path)

# Initialize the WebDriver using the Service
driver = webdriver.Chrome(service=service)

try:
    # Navigate to the transfer page
    driver.get("https://demo.testfire.net/bank/transfer.jsp")

    # Select from account
    from_account = driver.find_element(By.ID, "fromAccount")
    from_account.send_keys("800000")

    # Select to account
    to_account = driver.find_element(By.ID, "toAccount")
    to_account.send_keys("800001")

    # Enter the amount
    amount = driver.find_element(By.ID, "transferAmount")
    amount.send_keys("500")  # Transfer $500

    # Submit the transaction
    submit_btn = driver.find_element(By.ID, "transfer")
    submit_btn.click()

    # Wait for the transaction to complete
    time.sleep(2)

    # Check for success message
    confirmation = driver.find_element(By.ID, "conf_message").text
    assert "Transaction Complete" in confirmation

    print("Transaction Test Passed: ", confirmation)

except Exception as e:
    print("Transaction Test Failed: ", e)

finally:
    driver.quit()  # Ensure the browser is closed after the test
