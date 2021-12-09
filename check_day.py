class CheckDay:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def check_leap_year(self):
        if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
            return True
        else:
            return False

    def check_day(self):
        if not 1 <= self.day <= 31:
            raise ValueError("Błędny dzień!")
        elif self.month in [4, 6, 9, 11] and self.day > 30:
            raise ValueError("Błędny dzień!")
        elif self.month == 2:
            if self.day > 29:
                raise ValueError("Błędny dzień!")
            if self.day > 28 and not self.check_leap_year():
                raise ValueError("Błędny dzień!")
