from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element_presence(driver, by, locator, timeout=60):
    """
    Wait for the element to be present in the DOM of the page.
    """
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, locator)))


def wait_for_element_visibility(driver, by, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)))


def wait_for_element_clickable(driver, by, locator, timeout=10):
    """
    Wait for the element to be clickable on the page.
    """
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, locator)))