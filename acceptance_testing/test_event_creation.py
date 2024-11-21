import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constant delay 
    # Change if needed
DELAY = 1

def test_event_creation(email, password):
    logging.info("Starting the event creation test...")
    driver = webdriver.Chrome()
    time.sleep(DELAY)

    try:
        # Log in
        driver.get("https://cs-386-event-pulse.onrender.com/login")
        logging.info("Navigated to the login page.")

        # Wait for the email and password fields
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        password_field = driver.find_element(By.NAME, "password")
        time.sleep(DELAY)
        login_button = driver.find_element(By.CLASS_NAME, "btn-primary")

        # Enter credentials and log in
        email_field.send_keys(email)
        password_field.send_keys(password)
        login_button.click()
        time.sleep(DELAY)
        logging.info("Entered credentials and logged in.")

        # Navigate to Add Event page
        add_event_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Add Event"))
        )
        add_event_button.click()
        time.sleep(DELAY)
        logging.info("Navigated to the Add Event page.")

        # Fill out the event form
        # Enter the event title
        event_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "eventTitle"))
        )
        event_title.send_keys("test event")
        time.sleep(DELAY)
        logging.info("Entered event title: test event")

        # Enter the event date
        event_date = driver.find_element(By.ID, "eventDate")
        event_date.send_keys("11/27/2024")
        time.sleep(DELAY)
        logging.info("Entered event date: 11/27/2024")

        # Enter the event time
        event_time = driver.find_element(By.ID, "eventTime")
        event_time.send_keys("3:23P")
        time.sleep(DELAY)
        logging.info("Entered event time: 3:23 PM")

        # Enter the event location
        event_location = driver.find_element(By.ID, "eventLocation")
        event_location.send_keys("test location")
        time.sleep(DELAY)
        logging.info("Entered event location: test location")

        # Enter the event description
        event_description = driver.find_element(By.ID, "eventDescription")
        event_description.send_keys("testing event")
        time.sleep(DELAY)
        logging.info("Entered event description: testing event")

        # Select event type
        event_type_dropdown = Select(driver.find_element(By.ID, "eventType"))
        event_type_dropdown.select_by_value("community-event")
        time.sleep(DELAY)
        logging.info("Selected event type: Community Event")

        # Submit the form
        add_event_button = driver.find_element(By.CLASS_NAME, "btn-primary.btn-lg.px-5")
        add_event_button.click()
        time.sleep(DELAY)
        logging.info("Submitted the event creation form.")

        # Verify success message
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))
        ).text
        assert "Event added successfully!" in success_message, "Event creation failed."
        time.sleep(DELAY)
        logging.info("Event created successfully!")
    # Exception for when tests fail vice versa
    except Exception as exception:
        logging.error("Test failed with an unexpected error: %s", exception)
        print("Current page source:\n", driver.page_source)
    finally:
        driver.quit()
        time.sleep(DELAY)
        logging.info("Browser closed and test completed.")

# Run the test
test_event_creation("testuser@gmail.com", "acceptancetest")
