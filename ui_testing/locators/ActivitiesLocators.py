from selenium.webdriver.common.by import By


class ActivitiesLocators:
    CLICK_TO_CREATE_ACTIVITY_BY_IC0N_BTN = By.XPATH, '/html/body/app-root/div/div[2]/app-agenda/div/p-button[1]/button'

    EDIT_ACTIVITY_BTN = By.XPATH, '/html/body/app-root/div/div[2]/app-activities/div/div/div[2]/p-card/div/div/div[2]/p-footer/button[1]'
    ADDING_NEW_ACTIVITY = By.XPATH,'/html/body/app-root/div/div[2]/app-activities/div/div/div[2]/p-card/div/div/div[' \
                                   '2]/p-footer/button[2]'