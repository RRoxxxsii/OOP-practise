class Money:
    def __init__(self, dollar, cent):
        self.dollar = dollar
        self.cent = cent
        self.total_cents = dollar * 100 + cent

    @property
    def dollars(self):
        return self.dollar

    @dollars.setter
    def dollars(self, number):
        self.dollar = number



