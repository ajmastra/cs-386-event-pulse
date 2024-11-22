import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configures logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constant for Delay change if needed
DELAY = 1

def test_login(email, password):
    logging.info("Starting the login test...")
    driver = webdriver.Chrome()

    try:
        # Opens the login page
        driver.get("https://cs-386-event-pulse.onrender.com/login")
        logging.info("Navigated to the login page.")
        time.sleep(DELAY)
        # Wait for the email and password fields to populate
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        password_field = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.CLASS_NAME, "btn-primary")
        logging.info("Located email, password fields, and login button.")
        time.sleep(DELAY)
        
        # Entering credentials and log in
        email_field.send_keys(email)
        password_field.send_keys(password)
        login_button.click()
        logging.info("Entered credentials and clicked login.")
        time.sleep(DELAY)
        
        # Verifing the success message
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))
        ).text
        logging.info(f"Success message found: {success_message}")
        time.sleep(DELAY)
        assert "Logged in successfully!" in success_message, "Login failed or incorrect success message."

    except Exception as error_exception:
        logging.error("Test failed with an unexpected error: %s", error_exception)
        print("Current page source:\n", driver.page_source)
    finally:
        driver.quit()
        logging.info("Browser closed and test completed.")

# Run the test
test_login("testuser@gmail.com", "acceptancetest")
