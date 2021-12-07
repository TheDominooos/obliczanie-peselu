import click
from generate_pesel import *
from check_pesel import *


@click.group()
def pesel():
    pass


@pesel.command()
@click.argument("day", type=int)
@click.argument("month", type=int)
@click.argument("year", type=int)
@click.option("-male", is_flag=True)
@click.option("-female", required=False, is_flag=True)
def generate(day, month, year, male, female):
    generator = GeneratePesel(day, month, year, male, female)
    print("Wygenerowany pesel: %s" % (generator.generate_pesel()))


@pesel.command()
@click.argument("pid", type=str)
def check(pid):
    checker = CheckPesel(pid)
    birthdate, gender, control_number = checker.check_pesel()
    print("Data urodzenia: %s" % (birthdate))
    print("Płeć: %s" % (gender))
    print("Liczba kontrolna: %d" % (control_number))


if __name__ == "__main__":
    pesel()
