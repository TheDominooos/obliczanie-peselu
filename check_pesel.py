class CheckPesel:
    def __init__(self, pid):
        self.pid = pid

    def check_pesel(self):
        if len(self.pid) != 11:
            raise ValueError("Błędna ilość znaków w peselu!")
        if not (self.pid).isdigit():
            raise ValueError("Pesel może zawierać tylko cyfry")

        year_of_birth = self.pid[0:2]
        month_of_birth = int(self.pid[2:4])
        day_of_birth = int(self.pid[4:6])

        if int(self.pid[9]) % 2 == 1:
            gender = "mężczyzna"
        else:
            gender = "kobieta"

        if 81 <= int(month_of_birth) <= 92:
            century_of_birth = 18
            month_of_birth = int(month_of_birth) - 80
        elif 1 <= int(month_of_birth) <= 12:
            century_of_birth = 19
        elif 21 <= int(month_of_birth) <= 32:
            century_of_birth = 20
            month_of_birth = int(month_of_birth) - 20
        elif 41 <= int(month_of_birth) <= 52:
            century_of_birth = 21
            month_of_birth = int(month_of_birth) - 40
        else:
            raise ValueError("Błędny miesiąc!")

        if not 1 <= day_of_birth <= 31:
            raise ValueError("Błędny dzień!")
        control_number = 0
        index = 0

        for index, number in enumerate(self.pid):
            if index == 0 or index == 4 or index == 8:
                control_number += (int(number) * 1) % 10
            if index == 1 or index == 5 or index == 9:
                control_number += (int(number) * 3) % 10
            if index == 2 or index == 6:
                control_number += (int(number) * 7) % 10
            if index == 3 or index == 7:
                control_number += (int(number) * 9) % 10
        control_number = 10 - (control_number % 10)

        if control_number != int(self.pid[10]):
            raise ValueError("Liczba kontrolna się nie zgadza!")
        birthdate = "%d.%d.%d%s" % (
            day_of_birth,
            month_of_birth,
            century_of_birth,
            year_of_birth,
        )
        return birthdate, gender, control_number
