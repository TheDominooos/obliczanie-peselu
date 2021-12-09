class GenerateControlNumber:
    def __init__(self, pid):
        self.pid = pid

    def generate_control_number(self):
        control_number = 0
        for index, number in enumerate(self.pid):
            if index == 0 or index == 4 or index == 8:
                control_number += (int(number) * 1) % 10
            if index == 1 or index == 5 or index == 9:
                control_number += (int(number) * 3) % 10
            if index == 2 or index == 6:
                control_number += (int(number) * 7) % 10
            if index == 3 or index == 7:
                control_number += (int(number) * 9) % 10
        control_number = control_number % 10
        control_number = 10 - control_number
        control_number = control_number % 10
        return str(control_number)
