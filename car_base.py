class CarBase:

    def __init__(self, owner, vehicle_name, wheels, manufacturer, seats):
        self._owner = owner
        self.vehicle_name = vehicle_name
        self.wheels = wheels
        self.manufacturer = manufacturer
        self.seats = seats
        self.speed = 0

    # GETTER
    @property
    def owner(self):
        return self._owner

    # SETTER
    @owner.setter
    def owner(self, new_owner):
        print(self.owner, ' will now be changed to ', new_owner)
        self._owner = new_owner

    def ownerStatement(self):
        print('The', self.vehicle_name, 'is owned by', self.owner)

    def go(self):
        self.speed = 30

    def reverse(self):
        self.speed -= (self.speed * 1.5)

    def brake(self):
        self.speed = 0

    def speedUp(self, number):
        self.speed += number

    def slowDown(self, number):
        self.speed -= number

    def shoot(self):
        print('BANG!')