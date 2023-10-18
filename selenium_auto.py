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
    driver.implicitly_wait(0.5) # Introduces wait time of up to 0.5 seconds when attempting to find elements
    text_box = driver.find_element(by=By.NAME, value="my-text") # Finds an element by name attribute
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button") # Navigates the webpage using a CSS selector to find a button and performs a click action
    text_box.send_keys("Selenium") # Enables typing the text "Selenium" in a text box
    submit_button.click() # Stimulates clicking the submit button
    message = driver.find_element(by=By.ID, value="message") # Locates an element by the "ID" attribute and assigns it to variable "message"
    value = message.text # Retrieves the text content of that element using "message.text" and assigns it to the variable "value"
    assert value == "Received!" # Asserts that the text content is received

    # Closes Chrome
    # driver.quit() # Closes browser tab
    driver.close() # Closes the browser tab


test_eight_components() # A function call to run the test components
