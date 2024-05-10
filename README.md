# WP_Dark_Mode_Automation_Testing_Using_Selenium

This test suite automates the testing of various features of the WordPress Dark Mode plugin. It performs the following tasks:

1. Give the username and password to log in to the WordPress site by automation.
2. First part of the navigate_to_admin_panel_dark_mode() function check whether the WordPress Dark Mode plugin is active but for the some error problem it might be comment out.
3. Next part of the navigate_to_admin_panel_dark_mode() function enable admin dashboard dark mode.
4. In the customize_Floating_Switch_Style() function do the Customize Floating Switch Style.
5. select_Custom_Switch_size() function works for select the custom switch size.
6. switch_position() function do the change floating switch position.
7. Disable Keyboard Shortcut from Accessibility Settings works in the function of Accessibility_Settings().
8. Enable Page Transition Animation and Change Animation Effect in the Site_Animation() function.
9. test_dark_mode() function check the Validate Dark Mode functionality on the frontend.

## Requirements

To run this test suite, ensure you have the following installed:

- Python 3.x
- Selenium WebDriver for Python
- Chrome WebDriver
- dotenv Python package

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/mehedimahadi/WP_Dark_Mode_Automation_Testing_Using_Selenium

2. Change and give your username and password.
  _name=your_username
  Password=your_password
