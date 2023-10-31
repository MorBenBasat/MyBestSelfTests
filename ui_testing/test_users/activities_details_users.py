class TestActivityDetailsUsers:
    def __init__(self, activity_name, activity_text, hour, day):
        self.activity_name = activity_name
        self.activity_text = activity_text
        self.hour = hour
        self.day = day


ValidActivityDetails = TestActivityDetailsUsers("activity name", "activity text", "04:20",'ראשון')
NoFillActivityName = TestActivityDetailsUsers("", "activity text", "04:20",'ראשון')
NoFillWhyImDoingThis = TestActivityDetailsUsers("my mission", "", "4:20", "ראשון")
NoFillField = TestActivityDetailsUsers("", "", "",None)
