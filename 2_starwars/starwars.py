#!/usr/bin/env python

"""
Read starwars obejct from a json file on the internet
"""

from urllib.request import urlopen
from json import loads as json_loads, load as json_load
from re import search  # To search BBY or ADF (ABF for After Battle of Yavin)
from math import isnan  # To handle the unknown age of the droid


def starwars():
    """ Main """
    # Read person
    # TODO uncomment, just for test
    # pylint: disable=using-constant-test
    if False:
        with urlopen('https://swapi.dev/api/people/') as url:
            data = json_loads(url.read().decode())
    else:
        with open('./test/data_person.json', encoding="utf-8") as url:
            data = json_load(url)

    # Loop print person
    a_person = []
    for json_person in data['results']:
        person = Person.from_json(json_person)
        print(person)
        a_person += [person]


class Person():
    # pylint: disable=too-many-instance-attributes
    """ A person from starwars """
    def __init__(self):
        # pylint: disable=unused-private-member
        self.name = None
        self.height = None  # In cm
        self.__mass = None
        self.__hair_color = None
        self.__skin_color = None
        self.__eye_color = None
        self.__birth_year = None
        self.gender = None
        self.homeworld = None
        self.__species = None
        self.__vehicles = None
        self.__starships = None
        self.url = None

    @staticmethod
    def from_json(json_person):
        """ Craft a person from a json object """
        # pylint: disable=unused-private-member,protected-access
        person = Person()
        person.name = json_person['name']
        person.height = json_person['height']
        person.__mass = json_person['mass']
        person.__hair_color = json_person['hair_color']
        person.__skin_color = json_person['skin_color']
        person.__eye_color = json_person['eye_color']
        person.__birth_year = json_person['birth_year']
        person.gender = json_person['gender']
        person.homeworld = json_person['homeworld']
        person.__species = json_person['species']
        person.__vehicles = json_person['vehicles']
        person.__starships = json_person['starships']
        person.url = json_person['url']

        # Sanitize
        person.height = int(person.height)
        person.__mass = int(person.__mass)
        return person

    def get_birth_date(self):
        """ Return the birth date as a flot with Battle of Yavin as 0) """
        # Clause: lazy
        if isinstance(self.__birth_year, float):
            return self.__birth_year

        if "unknown" == self.__birth_year:
            return float('nan')

        if search(r'BBY', str(self.__birth_year)):
            self.__birth_year = float('-' + self.__birth_year.replace('BBY', ''))
        #if search(r'ABF', self.__birth_year):
        elif search(r'ABF', str(self.__birth_year)):
            self.__birth_year = float(self.__birth_year.replace('ABF', ''))
        else:
            try:
                self.__birth_year = float(self.__birth_year)
            except ValueError:
                return float('nan')

        return self.__birth_year


    def __str__(self):
        res = ''

        # Craft: Age string to know if older than darth vader
        birth = self.get_birth_date()
        darth_vader = Person()
        # pylint: disable=unused-private-member,protected-access
        darth_vader.__birth_year = -41.9  # WARNING: data hardcode
        ret = self.is_older(darth_vader)
        birth_cmp = f'{color("I do not know")} if is older that Darth Vader'
        if ret is None:
            pass
        elif 0 < ret:
            birth_cmp = f'Is {color("older")} that Darth Vader'
        else:
            birth_cmp = f'Is {color("younger")} that Darth Vader'

        # Concatenate key:value pairs
        for key, value in [
                ['0/ Name', self.name],
                ['1/ BMI', f'{self.get_bmi():.3f}'],
                ['2/ Human', "Yes" if self.is_human() else "No"],
                ['3/ Machines', self.get_machine_quantity()],
                ['4/ Birth', "%0.1f" % birth + '  # ' + birth_cmp],
                ['5/ Homeworld', self.get_homeworld()],
                ]:
            res += f'{color(key)}: {value}\n'
        res += color('----------------------------') + '\n'
        return res

    def get_bmi(self):
        """ Una función pública que permita calcular el IMC de cada persona
        -- peso / altura2 (nos preocupa su salud)
        Note: body mass index <= indice de masa corporal
        Return: <float> indice de masa corporal
        """
        # Clause: do not divide by 0
        if 0 == self.height**2:
            raise ValueError('Person height is zero so I cannot get her or his IMC (name={name})')

        return self.__mass / self.height**2 * 10000  # Because height must be in meter

    
    def get_species(self):
        """ TODO: Get names of the species objects of this person
        Return: <list[string]>
        """
        return []

    def is_human(self):
        """ Una función pública que nos diga si la persona es humana o no
        Return: <bool>
        """
        # WARNING: Hard code
        if 'https://swapi.dev/api/species/1' in self.get_species():
            return True
        return False

    def get_machine_quantity(self):
        """ Una función pública que diga cuántos vehículos y naves tiene en total la persona. """
        return len(self.__vehicles) + len(self.__starships)

    def is_older(self, person2):
        """ Una función pública que permita compararse con otra persona,
        -- y nos diga cuál de las dos tiene mayor edad.
        tip: no tienes por qué saberlo, pero la fecha está con el sufijo
        -- BBY que significa Before Battle of Yavin (ABF para After Battle of Yavin),
        para que lo que tengas en consideración.

        Return: True, False or None
        """
        # Get dates
        birth1 = self.get_birth_date()
        birth2 = person2.get_birth_date()

        # Clause: Cannot compare no numbers
        if any(isnan(elt) or (not isinstance(elt, float) and not isinstance(elt, int))
                for elt in [birth1, birth2]):
            return None

        return birth1 < birth2

    def get_homeworld(self):
        """ Una función pública que nos devuelva el planeta de origen (homeworld) como un objeto """
        # Warning hardcode
        hardcoded_dict = {
                'https://swapi.dev/api/planets/1/': 'Tatooine',
                'https://swapi.dev/api/planets/2/': 'Alderaan',
                'https://swapi.dev/api/planets/8/': 'Naboo',
                'https://swapi.dev/api/planets/20/': 'Stewjon',
        }

        res = self.homeworld
        if self.homeworld in hardcoded_dict:
            res = hardcoded_dict[self.homeworld]
        return res


def color(msg):
    """ Return: Anisi escaped colored string """
    return f'\033[34m{msg}\033[0m'


if __name__ == "__main__":
    starwars()
