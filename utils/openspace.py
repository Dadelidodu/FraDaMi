
# Importing class Table from table.py file


from utils.table import Table, Seat
from utils.file_utils import name_list
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
                
                if len(temp_names) > 0:
                    random_name = random.choice(temp_names)
                    table.assign_seat(random_name)
                    temp_names.remove(random_name)
                    self.dictionary[key_name].append(random_name)
                else: 
                    table.assign_seat('Free Spot')
                    self.dictionary[key_name].append(f'Free Spot {i}')
            
                

    def display(self):

        print(pd.DataFrame(self.dictionary))

        if self.dictionary:
            return pd.DataFrame(self.dictionary)
        else:
            return pd.DataFrame()

    def store(self, filename):
        df = pd.DataFrame(self.dictionary)
        df.to_excel(filename, index=False)




