class Vehicle:
    def __init__(self, name, mileage, capacity) -> None:
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def __str__(self) -> str:
        return 'Vehicle: name = {}, mileage = {}, cap = {}'.format(self.name, self.mileage, self.capacity)

    def fare(self):
        return self.capacity * 100
    
class Bus(Vehicle):
    def __init__(self, name, mileage, capacity = 50) -> None:
        super().__init__(name, mileage, capacity)

    def __str__(self) -> str:
        return 'Bus: name = {}, mileage = {}, cap = {}'.format(self.name, self.mileage, self.capacity)

    def fare(self):
        return self.capacity * 100 * 1.1
    
print(Vehicle("Camry", 100, 5))
b = Bus("Bach Khoa", 12, 10)
print(b)
print(b.fare())
print(isinstance(b, Bus))
print(isinstance(b, Vehicle))