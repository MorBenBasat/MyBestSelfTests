from selenium.webdriver.common.by import By


class ActivitiesDetailsLocators:
    MY_ACTIVITY = By.XPATH, '//*[@id="activityName"]'
    ACTIVITY_DESCRIPTION = By.XPATH, '//*[@id="activityDescription"]'
    TIME_FIELD = By.XPATH, '//*[@id="activityTime"]/span/input'
    HOUR_ARROW_UP = By.XPATH, '//*[@id="activityTime"]/span/div/div/div[1]/button[1]'
    HOUR_ARROW_DOWN = By.XPATH, '//*[@id="activityTime"]/span/div/div/div[1]/button[2]'
    MIN_ARROW_UP = By.XPATH, '//*[@id="activityTime"]/span/div/div/div[3]/button[1]'
    MIN_ARROW_DOWN = By.XPATH, '//*[@id="activityTime"]/span/div/div/div[3]/button[2]'

    DAYS_FIELD = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/app-form/form/app-input' \
                           '-wrapper[4]/div/app-input-combobox-field/div/p-multiselect/div/div[2]/div'

    DAYS_SEARCH_FIELD = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/app-form/form/app-input' \
                                  '-wrapper[4]/div/app-input-combobox-field/div/p-multiselect/div/p-overlay/div/div' \
                                  '/div/div[1]/div[2]/input'

    REMOVE_DAY_SELECTION = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/app-form/form/app' \
                                     '-input-wrapper[4]/div/app-input-combobox-field/div/p-multiselect/div/div[' \
                                     '2]/div/div/timescircleicon'

    DAY_IN_DAYS_FIELD = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/app-form/form/app-input' \
                                  '-wrapper[4]/app-input-combobox-field/div/p-multiselect/div/div[2]/div/div[1]'

    SUNDAY_BTN = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/app-form/form/app-input' \
                           '-wrapper[4]/div/app-input-combobox-field/div/p-multiselect/div/p-overlay/div/div/div/div[' \
                           '2]/ul/p-multiselectitem/li/div/div'

    MONDAY_BTN = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/app-input-combobox-field/div/p' \
                           '-multiselect/div/p-overlay/div/div/div/div[2]/ul/p-multiselectitem[2]/li'

    PICK_ALL_DAYS_RADIO_BTN = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/app-form/form/app' \
                                        '-input-wrapper[' \
                                        '4]/div/app-input-combobox-field/div/p-multiselect/div/p-overlay/div/div/div' \
                                        '/div[1]/div[1]/div[2]'

    CONFIRM_BTN = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/p-button/button'

    DROP_LIST_ACTIVITIES_DETAILS_PAGE_CLICK = By.CSS_SELECTOR, 'a[ng-reflect-router-link="/activities-details/0"]'

    DROP_LIST_NEW_ACTIVITIES_DETAILS_BTN = By.XPATH, '/html/body/app-root/div/div[' \
                                                     '1]/app-header/p-menubar/div/p-menubarsub/ul/li[' \
                                                     '2]/p-menubarsub/ul/li[2]/div/a'

    ACTIVITIES_DETAILS_CONFIRM_BTN = By.XPATH, '/html/body/app-root/div/div[' \
                                               '2]/app-activities-details/div/p-button/button'
    NO_FOUND_DAY_ALERT = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/app-form/form/app-input' \
                                   '-wrapper[4]/app-input-combobox-field/div/p-multiselect/div/p-overlay/div/div/div' \
                                   '/div[2]/ul/li'
    MY_ACTIVITY_MANDATORY_TEXT = By.XPATH, '/html/body/app-root/div/div[' \
                                           '2]/app-activities-details/div/app-form/form/app-input-wrapper[1]/small'
    DAYS_MANDATORY_TEXT = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/app-form/form/app-input' \
 \
                                    '-wrapper[4]/small'
    HOUR_MANDATORY_TEXT = By.XPATH, '/html/body/app-root/div/div[2]/app-activities-details/div/app-form/form/app-input' \
 \
                                    '-wrapper[3]/small'
    GREEN_ALERT_TEXT = By.XPATH, '/html/body/app-root/div/p-toast/div/p-toastitem/div/div/div/div[2]'
    GREEN_ALERT = By.XPATH, "/html/body/app-root/div/p-toast/div/p-toastitem/div/div"
    AGENDA_MENU = By.XPATH, "/html/body/app-root/div/div[1]/app-header/p-menubar/div/p-menubarsub/ul/li[2]/div/a"
    HOUR_FIELD = By.XPATH, "/html/body/app-root/div/div[2]/app-activities-details/div/app-form/form/app-input-wrapper[" \
                           "3]/div/app-input-date-field/div/p-calendar/span/input"
    HOUR_TEXT = By.XPATH,"/html/body/app-root/div/div[2]/app-activities-details/div/app-form/form/app-input-wrapper[" \
                         "3]/div/app-input-date-field/div/p-calendar/span/div/div/div[1]/span"
    MIN_TEXT = By.XPATH,"/html/body/app-root/div/div[2]/app-activities-details/div/app-form/form/app-input-wrapper[" \
                        "3]/div/app-input-date-field/div/p-calendar/span/div/div/div[3]/span"
