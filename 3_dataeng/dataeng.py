#!/usr/bin/env python
# pylint: disable=line-too-long

"""
Parse, treat and format data
"""

from os.path import dirname, abspath  # Get root dir
#from csv import reader  # read file
from numpy import genfromtxt  # read file

root_dir = dirname(abspath(__file__))
csv_file = root_dir + '/test/crucero_1.csv'

def dataeng():
    """ Main """
    csv = get_csv()

    task1_clean(csv)


def task1_clean(csv):
    """ Al cargar los datos, elimina cualquier fila o columna que esté completamente sin datos. Si tiene al menos un valor válido en la fila/columna, no la elimines en este paso y vuelve a evaluar al final del ejercicio. """
    col_len = len(csv)
    print(col_len)

    for col in range(col_len):
        col_name = csv[0, col]
        is_empty = all(not elt for elt in csv[1:,col])

        print(col_name, is_empty)

def get_csv():
    """ Get cvs as line col """
    #with open(csv_file, encoding="utf-8") as fil:
    #    my_reader = reader(fil, delimiter=",", quotechar='"')
    #    # Skip the headers
    #    #next(my_reader, None)
    #    data_read = [row for row in my_reader]
    data_read = genfromtxt(csv_file, delimiter=',')

    return data_read


if __name__ == "__main__":
    dataeng()
