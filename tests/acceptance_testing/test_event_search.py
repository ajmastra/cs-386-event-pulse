import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constant for delay
     # Change if needed
DELAY = 1 

def test_event_search(email, password, search_keyword):
    logging.info("Starting the event search test...")
    driver = webdriver.Chrome()

    try:
        # Log in
        driver.get("https://cs-386-event-pulse.onrender.com/")
        logging.info("Navigated to the login page.")
        time.sleep(DELAY)

        # Wait for the email and password fields
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        password_field = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.CLASS_NAME, "btn-primary")

        # Enter credentials and log in
        email_field.send_keys(email)
        password_field.send_keys(password)
        login_button.click()
        logging.info("Entered credentials and logged in.")
        time.sleep(DELAY)

        # Check if the navbar is minimized and expand it if needed
        try:
            navbar_toggle = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "navbar-toggler"))
            )
            navbar_toggle.click()
            logging.info("Navbar was minimized. Clicked the toggle to expand it.")
            time.sleep(DELAY)
        except Exception:
            logging.info("Navbar toggle not found. Assuming navbar is already expanded.")

        # Navigate to the search page
        search_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "search"))
        )
        search_link.click()
        logging.info("Clicked the 'Search' link and navigated to the search page.")
        time.sleep(DELAY)

        # Interact with the search bar
        search_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "query"))
        )
        search_bar.clear()
        search_bar.send_keys(search_keyword)
        logging.info(f"Entered search keyword: {search_keyword}")
        time.sleep(DELAY)

        # Click the Search button
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
        )
        search_button.click()
        logging.info("Clicked the 'Search' button to confirm the search.")
        time.sleep(DELAY)

        # Verify search results presence
        search_results = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, search_keyword))
        )
        assert search_results is not None, f"No results found for the keyword: {search_keyword}"
        logging.info(f"Search results found for the keyword: {search_keyword}")

        # Print success
        print("Search test executed successfully!")

    except Exception as general_exception:
        logging.error("Test failed with an unexpected error: %s", general_exception)
        print("Test failed. Please check the logs for more details.")
    finally:
        driver.quit()
        logging.info("Browser closed and test completed.")

# Run the test
test_event_search("testuser@gmail.com", "acceptancetest", "test event")
