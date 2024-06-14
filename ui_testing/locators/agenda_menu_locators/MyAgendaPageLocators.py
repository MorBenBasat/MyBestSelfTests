from selenium.webdriver.common.by import By


class MyAgendaPageLocators:
    OPEN_AGENDA_DROP_LIST = By.XPATH, "/html/body/app-root/div/div[1]/app-header/p-menubar/div/p-menubarsub/ul/li[" \
                                      "2]/div/a"
    AGENDA_DROP_LIST = By.XPATH, '/html/body/app-root/div/div[' \
                                 '1]/app-header/p-menubar/div/p-menubarsub/ul/li[2]/a'
    DAY_LABEL = By.XPATH, '//*[@id="fc-dom-34"]'

    # לוקטרים לכניסה לדפי אקטיביטיז ופרטים
    PLUS_BTN_OPEN_ACTIVITY_DETAILS = By.XPATH, '/html/body/app-root/div/div[2]/app-agenda/div/p-button[1]/button'
    FOLDER_BTN_OPEN_ALL_ACTIVITIES = By.XPATH, '/html/body/app-root/div/div[2]/app-agenda/div/p-button[2]/button'

    TODAY_BTN = By.XPATH, '/html/body/app-root/div/div[2]/app-agenda/div/full-calendar/div[1]/div[3]/button'
    YESTERDAY_BTN = By.XPATH, '/html/body/app-root/div/div[2]/app-agenda/div/full-calendar/div[1]/div[3]/div/button[1]'
    TOMORROW_BTN = By.XPATH, '/html/body/app-root/div/div[2]/app-agenda/div/full-calendar/div[1]/div[3]/div/button[2]'
    DAY_TEXT = By.XPATH,'/html/body/app-root/div/div[2]/app-agenda/div/full-calendar/div[1]/div[1]/h2'
