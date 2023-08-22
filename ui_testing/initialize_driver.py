from selenium import webdriver


def initialize_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Uncomment this line to run in headless mode

    driver = webdriver.Chrome(options=options, executable_path='c:\chromedriver.exe')
    return driver
