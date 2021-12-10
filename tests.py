from click.testing import CliRunner
from main import *
from check_pesel import *
from generate_pesel import *
from generate_control_number import *

# TESTING PESEL GENERATOR

generator = GeneratePesel(25, 6, 2004, "-male", None)
pid = generator.generate_pesel()


def test_generator_length():
    if len(pid) != 11:
        assert False, "test failed because len(pid)=%d" % (len(pid))


def test_generator_gender():
    if generator.generate_gender() % 2 != 1:
        assert False, "test failed because gender_number is an even number"


def test_generator_year():
    if pid[0:2] != "04":
        assert False, "test failed because year=%s" % (pid[0:2])


def test_generator_month():
    month_check = GeneratePesel(25, 6, 2004, "-male", None)
    month = month_check.generate_month()
    if month != 26:
        assert False, "test failed because month=%d" % (month)


def test_generator_day():
    if pid[4:6] != "25":
        assert False, "test failed because day=%d" % (pid[4:6])


# TESTING PESEL CHECKER

checker = CheckPesel("04262507017")


def test_checker_month():
    month = checker.check_month(26)
    if month != (20, 6):
        assert False, "test failed because century and month=%d, %d" % (month)


def test_checker_gender():
    gender = checker.check_gender()
    if gender != "mężczyzna":
        assert False, "test failed because gender=%s" % (gender)


def test_checker_results():
    birthdate, gender, control_number = checker.check_pesel()
    if not birthdate == "25.6.2004" and gender == "mężczyzna" and control_number == "7":
        assert False, "test failed because results are %s %s %s" % (
            birthdate,
            gender,
            control_number,
        )


# TESTING MAIN.PY CLICK FUNCTIONALITY


def test_click_check():
    runner = CliRunner()
    result = runner.invoke(check, ["04262507017"])
    assert "Data urodzenia: 25.6.2004" in result.output
    assert "Płeć: mężczyzna" in result.output
    assert "Liczba kontrolna: 7" in result.output


def test_click_generate():
    runner = CliRunner()
    result = runner.invoke(generate, ["25", "6", "2004", "-male"])
    assert "Wygenerowany pesel: " in result.output
    assert "042625" in result.output[20:26]


# TESTING DAY CHECKER


def test_day_checker():
    day_checker = CheckDay(29, 2, 2000)
    day_checker.check_day()
    assert True


def test_leap_year():
    day_checker = CheckDay(29, 2, 2000)
    assert day_checker.check_leap_year()


# TESTING CONTROL NUMBER GENERATOR


def test_generator_control_number():
    generate_control_number = GenerateControlNumber("0426250701")
    control_number = generate_control_number.generate_control_number()
    if control_number != "7":
        assert False, "test failed because control number: %s" % (control_number)
