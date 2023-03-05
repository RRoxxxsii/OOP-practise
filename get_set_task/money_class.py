from errors import ErrorDollars, ErrorCents

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
        if isinstance(number, int):
            self.dollar = number
        raise ErrorDollars

    @property
    def cents(self):
        return self.cent

    @cents.setter
    def cents(self, number):
        if isinstance(number, int) and number <= 100:
            self.cent = number
        else:
            raise ErrorCents


