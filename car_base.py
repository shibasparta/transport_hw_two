class CarBase:

    def __init__(self, owner, wheels, manufacturer, seats):
        self._owner = owner
        self.wheels = wheels
        self.manufacturer = manufacturer
        self.seats = seats

    # GETTER
    @property
    def owner(self):
        return self._owner

    # SETTER
    @owner.setter
    def owner(self, new_owner):
        print(self.owner, ' will now be chnaged to ', new_owner)
        self._owner = new_owner

    def ownerStatement(self):
        print('This is owned by', self.owner)