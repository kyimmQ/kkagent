from playwright.sync_api import sync_playwright


from automation.playwright import WebAutomation

def main():
    kahoot_link = "https://kahoot.it/?pin=8747466&refer_method=link"
    # Initialize the WebAutomation class
    web_automation = WebAutomation()

    # Open a webpage
    web_automation.open_page("https://kahoot.it/?pin=8747466&refer_method=link")

    web_automation.page.wait_for_timeout(5000)  # Wait for 5 seconds

    # Perform other actions as needed...

if __name__ == "__main__":
    main()