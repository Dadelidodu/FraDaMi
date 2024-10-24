import random
class Openspace:
    def __init__(self, tables):
        self.tables =  tables
        self.number_of_tables = len(tables)

    def organize(self, tables, seats, names):
        temp_names = names
        for x in tables:
            for x in seats:
                random_name = random.choice(temp_names)
                x.set_occupant(random_name)
                temp_names.remove(random_name)

    def display(self):
        pass

    def store(self):
        pass