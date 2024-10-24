import pandas as pd

df = pd.read_excel(r".\FraDaMi\bouman_8.xlsx")


class OpenSpace:
        seats = 24
        name = [name for name in df['Miro']]
        name.insert(0, "Miro")

        
        def is_enought_seat(self):
            
                if len(self.name) > self.seats:
                        
                        print(f"there's {len(self.name) - self.seats} people too much, for the number of seat available")
                        print(f"Add {len(self.name) - self.seats} seats to match the number")
                else:
                        print("Enought seat")
                        #return function to randomize the table seat with the names

        def too_much_people(self):
                if len(self.name) > self.seats:
                        print(self.name)
                        #return function to randomize the table seat with the names even if there is more people then seat available
                else:
                        return False


        def add_name(self):
                    name = input("Enter the name you wan't to add : ")
                    self.name.insert(0, name)
                    return op.is_enought_seat()

                

op = OpenSpace()





op.add_name()
op.too_much_people()


