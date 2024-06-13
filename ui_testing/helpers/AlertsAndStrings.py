from test_users.activities_details_users import ValidActivityDetails


class AlertsString:
    def __init__(self, alert, my_string):
        self.alert = alert
        self.my_string = my_string


DisableBtn = AlertsString(None, "כפתור מוצג לא לחיץ")
AbleBtn = AlertsString(None, "כפתור מוצג לחיץ")
SuccessLogin = AlertsString(None, "כניסה למערכת בוצעה בהצלחה")
LoginTitleText = AlertsString(None, "כותרת מציגה כניסה למערכת")
MandatoryText = AlertsString(None, "טקסט דרישת מילוי מופיע")

ActivityPageAgendaDropList = AlertsString(None, "Activities Page Agenda Open By Drop List")

AgendaPagePageOpen = AlertsString(None, "Activities page opens properly")
CardDoesntAdded = AlertsString(None, "New activity was not added successfully")
NewActivityCreate = AlertsString(None, f" מופיעה בהערת יצירה {ValidActivityDetails.activity_name}משימה חדשה: ")

NoResultText = AlertsString("No results found")
DayRemoved = AlertsString(None, "Day successfully removed!")
DropListClearField = AlertsString(None, "שדות נקיים בכניסה לדרופ ליסט")
ActivitiesDetailsPageAgenda = AlertsString(None, "Activities Details Page Open ByPlus Icon")
#############################################################################################

MandatoryFieldText = AlertsString("נא מלא שדה זה לפני שליחה", None)
