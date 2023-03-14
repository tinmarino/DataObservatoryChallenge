#!/usr/bin/env python3
"""
Title:
    Get ID from patent

Brief:
    A deterministic arithmetic operation
    From an unique indexable string to an unique integer ID

Desc:
    Para ello, necesitamos que crees funciones que nos permitan:

        1. Ingresar una patente y que la función retorne el ID asociado.
        2. Ingresar el ID y que la función retorne la patente.

    El dominio de las patentes corresponde a los siguientes: [AAAA000, AAAA001, ..., ZZZZ999],
    el ID es secuencial, comienza en 1, por lo que AAAA000 tiene ID=1,
    AAAA001 tiene ID=2, AAAB000 tiene el ID=1.001 y así sucesivamente.
    En el registro, no está incluida la letra Ñ.

TODO
    Add description of input string
    Add test
    OK Add Check
    OK Sanitize input (lower case)
"""

from argparse import ArgumentParser  # Get input
from re import match  # Check input


def patent():
    """ Main """
    res = 0

    # Parse
    args = parse_args()

    # Instanciate
    vehicle_id = VehicleId(args.patent)

    # Check in
    vehicle_id.check_patent()

    # Work
    res = vehicle_id.get_id()

    # Stdout
    print(res)

    # Python return
    return res


def parse_args():
    """ Parse, check and sanitize command line argument
    Return: namespace object with patent
    """
    parser = ArgumentParser(
        prog='patent.py',
        description='Get ID from the given vehicle patent string',
        )

    parser.add_argument(
        'patent',
        type=str,
        help='Vehicle patent string'
        )

    return parser.parse_args()


class VehicleId():
    """ Contains vehicle information and methods """
    def __init__(self, patent):
        self.patent = patent  # string
        self.id = 0  # integer

        self.head = None  # string
        self.tail = None  # integer

    def check_patent(self):
        """ Check that given patent is OK """
        self.get_head_n_tail()

    def get_head_n_tail(self):
        """ Devide the patent in head and tail parts (lazy)
        Return: (lower case A..Z string, number 0..999)
        """
        # Clause: Lazy return if work already done
        if all(elt is not None for elt in (self.head, self.tail)):
            return (self.head, self.tail)

        # Check that string is 7 characters long
        if 7 != len(self.patent):
            raise IllegalArgumentError("Input string must be 7 characetrs long")

        # Get and check head
        head = self.patent[0:4].lower()
        if not match(r'[a-z]{4}', head):
            raise IllegalArgumentError("Input string must start with 4 alpha characters (like ABCD)")
        self.head = head

        # Get and check tail
        tail = self.patent[4:7]
        if not match(r'[0-9]{3}', tail):
            raise IllegalArgumentError("Input string must end with 3 digit characters (like 012)")
        self.tail = int(tail)

        return (self.head, self.tail)

    def get_id(self):
        """ Return integer ID (lazy) """
        res = 1

        # Clause: do not work twice
        if 0 != self.id:
            return self.id

        # Divide string in 2 parts
        head, tail = self.get_head_n_tail()

        # Tail: the low part
        res += tail

        # Head: the high part
        # -- Should be a 26-based alpha string
        # -- With A as 0 and Z as 25
        i_head = 0
        for i, char in enumerate(head[::-1]):
            digit = ord(char) - ord('a')  # 97 is ord('a')
            digit *= 26**i  # enumerate function is zero based
            i_head += digit

        res += i_head * 1000

        return res


class IllegalArgumentError(ValueError):
    """ Just a better name for ValueError """


if __name__ == "__main__":
    patent()
