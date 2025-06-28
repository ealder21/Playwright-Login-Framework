
import pytest
from playwright.sync_api import Page, expect
from PytestPlaywright_NewSetup.Pages.loginPage_page import LoginPage
from PytestPlaywright_NewSetup.Pages.landingPage_page import LandingPage
from PytestPlaywright_NewSetup.utils import fixed_data as fixed_data


# baseURL = fixed_data.baseURL
#
# def test_login(page: Page):
#     login_page = LoginPage(page) #Access LoginPage methods#Access LoginPage methods
#     page.goto(baseURL) #Navigate to webpage
#     login_page.enter_username(fixed_data.username) #Enter username, data coming from fixed_data file
#     login_page.enter_password(fixed_data.password) #Enter password, data coming from fixed_data file
#     login_page.click_login_button() #Click button
#     expect(login_page.verify_login_message).to_be_visible() # Verify successful login



# def test_login(page: Page):
#     page.goto(baseURL)
#     page.locator("id=uname").fill("test")
#     page.locator("id=pwd").fill("test")
#     page.get_by_role("button", name="Login").click()
#     expect(page.locator("text=Login Successful :)")).to_be_visible()


#Navigate to webpage and login
def test_login(log_into_site): #Uses fixture from conftest.py
    login = LoginPage(log_into_site)
    expect(login.verify_login_message).to_be_visible()


#Navigate to webpage
def test_navigate_to_webpage(navigate_to_webpage): #Uses fixture from conftest.py
    landing_page = LandingPage(navigate_to_webpage)
    expect(landing_page.verify_landingPage_message).to_be_visible()