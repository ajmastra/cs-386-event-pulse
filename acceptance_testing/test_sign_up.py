import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Global delay variable
# Edit if needed
DELAY = 2  

def test_sign_up():
    logging.info("Starting the sign-up test...")
    driver = webdriver.Chrome()

    # Test data
    test_email = "testuser@gmail.com"
    test_username = "acceptance_tests"

    try:
        # Navigate to the home page
        driver.get("https://cs-386-event-pulse.onrender.com/")  
        logging.info("Navigated to the home page.")
        time.sleep(DELAY)

        # Handle dynamic navbar if minimized
        try:
            navbar_toggle = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "navbar-toggler"))
            )
            navbar_toggle.click()
            logging.info("Navbar was minimized. Clicked the toggle to expand it.")
            time.sleep(DELAY)
        except Exception as navbar_exception:
            logging.info("Navbar toggle not found. Assuming navbar is already expanded.")

        # Navigate to the Sign-Up page
        sign_up_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "signUp"))
        )
        sign_up_link.click()
        logging.info("Navigated to the Sign-Up page.")
        time.sleep(DELAY)

        # Fill out the sign-up form
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_field.send_keys(test_email)
        logging.info(f"Entered email: {test_email}")
        time.sleep(DELAY)

        username_field = driver.find_element(By.NAME, "username")
        username_field.send_keys(test_username)
        logging.info(f"Entered username: {test_username}")
        time.sleep(DELAY)

        first_name_field = driver.find_element(By.NAME, "firstName")
        first_name_field.send_keys("test")
        logging.info("Entered first name: test")
        time.sleep(DELAY)

        password_field = driver.find_element(By.NAME, "password1")
        password_field.send_keys("acceptancetest")
        logging.info("Entered password.")
        time.sleep(DELAY)

        password_confirm_field = driver.find_element(By.NAME, "password2")
        password_confirm_field.send_keys("acceptancetest")
        logging.info("Entered password confirmation.")
        time.sleep(DELAY)

        # Submit the form
        submit_button = driver.find_element(By.CLASS_NAME, "btn-primary.w-100")
        submit_button.click()
        logging.info("Clicked the submit button.")
        time.sleep(DELAY)

        # Print success message
        logging.info("Sign-up process completed successfully.")
        print("Sign-up test executed successfully!")

    except Exception as exception:
        logging.error("Test failed with an unexpected error: %s", exception)
        print("Test failed. Please check the logs for more details.")
    finally:
        driver.quit()
        logging.info("Browser closed and test completed.")

# Run the test
test_sign_up()
