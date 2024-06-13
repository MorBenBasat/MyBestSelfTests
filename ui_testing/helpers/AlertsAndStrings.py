from test_users.activities_details_users import ValidActivityDetails


class AlertsString:
    def __init__(self, alert, my_string):
        self.alert = alert
        self.my_string = my_string


DisableBtn = AlertsString(None, "כפתור מוצג לא לחיץ")
AbleBtn = AlertsString(None, "כפתור מוצג לחיץ")
SuccessLogin = AlertsString(None, "כניסה למערכת בוצעה בהצלחה")
LoginTitleVerify= AlertsString(None, "כותרת מציגה כניסה למערכת")
MandatoryText = AlertsString(None, "טקסט דרישת מילוי מופיע")

ActivityPageAgendaDropList = AlertsString(None, "Activities Page Agenda Open By Drop List")

AgendaPagePageOpen = AlertsString(None, "Activities page opens properly")
CardDoesntAdded = AlertsString(None, "New activity was not added successfully")
NewActivityCreate = AlertsString(None, f" מופיעה בהערת יצירה {ValidActivityDetails.activity_name}משימה חדשה: ")

DayRemoved = AlertsString(None, "Day successfully removed!")
DropListClearField = AlertsString(None, "שדות נקיים בכניסה לדרופ ליסט")
DetailsPageAgendaOpenPlusIcon = AlertsString(None, "Activities Details Page Open By Plus Icon")
DetailsPageAgendaOpenDropList = AlertsString(None, "Activities Details Page Open By Drop List!")
DetailsPageAgendaOpen = AlertsString(None, "Activities page shown")
TimeDontChange = AlertsString(None, "The time should have changed after using the arrows")
DaysText = AlertsString(None,"Days Count")
#############################################################################################

MandatoryFieldText = AlertsString("נא מלא שדה זה לפני שליחה", None)
NoResultText = AlertsString("No results found", None)
LoginLengthErrorText = AlertsString("המינימום תווים בשדה זה הוא 6",None)
LoginTitleText = AlertsString("כניסה למערכת",None)