import random

class Cars:
    group = "Toyota"
    group = "Volkswagen"

    def __init__(self, color, model):
        self.weight = 1000
        self.width = 1.5
        self.length = 5
        self.color = color
        self.model = model

    def to_ride(self):
        print("Поїхали!")

    def to_stop(self):
        print("Стоп!")

    def ride(self, ride):
        ride = self.model + str(ride)
        live_cube = random.randint(1, 2)
        if live_cube == 1:
            self.to_ride()
        elif live_cube == 2:
            self.to_stop()


Tiguan = Cars("Gray", "Tiguan")
print(Tiguan)
