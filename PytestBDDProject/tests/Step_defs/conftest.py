
from playwright.sync_api import Page, expect, Playwright
from pytest_bdd import given, when, then, parsers, scenarios, scenario
from PytestBDDProject.utilis import fixed_data as fixed_data
from PytestBDDProject.Pages.loginPage_page import LoginPage
import pytest

baseURL = fixed_data.baseURL #Set up baseURL

# Navigate and login
@pytest.fixture() #Add pytest fixture
def log_in_to_website(page:Page): #Name function and pass the Playwright page fixture
    page.set_viewport_size({"width": 1420, "height": 800}) #Set viewport size
    login_page = LoginPage(page) #Access LoginPage methods#Access LoginPage methods
    page.goto(baseURL) #Navigate to browser
    login_page.enter_username(fixed_data.username) #Enter username, data coming from fixed_data file
    login_page.enter_password(fixed_data.password) #Enter password, data coming from fixed_data file
    login_page.click_login_button() #Click button
    return page




# Navigate to webpage
@pytest.fixture() #Add pytest fixture
def navigate_to_webpage(page:Page): #Name function and pass the Playwright page fixture
    page.set_viewport_size({"width": 1280, "height": 720}) #Set viewport size
    page.goto(baseURL) #Navigate to the webpage
    return page



