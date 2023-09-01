class PagesUrl:
    def __init__(self, login, signup, my_profile, agenda, activities_details, activities, logout):
        self.login = login
        self.register = signup
        self.my_profile = my_profile
        self.agenda = agenda
        self.activities_details = activities_details
        self.activities = activities
        self.logout = logout


# Creating an object of the Person class
PagesUrlMbs = PagesUrl("http://localhost:4200/login", "http://localhost:4200/register",
                       "http://localhost:4200/my-profile", "http://localhost:4200/agenda",
                       "http://localhost:4200/activities-details/0", "http://localhost:4200/activities",
                       "http://localhost:4200/logout")

