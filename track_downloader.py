from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os

# Global variable to hold the driver instance
driver = None

def download_track(url):
    global driver  # Declare 'driver' as global to modify it

    # Only initialize the driver if it has not been done before
    if driver is None:
        # Path to your Chrome user data
        chrome_profile_path = "C:/Users/ethan/AppData/Local/Google/Chrome/User Data"

        # Check if the path exists
        if not os.path.exists(chrome_profile_path):
            print("Chrome profile path does not exist:", chrome_profile_path)
            exit(1)

        # Set up Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir=C:/Users/ethan/AppData/Local/Google/Chrome/User Data/Profile 2")
        chrome_options.add_argument("profile-directory=Profile 2")  # Use 'Profile 2'
        chrome_options.add_argument("--remote-debugging-port=9222")

        chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"

        # Start the Chrome browser
        print("Starting Chrome...")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("Chrome started successfully.")
        blocker = input("Install extension and set download path \n Press enter to continue... \n")

    try:
        # Navigate to the website
        print("Navigating to the website...")
        driver.get(url)
        sleep(2)  # Wait for the page to load

        # Locate the button and click it
        print("Clicking the button...")
        download_button = driver.find_element(By.ID, "newDownloadProcess")
        download_button.click()
        sleep(2)

        # Add additional code here if needed

    except Exception as e:
        print(f"An error occurred: {e}")
