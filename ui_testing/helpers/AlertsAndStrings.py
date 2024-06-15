from helpers.Helpers import HelpersMbs
from test_users.activities_details_users import ValidActivityDetails
from test_users.login_users import SuccessLoginUser
from test_users.register_users import ValidRegistrationUser

today_date = HelpersMbs.get_today_date_in_hebrew()


class AlertsString:
    def __init__(self, alert: object, my_string: object) -> object:
        self.alert = alert
        self.my_string = my_string


TextExpected = AlertsString(None, "Text is as expected:")

# LoginStrings
SuccessLogin = AlertsString(None, "כניסה למערכת בוצעה בהצלחה")
LoginTitleVerify = AlertsString(None, "כותרת מציגה כניסה למערכת")

# Register Strings
UserCreate = AlertsString(None, "User Created")
SignUpPageOpen = AlertsString(None, "נפתח דף הרשמה למערכת")

# Activity Strings
CardDoesntAdded = AlertsString(None, "New activity was not added successfully")
ActivitiesOpen = AlertsString(None, "Activities page shown")
ActivityPageDropList = AlertsString(None, "Activities Page Open By Drop List")

# Agenda Strings
TodayBtnDisable = AlertsString(None, "כפתור היום צריך להופיע לא לחיץ")
VerifyTodayDisable = AlertsString(None, "כפתור היום מופיע לא לחיץ : ")
AgendaPageOpen = AlertsString(None, "Agenda page opens properly")
AgendaPageOpenByDropList = AlertsString(None, "Agenda page open by drop list!")
DaysDontMatch = AlertsString(None, "The displayed day does not match today's date")
YesterdayBtnInvalidText = AlertsString(None,"The displayed date does not match yesterday's date.")
# Activity Details Strings
DaysText = AlertsString(None, "Days Count : ")
DetailsPageAgendaOpenPlusIcon = AlertsString(None, "Activities Details Page Open By Plus Icon")
DetailsPageAgendaOpenDropList = AlertsString(None, "Activities Details Page Open By Drop List!")
NewActivityCreate = AlertsString(None, f" מופיעה בהערת יצירה {ValidActivityDetails.activity_name}משימה חדשה: ")
DayRemoved = AlertsString(None, "Day successfully removed!")
TimeDontChange = AlertsString(None, "The time should have changed after using the arrows")

# General Strings
CompareTextFail = AlertsString(None, "Expected message does not match actual message")
DisableBtn = AlertsString(None, "כפתור מוצג לא לחיץ")
AbleBtn = AlertsString(None, "כפתור מוצג לחיץ")
MandatoryText = AlertsString(None, "טקסט דרישת מילוי מופיע")
DropListClearField = AlertsString(None, "שדות נקיים בכניסה לדרופ ליסט")
ExpectedDate = AlertsString(None, f"Expected date: {today_date}")
ActualDate = AlertsString(None, "Actual day text:")

# My Profile Strings
LogoOpenMyProfile = AlertsString(None, "My profile open on logo click")

#############################################################################################

# General Alerts
MandatoryFieldText = AlertsString("נא מלא שדה זה לפני שליחה", None)
NoResultText = AlertsString("No results found", None)

# Login Alerts
LoginLengthErrorText = AlertsString("המינימום תווים בשדה זה הוא 6", None)
LoginTitleText = AlertsString("כניסה למערכת", None)
SuccessLoginText = AlertsString(f'כניסה למערכת\nברוך הבא {SuccessLoginUser.username}', None)

# Register Alerts
AfterRegisterLoginSystem = AlertsString(f'כניסה למערכת\nברוך הבא {ValidRegistrationUser.username}', None)
UserExist = AlertsString("User already exists", None)
UserCreateText = AlertsString(f'הרשמה למערכת\nברוך הבא {ValidRegistrationUser.firstname} אנו שמחים שבחרת להצטר'
                              f' אלינו', None)

# Recover Password Alerts
ValidMailMandatoryMessage = AlertsString("נא להזין מייל חוקי", None)

# Activity Page Alerts
UpdateUserAlert = AlertsString(f"עדכון פריט סדר יום\nפריט סדר יום: {HelpersMbs.random_string()} התעדכן בהצלחה", None)
