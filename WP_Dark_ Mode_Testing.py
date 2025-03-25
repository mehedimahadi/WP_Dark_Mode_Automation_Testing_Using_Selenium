import os

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv

#load the environment variable
load_dotenv()
U_name = os.getenv("name")
password = os.getenv("Password")



def Site_Animation(driver):
    click_Site_Animation = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                 "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div[2]/a[5]")))
    # Click on the switch to toggle it ON or OFF
    click_Site_Animation.click()
    time.sleep(1)  # Adding a short delay

    Enable_Page_Transition_Animation = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                 "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[3]/div/div/div[1]/div/div/div/label/div[1]/div")))
    # Click on the switch to toggle it ON or OFF
    Enable_Page_Transition_Animation.click()
    time.sleep(1)  # Adding a short delay

    Select_Animation = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                                   "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div[4]/span[2]")))
    # Click on the switch to toggle it ON or OFF
    Select_Animation.click()
    time.sleep(1)  # Adding a short delay



    save_Accessibility_Settings = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[4]/button[2]")))
    # Click on the switch to toggle it ON or OFF
    save_Accessibility_Settings.click()
    time.sleep(5)  # Adding a short delay

def Accessibility_Settings(driver):
    switch_Accessibility = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                 "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[3]/div/section/div[2]/div/div[3]/div/div[2]/div[3]/a")))
    # Click on the switch to toggle it ON or OFF
    switch_Accessibility.click()
    time.sleep(1)  # Adding a short delay

    Disable_Keyboard_Shortcut = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                 "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[3]/div/div[6]/div[1]/label/div[1]/div")))
    # Click on the switch to toggle it ON or OFF
    Disable_Keyboard_Shortcut.click()
    time.sleep(1)  # Adding a short delay



    save_Accessibility_Settings = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[4]/button[2]")))
    # Click on the switch to toggle it ON or OFF
    save_Accessibility_Settings.click()
    time.sleep(5)  # Adding a short delay


def switch_position(driver):
    switch_position = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                 "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[3]/div/section/div[2]/div/div[2]/div[4]/div/div[1]/div[2]/div[2]/div[1]")))
    # Click on the switch to toggle it ON or OFF
    switch_position.click()
    time.sleep(1)  # Adding a short delay



    save_switch_position = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[4]/button[2]")))
    # Click on the switch to toggle it ON or OFF
    save_switch_position.click()
    time.sleep(10)  # Adding a short delay

def select_Custom_Switch_size(driver):
    Floating_Switch_Size = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                 "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[3]/div/section/div[2]/div/div[2]/div[4]/div/div[1]/div[1]/div[2]/div[6]/span")))
    # Click on the switch to toggle it ON or OFF
    Floating_Switch_Size.click()
    time.sleep(1)  # Adding a short delay

    input_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                 "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[3]/div/section/div[2]/div/div[2]/div[4]/div/div[1]/div[1]/div[3]/div[2]/div/div[2]/input")))

    # Clear the input field in case there is any existing value
    input_field.clear()

    # Input the number "220" into the input field
    input_field.send_keys("220")

    # Wait for a few seconds to see the result
    time.sleep(5)

    time.sleep(10)  # Adding a short delay

    save_select_Custom_Switch_size = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[4]/button[2]")))
    # Click on the switch to toggle it ON or OFF
    save_select_Custom_Switch_size.click()
    time.sleep(10)  # Adding a short delay

def customize_Floating_Switch_Style(driver):
    driver.get("https://demo.wppool.dev/wp-dark-mode-146a2b3kgnlew08/wp-admin/admin.php?page=wp-dark-mode#/frontend")
    customization_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                 "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div/h4")))
    # Click on the switch to toggle it ON or OFF
    customization_element.click()
    time.sleep(1)  # Adding a short delay

    switch_setting = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div[2]/a[1]")))
    # Click on the switch to toggle it ON or OFF
    switch_setting.click()
    time.sleep(1)  # Adding a short delay

    select_Floating_Switch_Style = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[3]/div/section/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[4]")))
    # Click on the switch to toggle it ON or OFF
    select_Floating_Switch_Style.click()
    time.sleep(1)  # Adding a short delay

    save_Floating_Switch_Style = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[4]/button[2]")))
    # Click on the switch to toggle it ON or OFF
    save_Floating_Switch_Style.click()
    time.sleep(10)  # Adding a short delay


