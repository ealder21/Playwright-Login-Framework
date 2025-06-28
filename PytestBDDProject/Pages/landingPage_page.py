
from playwright.sync_api import Page, expect, Playwright


class LandingPage:
    def __init__(self, page:Page):
        self.page = page

        self.verify_landingPage_message = page.locator("text=Your Website to practice Automation Testing")