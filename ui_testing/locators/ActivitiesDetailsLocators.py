from selenium.webdriver.common.by import By


class ActivitiesDetails:
    TASK_NAME = By.XPATH, '//*[@id="name"]'
    WHY_I_DO_THIS = By.ID, 'description'
    HOUR_FIELD = By.XPATH, '//*[@id="time"]/span/input'
    HOUR_ARROW_UP = By.XPATH, '//*[@id="time"]/span/div/div/div[1]/button[1]'
    HOUR_ARROW_DOWN = By.XPATH, '//*[@id="time"]/span/div/div/div[1]/button[2]'
    MIN_ARROW_UP = By.XPATH, '//*[@id="time"]/span/div/div/div[3]/button[1]'
    MIN_ARROW_DOWN = By.XPATH, '//*[@id="time"]/span/div/div/div[3]/button[2]'
    WHICH_DAYS_FIELD = By.XPATH, '//*[@id="time"]/span/div/div/div[3]/button[2]'
    SPECIFIC_DAY_SEARCH = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/app-input-combobox-field' \
                                    '/div/p-multiselect/div/p-overlay/div/div/div/div[1]/div[2]/input'
    CONFIRM_BUTTON = By.XPATH,'/html/body/app-root/div/div[2]/app-activities-details/div/p-button/button'