def test_dark_mode(driver):
    # Open the webpage
    driver.get("https://demo.wppool.dev/wp-dark-mode-678dq2bnr09k1mf/wp-admin/")

    # Check if Dark Mode toggle button exists
    dark_mode_toggle = driver.find_elements(By.CLASS_NAME, "dark-mode-toggle")
    if dark_mode_toggle:
        # Toggle Dark Mode
        dark_mode_toggle.click()

        # Wait for the page to reload or for elements to change
        time.sleep(2)

        # Verify changes in element styles or behavior indicating Dark Mode
        # For example, you could check the background color of the body element
        body_background_color = driver.find_element(By.TAG_NAME, "body").value_of_css_property("background-color")
        if body_background_color == "rgb(0, 0, 0)":  # Check for dark background color
            print("Dark Mode is working.")
        else:
            print("Dark Mode is not working.")
    else:
        print("Dark Mode toggle button not found.")

def navigate_to_admin_panel_dark_mode(driver):
    # try:
    #     # Navigate to the WP Dark Mode plugin page
    #     driver.get("https://wordpress.org/plugins/wp-dark-mode/")
    #
    #     # Find the plugin title element
    #     plugin_title_element = driver.find_element(By.CSS_SELECTOR,
    #                                                ".wporg-local-navigation-bar__fade-in-scroll.wp-block-post-title.has-small-font-size.has-inter-font-family")
    #
    #     # Check if the plugin title element exists
    #     if plugin_title_element:
    #         print("WP Dark Mode Plugin is Active.")
    #     else:
    #         print("Should Install the Plugin and Activate it.")
    #
    # except Exception as e:
    #     print("Error occurred:", e)

    # Go to Admin Panel Dark Mode
    try:

        WP_Dark_Mode = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                            "/html/body/div[1]/div[1]/div[2]/ul/li[7]/a/div[3]")))

        # Click on the Admin Panel Dark Mode switch
        WP_Dark_Mode.click()

        time.sleep(5)  # Adding a short delay

        # Wait for the Admin Panel Dark Mode switch to be clickable
        admin_panel_dark_mode = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                            "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/a[2]")))

        # Click on the Admin Panel Dark Mode switch
        admin_panel_dark_mode.click()

        time.sleep(5)  # Adding a short delay

        print("Admin Panel Dark Mode enabled successfully.")

    except Exception as e:
        print("An error occurred while enabling Admin Panel Dark Mode:", e)

    try:
        # Wait for the switch element to be clickable
        switch_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                     "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[3]/section/div[1]/div[1]/label/div[1]/div")))
        # Click on the switch to toggle it ON or OFF
        switch_element.click()
        time.sleep(1)  # Adding a short delay

        # Save the changes
        save_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[4]/button[2]")))
        save_element.click()
        time.sleep(1)  # Adding a short delay

        # Click on the dark mode element
        dark_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/ul[1]/li[5]/div/div/div/span[2]")))
        dark_element.click()
        time.sleep(10)
        print("Clicked on dark mode successfully.")

    except Exception as e:
        print("Error:", e)


# Function to log in to WordPress site
def login_to_wordpress(username, password):
    # Initialize the WebDriver (assuming Chrome WebDriver is used)
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open the WordPress login page
    driver.get("https://demo.wppool.dev/wp-dark-mode-678dq2bnr09k1mf/wp-admin/")

    # Find the username and password fields, and the login button
    username_field = driver.find_element(By.ID, "user_login")
    password_field = driver.find_element(By.ID, "user_pass")
    login_button = driver.find_element(By.ID, "wp-submit")

    # Enter the username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Click on the login button
    login_button.click()

    # Add a short delay to allow time for the login process to complete
    time.sleep(10)

    # Verify if login is successful
    if "Dashboard" in driver.title:
        print("Login successful!")
        # Navigate to Admin Panel Dark Mode
        navigate_to_admin_panel_dark_mode(driver)

        customize_Floating_Switch_Style(driver)
        select_Custom_Switch_size(driver)
        switch_position(driver)
        Accessibility_Settings(driver)
        Site_Animation(driver)
        test_dark_mode(driver)
    else:
        print("Login failed!")

    # Close the WebDriver
    driver.quit()




# Test the login functionality
if __name__ == "__main__":
    # Give the username in the .env file
    login_to_wordpress(U_name, password)

