from selenium import webdriver # For importing the webdriver module from Selenium
from selenium.webdriver.common.by import By # Helps in locating elements on a webpage
from selenium.webdriver.chrome.options import Options # Allows you to configure setting and preferences for the Chrome Webdriver

# Deprecated - no longer needed
chrome_driver_path = "/Users/philippmuellauer/Development/chromedriver" # Setting the path to the Chrome webdriver

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)

def test_eight_components():
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    title = driver.title
    assert title == "Web form"
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
