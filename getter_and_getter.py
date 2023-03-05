from errors import ErrorMail

class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    @property
    def email_func(self):
        return self.__email

    @email_func.setter
    def email_func(self, new_email):
        if new_email.count('@') == 1 and '@.' in new_email:
            self.__email = new_email
            print(f'Почта была изменена: {new_email}')
        else:
            raise ErrorMail(new_email)





