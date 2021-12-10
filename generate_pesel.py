import random
from check_day import *
from generate_control_number import *  # czy import moze byc w dwoch plikach


class GeneratePesel:
    def __init__(self, day, month, year, male, female):
        self.day = day
        self.month = month
        self.year = year
        self.male = male
        self.female = female

    def generate_month(self):
        if not 1 <= self.month <= 12:
            raise ValueError("Błędny miesiąc!")
        if 1800 <= self.year <= 1899:
            self.month += 80
        elif 1900 <= self.year <= 1999:
            pass
        elif 2000 <= self.year <= 2099:
            self.month += 20
        elif 2100 <= self.year <= 2199:
            self.month += 40
        elif 2200 <= self.year <= 2299:
            self.month += 60
        else:
            raise ValueError("Błędny rok!")
        return self.month

    def generate_gender(self):
        if self.male:
            gender_number = random.randrange(1, 10000, 2)
        else:
            gender_number = random.randrange(0, 9999, 2)
        return gender_number

    def generate_pesel(self):
        month = self.generate_month()
        check_day = CheckDay(self.day, month, self.year)
        check_day.check_day()
        self.year = self.year % 100
        gender_number = self.generate_gender()
        pid = str("%02d%02d%02d%04d" % (self.year, month, self.day, gender_number))
        generate_control_number = GenerateControlNumber(pid)
        control_number = generate_control_number.generate_control_number()
        pid += control_number
        return pid
