import random


class GeneratePesel:
    def __init__(self, day, month, year, male, female):
        self.day = day
        self.month = month
        self.year = year
        self.male = male
        self.female = female

    def generate_pesel(self):
        if self.year >= 2200:
            self.month += 60
        elif self.year >= 2100:
            self.month += 40
        elif self.year >= 2000:
            self.month += 20
        elif self.month >= 1800 and self.month <= 1899:
            self.month += 80
        self.year = self.year % 100
        if self.male:
            pppp = random.randrange(1, 10000, 2)
        else:
            pppp = random.randrange(0, 9999, 2)

        pid = str("%02d%02d%02d%04d" % (self.year, self.month, self.day, pppp))
        control_number = 0
        index = 0

        for number in pid:
            if index == 0 or index == 4 or index == 8:
                control_number += (int(number) * 1) % 10
            if index == 1 or index == 5 or index == 9:
                control_number += (int(number) * 3) % 10
            if index == 2 or index == 6:
                control_number += (int(number) * 7) % 10
            if index == 3 or index == 7:
                control_number += (int(number) * 9) % 10
            index += 1
        control_number = control_number % 10
        control_number = 10 - control_number
        pid = pid + str(control_number % 10)
        return pid
