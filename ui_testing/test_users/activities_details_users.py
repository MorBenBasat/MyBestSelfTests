class TestActivityDetailsUsers:
    def __init__(self, activity_name, activity_text, hour):
        self.activity_name = activity_name
        self.activity_text = activity_text
        self.hour = hour


ValidActivityDetails = TestActivityDetailsUsers("activity name", "activity text", "04:20")
NoFillActivityName = TestActivityDetailsUsers("", "activity text", "04:20")
