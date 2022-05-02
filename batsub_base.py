import car_base

class BatsubBase(car_base.CarBase):
    def __init__(self, owner, wheels, manufacturer, seats, oxygentank_hours):
        self.oxygentank_hours = oxygentank_hours
        self.release_anchor = False
        super().__init__(owner, wheels, manufacturer, seats)

    def ownerStatement(self):
        print('!!!!This is owned by', self.owner)

    def release_anchor(self):
        self.release_anchor = True

    def retrieve_anchor(self):
        self.release_anchor = False
