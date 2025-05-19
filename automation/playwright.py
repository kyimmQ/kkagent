from playwright.sync_api import sync_playwright

class WebAutomation:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
    
    def open_page(self, url: str):
        self.page.goto(url)

    def end(self):
        self.page.close()
        self.browser.close()
        self.playwright.stop()

class KahootAutomation(WebAutomation):
    def __init__(self, kahoot_link: str):
        super().__init__()
        self.kahoot_link = kahoot_link
    
    def open_kahoot(self):
        self.open_page(self.kahoot_link)

    def fill_name(self, name: str):
        self.page.fill("input[name='nickname']", name)
        self.page.click("button[type='submit']")

    def wait_for_question(self):
            