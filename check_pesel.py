from check_day import *
from generate_control_number import *


class CheckPesel:
    def __init__(self, pid):
        self.pid = pid

    def check_month(self, month_of_birth):
        if 81 <= month_of_birth <= 92:
            century_of_birth = 18
            month_of_birth = month_of_birth - 80
        elif 1 <= month_of_birth <= 12:
            century_of_birth = 19
        elif 21 <= month_of_birth <= 32:
            century_of_birth = 20
            month_of_birth = month_of_birth - 20
        elif 41 <= month_of_birth <= 52:
            century_of_birth = 21
            month_of_birth = month_of_birth - 40
        else:
            raise ValueError("Błędny miesiąc!")
        return century_of_birth, month_of_birth

    def check_gender(self):
        if int(self.pid[9]) % 2 == 1:
            gender = "mężczyzna"
        else:
            gender = "kobieta"
        return gender

    def check_pesel(self):
        if len(self.pid) != 11:
            raise ValueError("Błędna ilość znaków w peselu!")
        if not (self.pid).isdigit():
            raise ValueError("Pesel może zawierać tylko cyfry")

        year_of_birth = self.pid[0:2]
        month_of_birth = int(self.pid[2:4])
        day_of_birth = int(self.pid[4:6])
        century_of_birth, month_of_birth = self.check_month(month_of_birth)
        check_day = CheckDay(
            day_of_birth, month_of_birth, int(str(century_of_birth) + year_of_birth)
        )
        check_day.check_day()
        gender = self.check_gender()
        generate_control_number = GenerateControlNumber(self.pid)
        control_number = generate_control_number.generate_control_number()
        if control_number != str(self.pid[10]):
            raise ValueError("Liczba kontrolna się nie zgadza!")
        birthdate = "%d.%d.%d%s" % (
            day_of_birth,
            month_of_birth,
            century_of_birth,
            year_of_birth,
        )
        return birthdate, gender, control_number
