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
        self.page.set_default_timeout(0)
        self.kahoot_link = kahoot_link
    
    def open_kahoot(self):
        self.open_page(self.kahoot_link)

    def fill_name(self, name: str):
        self.page.fill("input[name='nickname']", name)
        self.page.click("button[type='submit']")

    def wait_for_question(self):
        pass
    
    def get_question(self):
        # wait until the question title is in the DOM
        self.page.wait_for_selector('[class^="extensive-question-title__Title"]')

        # locate it
        question_locator = self.page.locator('[class^="extensive-question-title__Title"]')

        # grab its visible text
        question_text = question_locator.text_content()

        return question_text

    def get_choices(self):
        choices_container = self.page.locator('[class^="quiz-choices__Container"]')
        buttons = choices_container.locator('button[data-functional-selector]')
        options = []
        count = buttons.count()
        for i in range(count):
            choice = buttons.nth(i)
            choice_text_div = choice.locator('[data-functional-selector^="question-choice-text-"]')
            options.append(choice_text_div.text_content())
        return options

    def get_media(self):
        # 1) Locate the media container for the current question
        media_container = self.page.locator('[data-functional-selector="media-container"]')

        # 2) Is it empty? (`<div … data-functional-selector="media-container"></div>`)
        if not media_container.locator("img").count():
            return None

        # 3) Grab the first <img> inside it and return its src
        src = media_container.locator("img").first.get_attribute("src")
        return src

    def wait_for_sent_page(self):
        self.page.wait_for_selector(selector='main[class^="sent"]')

    def choose(self, option: int):
        # Choices container
        choices_container = self.page.locator('[class^="quiz-choices__Container"]')
        buttons = choices_container.locator('button[data-functional-selector]')
        buttons.nth(option).click()


    def mock_choose_answer(self, question, options, media_url) -> int:
        """Return a random choice index between 0 and 3 inclusive."""
        print("‣ Question:", question)
        print("‣ Options :", options)
        print("‣ Media   :", media_url or "None")
        print("-" * 40)
        import random
        return random.randint(0, 3)