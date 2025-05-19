from playwright.sync_api import sync_playwright


from automation.playwright import KahootAutomation

def main():
    kahoot_link = "https://kahoot.it/?pin=547962&refer_method=link"
    # Initialize the WebAutomation class
    web_automation = KahootAutomation(kahoot_link)

    # Open a webpage
    web_automation.open_kahoot()

    web_automation.fill_name("KKAgent")
    while(True):
        question = web_automation.get_question()
        choices = web_automation.get_choices()
        media_url = web_automation.get_media()

        # process question
        choice = web_automation.mock_choose_answer(question=question, options=choices, media_url=media_url)
        # choose answer
        web_automation.choose(choice)

        # wait for next page
        web_automation.wait_for_sent_page()

    # Perform other actions as needed...

if __name__ == "__main__":
    main()