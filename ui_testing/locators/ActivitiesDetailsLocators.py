from selenium.webdriver.common.by import By


class ActivitiesDetailsLocators:
    MY_ACTIVITY = By.XPATH, '//*[@id="activityName"]'
    WHY_I_DO_THIS = By.XPATH, '//*[@id="activityDescription"]'
    TIME_FIELD = By.XPATH, '//*[@id="activityTime"]/span/input'
    HOUR_ARROW_UP = By.XPATH, '//*[@id="time"]/span/div/div/div[1]/button[1]'
    HOUR_ARROW_DOWN = By.XPATH, '//*[@id="time"]/span/div/div/div[1]/button[2]'
    MIN_ARROW_UP = By.XPATH, '//*[@id="time"]/span/div/div/div[3]/button[1]'
    MIN_ARROW_DOWN = By.XPATH, '//*[@id="time"]/span/div/div/div[3]/button[2]'
    DAYS_FIELD = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/app-form/form/app-input' \
                           '-wrapper[4]/app-input-combobox-field/div/p-multiselect/div/div[2]/div'

    DAYS_SEARCH_FIELD = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/app-form/form/app-input' \
                                  '-wrapper[4]/app-input-combobox-field/div/p-multiselect/div/p-overlay/div/div/div' \
                                  '/div[1]/div[2]/input'
    SUNDAY_BTN = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/app-form/form/app-input' \
                           '-wrapper[4]/app-input-combobox-field/div/p-multiselect/div/p-overlay/div/div/div/div[' \
                           '2]/ul/p-multiselectitem/li'
    MONDAY_BTN = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/app-input-combobox-field/div/p' \
                           '-multiselect/div/p-overlay/div/div/div/div[2]/ul/p-multiselectitem[2]/li'

    CONFIRM_BTN = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/p-button/button'
    GREEN_ALERT = By.XPATH, '/html/body/app-root/div/p-toast/div/p-toastitem/div/div'
    RED_ALERT = None

    DROP_LIST_ACTIVITIES_DETAILS_PAGE_CLICK = By.CSS_SELECTOR, 'a[ng-reflect-router-link="/activities-details/0"]'
