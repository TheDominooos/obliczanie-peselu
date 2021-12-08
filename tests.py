from click.testing import CliRunner
from main import *
from check_pesel import *
from generate_pesel import *

generator = GeneratePesel(25, 6, 2004, "-male", None)
string_pid = generator.generate_pesel()


def test_generator_length():
    if len(string_pid) != 11:
        assert False


integer_map = map(int, string_pid)
pid = list(integer_map)


def test_generator_gender():
    if pid[9] not in [1, 3, 5, 7, 9]:
        assert False, "test failed because pid=" + string_pid[9] + " is not in list"


def test_generator_year():
    if pid[0] != 0 or pid[1] != 4:
        assert False, "test failed because pid year=%d%d" % (pid[0], pid[1])


def test_generator_month():
    if pid[2] != 2 or pid[3] != 6:
        assert False, "test failed because pid month=%d%d" % (pid[2], pid[3])


def test_generator_day():
    if [pid[4], pid[5]] != [2, 5]:
        assert False, "test failed becaude pid day=%d%d" % (pid[4], pid[5])


checker = CheckPesel("04262507017")
birthdate, gender, control_number = checker.check_pesel()


def test_checker_date():
    if birthdate != "25.6.2004":
        assert False, "test failed because birthdate=%s" % (birthdate)


def test_checker_gender():
    if gender != "mężczyzna":
        assert False, "test failed because gender=%s" % (gender)


def test_checker_control_number():
    if control_number != 7:
        assert False, "test failed because control number=%d" % (control_number)


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
