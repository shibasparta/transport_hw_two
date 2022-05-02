import car_base

class BatmobileBase(car_base.CarBase):
    def __init__(self, owner, wheels, manufacturer, seats, ejected_seats):
        self.ejected_seats = ejected_seats
        self.seats_ejected = False
        super().__init__(owner, wheels, manufacturer, seats)

    def eject_seats(self):
        print('Seats have been ejected')
        self.seats_ejected = True
