
import pytest
from playwright.sync_api import Page, expect
from PytestPlaywright_NewSetup.Pages.loginPage_page import LoginPage
from PytestPlaywright_NewSetup.utils import fixed_data as fixed_data


baseURL = fixed_data.baseURL

# Navigate to webpage and login
@pytest.fixture() #Add pytest fixture
def log_into_site(page): #Name fixture
    login_page = LoginPage(page) #Access LoginPage methods#Access LoginPage methods
    page.goto(baseURL) #Navigate to webpage
    login_page.enter_username(fixed_data.username) #Enter username, data coming from fixed_data file
    login_page.enter_password(fixed_data.password) #Enter password, data coming from fixed_data file
    login_page.click_login_button() #Click button
    return page


#expect(login_page.verify_login_message).to_be_visible() # Verify successful login

# Navigate to the webpage
@pytest.fixture() #Add fixture
def navigate_to_webpage(page): #Name fixture
    page.goto(baseURL) #Navigate to browser
    return page