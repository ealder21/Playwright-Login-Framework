
from playwright.sync_api import Page, expect, Playwright
from pytest_bdd import given, when, then, parsers, scenarios, scenario
from PytestBDDProject.Pages.loginPage_page import LoginPage #Import page class
from PytestBDDProject.Pages.landingPage_page import LandingPage #Import page class
from PytestBDDProject.utilis import fixed_data as fixed_data


scenarios('../Features/login.feature') #Link feature file to test file


@given("The user has launched the browser and is on the login page") #Given step from feature file
def navigate_to_the_webpage(navigate_to_webpage): # Fixture from conftest.py
    landing_page = LandingPage(navigate_to_webpage)
    expect(landing_page.verify_landingPage_message).to_be_visible()

#def navigate_to_webpage(page:Page):#Function name. Makes use of the Pytest-Playwright built-in fixture
    #page.goto(baseURL)# Code to open browser and navigate to webpage


@when(parsers.parse("The users enters a valid username")) #When step from feature file
def enter_a_username(page:Page): #Function name. Makes use of the Pytest-Playwright built-in fixture
    login_page = LoginPage(page)
    login_page.enter_username(fixed_data.username)

    #page.locator("id=uname").fill("test") #Code to perform action


@when(parsers.parse("The user enters a valid password")) #When step from feature file
def enter_a_password(page:Page): #Function name. Makes use of the Pytest-Playwright built-in fixture
    login_page = LoginPage(page)
    login_page.enter_password(fixed_data.password)

    #page.locator("id=pwd").fill("test") #Code to perform action


@when("The user clicks on the login button") #When step from feature file
def click_the_login_button(page:Page):#Function name. Makes use of the Pytest-Playwright built-in fixture
    login_page = LoginPage(page)
    login_page.click_login_button()

    #page.get_by_role("button", name="Login").click() #Code to perform action


@then("The user should be logged in and be on the successful login screen") #Then step from feature file
def verify_login(page:Page):#Function name. Makes use of the Pytest-Playwright built-in fixture
    login_page = LoginPage(page)
    expect(login_page.verify_login_message).to_be_visible() #Code to perform action



#----------------------------------------------------------------------------------------------------------------
#Example of using the login fixture
#
# @given("The user has launched the browser and is on the login page") #Given step from feature file
# def login_to_site(log_in_to_website): #Login fixture from conftest.py file
#     login_page = LoginPage(log_in_to_website) #Use fixture in test
#     expect(login_page.verify_login_message).to_be_visible() #Code to perform action