# Importing class Table from table.py file

from table import Table
from table import Seat
from file_utils import name_list
import random
import pandas as pd

# Defining and initiating class Openspace

class Openspace:

    def __init__(self, number_of_tables: int = 6, number_of_seats: int = 4):

        self.number_of_tables = number_of_tables

        self.tables = []
        for i in range(number_of_tables):
            self.tables.append(Table())

        self.seats = []
        for i in range(number_of_seats):
            self.seats.append(Seat())

        self.dictionary = {}
        for x in range(number_of_tables):
            key_name = F"Table {x+1}"
            self.dictionary[key_name] = []

    def organize(self, names: list = name_list):

        temp_names = names
        for ind, table in enumerate(self.tables):
            key_name = F"Table {ind + 1}"
            for i, seat in enumerate(self.seats):
                random_name = random.choice(temp_names)
                table.assign_seat(random_name)
                temp_names.remove(random_name)
                self.dictionary[key_name].append(random_name)

    def display(self):
        print(pd.DataFrame(self.dictionary))



op1 = Openspace()
print(op1.organize())
print(op1.dictionary)
op1.display()