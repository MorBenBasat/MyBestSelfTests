from selenium.webdriver.common.by import By


class ActivitiesDetailsLocators:
    MY_MISSION = By.ID, 'name'
    WHY_I_DO_THIS = By.ID, 'description'
    TIME_FIELD = By.XPATH, '//*[@id="time"]/span/input'
    HOUR_ARROW_UP = By.XPATH, '//*[@id="time"]/span/div/div/div[1]/button[1]'
    HOUR_ARROW_DOWN = By.XPATH, '//*[@id="time"]/span/div/div/div[1]/button[2]'
    MIN_ARROW_UP = By.XPATH, '//*[@id="time"]/span/div/div/div[3]/button[1]'
    MIN_ARROW_DOWN = By.XPATH, '//*[@id="time"]/span/div/div/div[3]/button[2]'
    DAYS_FIELD = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/app-input-combobox-field/div/p' \
                           '-multiselect/div/div[2]/div'
    SUNDAY_BTN = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/app-input-combobox-field/div/p' \
                           '-multiselect/div/p-overlay/div/div/div/div[2]/ul/p-multiselectitem[1]/li'
    MONDAY_BTN = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/app-input-combobox-field/div/p' \
                           '-multiselect/div/p-overlay/div/div/div/div[2]/ul/p-multiselectitem[2]/li'

    CONFIRM_BTN = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/p-button/button'
    GREEN_ALERT = By.XPATH, '/html/body/app-root/div/p-toast/div/p-toastitem/div/div'
    RED_ALERT = None
