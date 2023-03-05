class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    @property
    def get_email(self):
        return self.__email





