from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def wait_for_element_presence(driver, by, locator, timeout=60):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, locator)))


def wait_for_element_visibility(driver, by, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)))


def wait_for_element_clickable(driver, by, locator, timeout=10):
    """
    Wait for the element to be clickable on the page.
    """
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, locator)))


def wait_for_elements(driver, locator, timeout=10):
    try:
        elements = WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return elements
    except TimeoutException:
        return []
