import pandas as pd

df = pd.read_excel(r".\FraDaMi\bouman_8.xlsx")


name_list = [name for name in df['Names']]



class OpenSpace:
        
        def __init__(self, seats=24, number_of_people=len(name_list), table=6):
            self.seats = seats
            self.number_of_people = number_of_people
            self.table = table

        def __str__(self):
                if self.seats < self.number_of_people:
                        print("Not enought seats")
                        op.too_much_people()
                else:
                        print("Enought seats")
            
        def is_enought_seat(self):
                
                if self.number_of_people < self.seats:
                        return True
                else:
                        op.add_table_seats()
                        

        def too_much_people(self):
                if self.number_of_people > self.seats:
                        print("Let's add a table")
                        op.add_table_seats()
                   
                else:
                        return False
        
        def add_table_seats(self):
                self.table = self.table + 1
                self.seats = self.seats + 4
                print(f"Number of table : {self.table}")
                print(f"Number of table : {self.seats}")
                op.too_much_people()

                
        


                

op = OpenSpace()

def main():
        op.__init__()
        op.__str__()
        
        
        

main()





