class Car():
    def __init__(self):
        self.Name = ""
        self.Price = 0
    def setCar(self, name, price):
        self.Name = name
        self.Price = price

names = ["car1", "car2", "car3"]
prices = [100, 10, 1]
cars = []

for i in range(len(names)):
    car = Car()
    car.setCar(names[i],  prices[i])
    cars.append(car)

print(len(cars))

for c in cars:
    print(c.Name, c.Price)