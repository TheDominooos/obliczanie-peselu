import random


class GeneratePesel:
    def __init__(self, day, month, year, male, female):
        self.day = day
        self.month = month
        self.year = year
        self.male = male
        self.female = female

    def generate_pesel(self):
        # if not 1 <= self.month <= 12:
        #     quit("Błędny miesiąc!")
        # if not 1 <= self.day <= 31:
        #     quit("Błędny dzień!")

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
            quit("Błędny rok!")

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
