from helpers.Helpers import HelpersMbs
from pages.Agenda.MyAgendaPage import MyAgendaPage
from test_users.activities_details_users import ValidActivityDetails
from test_users.login_users import SuccessLoginUser
from test_users.register_users import ValidRegistrationUser

today_date = HelpersMbs.get_today_date_in_hebrew()


class AlertsString:
    def __init__(self, alert: object, my_string: object) -> object:
        self.alert = alert
        self.my_string = my_string


# LoginStrings
SuccessLogin = AlertsString(None, "כניסה למערכת בוצעה בהצלחה")
LoginTitleVerify = AlertsString(None, "כותרת מציגה כניסה למערכת")

#Register Strings
UserCreate = AlertsString(None, "User Created")
SignUpPageOpen = AlertsString(None, "נפתח דף הרשמה למערכת")

#Activity Strings
CardDoesntAdded = AlertsString(None, "New activity was not added successfully")
ActivitiesOpen = AlertsString(None, "Activities page shown")



DisableBtn = AlertsString(None, "כפתור מוצג לא לחיץ")
AbleBtn = AlertsString(None, "כפתור מוצג לחיץ")
MandatoryText = AlertsString(None, "טקסט דרישת מילוי מופיע")

ActivityPageAgendaDropList = AlertsString(None, "Activities Page Open By Drop List")

AgendaPageOpen = AlertsString(None, "Agenda page opens properly")
NewActivityCreate = AlertsString(None, f" מופיעה בהערת יצירה {ValidActivityDetails.activity_name}משימה חדשה: ")
AgendaPageOpenByDropList = AlertsString(None, "Agenda page open by drop list!")

DaysDontMatch = AlertsString(None, "The displayed day does not match today's date")
DayRemoved = AlertsString(None, "Day successfully removed!")
DropListClearField = AlertsString(None, "שדות נקיים בכניסה לדרופ ליסט")
DetailsPageAgendaOpenPlusIcon = AlertsString(None, "Activities Details Page Open By Plus Icon")
DetailsPageAgendaOpenDropList = AlertsString(None, "Activities Details Page Open By Drop List!")
TimeDontChange = AlertsString(None, "The time should have changed after using the arrows")
DaysText = AlertsString(None, "Days Count")
LogoOpenMyProfile = AlertsString(None, "My profile open on logo click")
CompareTextFail = AlertsString(None, "Expected message does not match actual message")
ExpectedDate = AlertsString(None, f"Expected date: {today_date}")
ActualDate = AlertsString(None, "Actual day text:")

#############################################################################################

MandatoryFieldText = AlertsString("נא מלא שדה זה לפני שליחה", None)
NoResultText = AlertsString("No results found", None)
LoginLengthErrorText = AlertsString("המינימום תווים בשדה זה הוא 6", None)
LoginTitleText = AlertsString("כניסה למערכת", None)
SuccessLoginText = AlertsString(f'כניסה למערכת\nברוך הבא {SuccessLoginUser.username}', None)
AfterRegisterLoginSystem = AlertsString(f'כניסה למערכת\nברוך הבא {ValidRegistrationUser.username}', None)
UserExist = AlertsString("User already exists", None)
UserCreateText = AlertsString(f'הרשמה למערכת\nברוך הבא {ValidRegistrationUser.firstname} אנו שמחים שבחרת להצטר'
                              f' אלינו', None)
ValidMailMandatoryMessage = AlertsString("נא להזין מייל חוקי", None)
