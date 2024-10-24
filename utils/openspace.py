import pandas as pd

df = pd.read_excel(r".\FraDaMi\bouman_8.xlsx")


name_list = [name for name in df['Names']]



class OpenSpace:
        
        def __init__(self, seats=24, number_of_people=len(name_list), table=6):
            self.seats = seats
            self.number_of_people = number_of_people
            self.table = table

        def __str__(self):
                print(f"Number of table {self.table}, number of seat {self.seats} and number of people {self.number_of_people}")
            
        def is_enought_seat(self):
                if self.number_of_people > self.seats:
                        print("Let's add tables and seats")
                        op.add_table_seats()
                   
                else:
                        return True
        
        def add_table_seats(self):
                while self.number_of_people > self.seats:
                        self.table = self.table + 1
                        self.seats = self.seats + 4
                print(f"Number of table needed : {self.table}")
                print(f"Number of seats needed: {self.seats}")
                op.is_enought_seat()

                
        


                

op = OpenSpace()

def run():
        op.__init__()
        op.__str__()
        op.is_enought_seat()
        
        
        

run()





