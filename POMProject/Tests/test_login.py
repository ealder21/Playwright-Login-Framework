
from playwright.sync_api import Playwright, Page, expect
import pytest
from POMProject.Pages.loginPage_page import LoginPage #import POM page class
from POMProject.Utils import fixed_data as fixed_data

"""Test case 1: Login into the try testing this site""" #Test case


#4: Create test case
def test_valid_login(page:Page):
    login_page = LoginPage(page) #Access LoginPage methods
    login_page.enter_username(fixed_data.username) #Enter username, data coming from fixed_data file
    login_page.enter_password(fixed_data.password) #Enter password, data coming from fixed_data file
    login_page.click_login_button() #Click button
    expect(login_page.verify_login_message).to_be_visible()  # Verify successful login

    # page.locator("id=uname").fill("test") #Enter username
    # page.locator("id=pwd").fill("test") #Enter password
    # page.get_by_role("button",name="Login").click() # Click button










