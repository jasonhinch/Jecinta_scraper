from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def scrape_trial_information():

    # Set up Chrome options
    options = Options()
    options.headless = False  # Ensure headless is False to see the browser in action

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Navigate to the URL
    driver.get("https://sanctr.samrc.ac.za/TrialDisplay.aspx?TrialID=10607")

    # Find the element using the given XPath and get its text
    element = driver.find_element(By.XPATH, '//*[@id="trialInformation"]/div[1]/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]').text

    # Print the text of the element
    print(element)

    # Just a small delay so you can see the browser open
    time.sleep(3)

    # Quit the driver
    driver.quit()


if __name__ == "__main__":
    scrape_trial_information()
