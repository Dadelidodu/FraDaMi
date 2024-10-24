import pandas as pd

df = pd.read_excel(r".\FraDaMi\bouman_8.xlsx")


name_list = [name for name in df['Names]]



class OpenSpace:
        
        def __init__(self, seats=24, number_of_people=len(name_list), table=6):
            self.seats = seats
            self.number_of_people = number_of_people
            self.table = table

        def __str__(self):
                if self.seats < self.number_of_people:
                        return "Not enought places"
                else:
                        return "Enought places"
            
        def is_enought_seat(self):
                
                if self.number_of_people < self.seats:
                        return True
                else:
                        return False
                        

        def too_much_people(self):
                if self.number_of_people > self.seats:
                        print("There is too much people for the seat available. Let's add a table")
                        return True
                   
                else:
                        return False
        
        def add_table_seats(self):
                self.table = self.table + 1
                self.seats = self.seats + 4
                print(self.table)
                print(self.seats)

                
        


                

op = OpenSpace()

def main():
        op.too_much_people()
        op.is_enought_seat()
        op.__str__()

main()





