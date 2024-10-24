import pandas as pd


df = pd.read_excel(r".\FraDaMi\bouman_8.xlsx")


name_list = [name for name in df['Names']]



class OpenSpace:
        
        def __init__(self, seats=24, number_of_people=len(name_list), table=6):
            """
            Function initiating the class
            """

            self.seats = seats
            self.number_of_people = number_of_people
            self.table = table

        def __str__(self):
                """
                Function returning the basics arguments

                return the number of table,seats and people in the beginning
                """

                print(f"Number of table {self.table}, number of seat {self.seats} and number of people {self.number_of_people}")
            
        def is_enought_seat(self, number_of_people, seats):
                """
                Function to know if we have enought seats compared to the number of people
                
                param number_of_people : An int to know how much people there is in total
                param seats : An int to know how much seat there is
                return a message to tell us to had tables,seats if needed and use the functions "add_table_seats" to add them or return "True if there is enought".
                """

                if number_of_people > seats:
                        print("Let's add tables and seats")
                        op.add_table_seats()
                   
                else:
                        return True
        
        def add_table_seats(self, number_of_people, table, seats):
                """
                Function to calculate the number of tables and seats we need for the number of peoples and print the number of tables and seats needed for that
                
                :param number_of_people: An int to compare to the number of tables and seats available
                :param table : An int to know how much table we need
                :param seats : An int to know how much seats we need
                :return the number of tables ,seats to match the number of people
                """

                while number_of_people > seats:
                        table = table + 1
                        seats = seats + 4
                print(f"Number of table needed : {table}")
                print(f"Number of seats needed: {seats}")
                op.is_enought_seat()

                
        

                

op = OpenSpace()

def run():
        op.__init__()
        op.__str__()
        op.is_enought_seat()
        
        
       

run()
