from selenium import webdriver


def initialize_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    return driver



