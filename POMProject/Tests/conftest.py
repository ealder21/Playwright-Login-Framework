
from playwright.sync_api import Playwright, Page, expect, sync_playwright
import pytest
from POMProject.Utils import fixed_data as fixed_data


#1: Store Url inside a variable
baseURL = fixed_data.baseURL #BaseURL coming from fixed_data file


#2: Setup browser
@pytest.fixture(scope="session") #Test scope
def browser(): #Create browser with keyword browser, pass playwright method
    with sync_playwright() as playwright: #Best practice to manage browser resources
        browser = playwright.chromium.launch(headless=False, slow_mo=500) # Launch browser

        yield browser #Tear down, runs after test is complete
        browser.close() #Close browser


#3: Navigate to the web page
@pytest.fixture() #Add pytest fixture
def page(browser): #Pass browser fixture into the page method
    context = browser.new_context() #Create a new browser context, basically open a new browser
    page =context.new_page() #Create and open a new page
    page.goto(baseURL) #Navigate to specified URL link

    yield page #Tear down, runs after test completes
    context.close() #Close browser context