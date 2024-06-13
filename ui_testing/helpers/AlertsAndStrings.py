from test_users.register_users import ValidRegistrationUser


class Alerts:
    def __init__(self, alert):
        self.alert = alert


DisableBtn = Alerts("כפתור מוצג לא לחיץ")
AbleBtn = Alerts("כפתור מוצג לחיץ")
SuccessLogin = Alerts("כניסה למערכת בוצעה בהצלחה")
LoginTitleText = Alerts("כותרת מציגה כניסה למערכת")
MandatoryText = Alerts("טקסט דרישת מילוי מופיע")

ActivityPageAgendaDropList = Alerts("Activities Page Agenda Open By Drop List")
AgendaPagePageOpen = Alerts("Activities page opens properly")
CardDoesntAdded = Alerts("New activity was not added successfully")