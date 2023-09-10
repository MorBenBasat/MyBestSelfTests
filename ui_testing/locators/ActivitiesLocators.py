from selenium.webdriver.common.by import By


class ActivitiesLocators:
    DROP_LIST_ACTIVITIES_PAGE_CLICK = By.XPATH,'/html/body/app-root/div/div[1]/app-header/p-menubar/div/p-menubarsub/ul/li[2]/p-menubarsub/ul/li[3]/a'
    EDIT_ACTIVITY_BTN = By.XPATH, '/html/body/app-root/div/div[2]/app-activities/div/div/div[2]/p-card/div/div/div[' \
                                  '2]/p-footer/button[1]'
    ADDING_NEW_ACTIVITY = By.XPATH,'/html/body/app-root/div/div[2]/app-activities/div/div/div[2]/p-card/div/div/div[' \
                                   '2]/p-footer/button[2]'