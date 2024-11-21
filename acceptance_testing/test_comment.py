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
DELAY = 2  

def test_make_comment(email, password, post_title, comment_text):
    
    logging.info("Starting the comment test...")
    driver = webdriver.Chrome()

    try:
        # Log in
        driver.get("https://cs-386-event-pulse.onrender.com/")
        logging.info("Navigated to the login page.")
        time.sleep(DELAY)

        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        password_field = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.CLASS_NAME, "btn-primary")

        email_field.send_keys(email)
        password_field.send_keys(password)
        login_button.click()
        logging.info("Entered credentials and logged in.")
        time.sleep(DELAY)

        # Handle navbar toggle if minimized
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
        logging.info("Navigated to the search page.")
        time.sleep(DELAY)

        # Search for the post
        search_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "query"))
        )
        search_bar.clear()
        search_bar.send_keys(post_title)
        logging.info(f"Entered search keyword: {post_title}")
        time.sleep(DELAY)

        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
        )
        search_button.click()
        logging.info("Clicked the 'Search' button.")
        time.sleep(DELAY)

        # Click on the post title
        post_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, post_title))
        )
        post_link.click()
        logging.info(f"Clicked on the post: {post_title}")
        time.sleep(DELAY)

        # Add a comment
        comment_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "content"))
        )
        comment_box.clear()
        comment_box.send_keys(comment_text)
        logging.info(f"Entered comment: {comment_text}")
        time.sleep(DELAY)

        submit_comment_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary.mt-2"))
        )
        submit_comment_button.click()
        logging.info("Clicked the 'Post Comment' button.")
        time.sleep(DELAY)

        # Verify success message
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))
        )
        assert "Comment added successfully!" in success_message.text, "Success message not displayed."
        logging.info("Success message displayed: Comment added successfully!")

        # Verify comment in comments section
        comments_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "list-group"))
        )
        assert comment_text in comments_section.text, "Comment not found in the comments section."
        logging.info("Comment posted successfully!")

        print("Comment test executed successfully!")

    except Exception as general_exception:
        logging.error("Test failed with an unexpected error: %s", general_exception)
        print("Test failed. Please check the logs for more details.")
        print("Current page source:\n", driver.page_source)
    finally:
        try:
            time.sleep(2)  # Allow browser to settle before quitting
            driver.quit()
            logging.info("Browser closed and test completed.")
        except Exception as cleanup_error:
            logging.error("Failed to close the browser properly: %s", cleanup_error)

# Run the test
test_make_comment("testuser@gmail.com", "acceptancetest", "test event", "test comment")
