from errors import ErrorMail

class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    @property
    def get_email(self):
        return self.__email

    @get_email.getter
    def set_email(self, new_email):
        if new_email.count('@') == 1 and '@.' in new_email:
            return new_email
        raise ErrorMail('')




