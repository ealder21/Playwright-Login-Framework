
from playwright.sync_api import Page


class LoginPage: #Name page class
    def __init__(self, page:Page): #Set up constructor, Makes use of the Pytest-Playwright built-in fixture
        self.page = page # Needed to use page fixtures

        self.username_textbox_byID = page.locator("id=uname") #Create page object
        self.password_textbox_byID = page.locator("id=pwd") #Create page object
        self.login_button_byRole= page.get_by_role("button", name="Login") #Create page object
        self.verify_login_message= page.locator("text=Login Successful :)") #Create page object


    def enter_username(self, username): #Name method
        self.username_textbox_byID.fill(username) #Create page method

    def enter_password(self, password): #Name method
        self.password_textbox_byID.fill(password) #Create page method

    def click_login_button(self): #Name method
        self.login_button_byRole.click() #Create page method


    #Optional, create a single login step
    def user_login(self, username, password): #Name method
        self.enter_username(username) #Create page method
        self.enter_password(password) #Create page method
        self.click_login_button() #Create page method

