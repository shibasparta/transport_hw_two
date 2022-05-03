import car_base

class BatsubBase(car_base.CarBase):
    def __init__(self, owner, vehicle_name, wheels, manufacturer, seats, oxygentank_hours):
        self.oxygentank_hours = oxygentank_hours
        self.release_anchor = False
        super().__init__(owner, vehicle_name, wheels, manufacturer, seats)


    def release_anchor(self):
        self.release_anchor = True
        print('Anchor has been released')

    def retrieve_anchor(self):
        self.release_anchor = False
        print('Anchor is being retrieved')
