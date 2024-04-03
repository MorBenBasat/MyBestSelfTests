class PagesUrl:
    baseURL = "https://my-best-self.vercel.app"

    def __init__(self, login, signup, my_profile, agenda, activities_details, activities, logout, recover_password):
        self.login = self._combine_with_base(login)
        self.register = self._combine_with_base(signup)
        self.my_profile = self._combine_with_base(my_profile)
        self.agenda = self._combine_with_base(agenda)
        self.activities_details = self._combine_with_base(activities_details)
        self.activities = self._combine_with_base(activities)
        self.logout = self._combine_with_base(logout)
        self.recover_password = self._combine_with_base(recover_password)

    def _combine_with_base(self, path):
        return f"{self.baseURL}/{path}"


PagesUrlMbs = PagesUrl("login", "register", "my-profile", "agenda", "activities-details/0", "activities", "logout",
                       "recover-password")
