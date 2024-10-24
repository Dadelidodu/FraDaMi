class Seat:

    def __init__(self, free: bool = True, occupant: str = None):

        self.free = free
        self.occupant = occupant

    def __str__(self):

        if self.free == True:
            return "A free spot"
        else:
            return "{self.occupant} is sitting there".format(self=self)

    def set_occupant(self, name: str):

        if self.free == True:
            self.occupant = name
            self.free = False

    def remove_occupant(self):

        self.free = True
        print(f'{self.occupant} was sitting here')
        self.occupant = None


# Defining and initiating class Table

class Table():

    def __init__(self, capacity: int = 4):

        self.capacity = capacity
        self.seats = []
        for i in range(capacity):
            self.seats.append(Seat())

    def has_free_spot(self):

        for seat in self.seats:
            if seat.free:
                print(True)
                break

    def left_capacity(self):

        free_spot_list = []
        for seat in self.seats:
            if seat.free == True:
                free_spot_list.append(seat)

        if len(free_spot_list) == 1:
            print(f'{len(free_spot_list)} last spot remaining')
            return len(free_spot_list)
        elif len(free_spot_list) > 1:
            print(f'{len(free_spot_list)} spots remaining')
            return len(free_spot_list)
        else:
            print('No more free spots')
            return 0

    def assign_seat(self, name: str = None):

        for index, seat in enumerate(self.seats):
            if seat.free == True:
                seat.set_occupant(name)
                break
            elif seat.free == False:
                pass
            else:
                print('No more free spots')