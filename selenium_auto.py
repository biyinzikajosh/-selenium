from selenium import webdriver # For importing the webdriver module from Selenium
from selenium.webdriver.common.by import By # Helps in locating elements on a webpage
from selenium.webdriver.chrome.options import Options # Allows you to configure setting and preferences for the Chrome Webdriver

# Deprecated - no longer needed
chrome_driver_path = "/Users/philippmuellauer/Development/chromedriver" # Setting the path to the Chrome webdriver

# keeps chrome open
chrome_options = webdriver.ChromeOptions() # Creates an instance or object from ChromeOptions class. This helps in configuring the Chrome WebDriver
chrome_options.add_experimental_option("detach", True) # Enables continous interaction with the browser even after the script has ended

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver = webdriver.Chrome() # Creating a Chrome WebDriver instance
driver = webdriver.Chrome(options=chrome_options) # Allows you to pass custom configurations and settings for the Chrome WebDriver

def test_eight_components(): # Defining the test_eight_components() function
    driver.get("https://www.selenium.dev/selenium/web/web-form.html") # Opens the URL in the browser
    title = driver.title # Retrieves the page title
    assert title == "Web form" # Asserts that the page title is a Web form
    driver.implicitly_wait(0.5)
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    text_box.send_keys("Selenium")
    submit_button.click()
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    # Closes Chrome
    # driver.quit()
    driver.close()


test_eight_components()
