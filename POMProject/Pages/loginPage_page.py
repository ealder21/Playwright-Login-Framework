
from playwright.sync_api import Page, Playwright, expect

class LoginPage:
    def __init__(self, page:Page):
        self.page = page

        self.username_textbox_byID = page.locator("id=uname")
        self.password_textbox_byID = page.locator("id=pwd")
        self.login_button_byRole = page.get_by_role("button",name="Login")
        self.verify_login_message = page.locator("text=Login Successful :)")

    def enter_username(self, username):
        self.username_textbox_byID.fill(username) #Enter username

    def enter_password(self, password):
        self.password_textbox_byID.fill(password) #Enter password

    def click_login_button(self):
        self.login_button_byRole.click() # Click button

    def user_login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
