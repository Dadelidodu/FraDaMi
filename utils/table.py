class Seat:
    def __init__(self, free, occupant =""):
        self.free = free
        self.occupant = occupant

    def set_occupant(self, name):
        if self.free:
            self.free = False
            self.occupant = name

    def remove_occupant(self):
        previous_occupant = self.occupant
        self.free  = True
        self.occupant = ""
        return previous_occupant

class Table:
    def __init__(self, seats):
        self.capacity = len(seats)
        self.seats = seats

    def has_free_spot(self):
        for x in self.seats:
            if x.free:
                return True

    def assign_seat(self, name):
        for x in self.seats:
            x.set_occupant(name)

    def left_capacity(self):
        capacity_left = self.capacity
        for x in self.seats:
            if not x.free:
                capacity_left -= 1
        return capacity_left
