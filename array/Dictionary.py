class Bike():
    def __init__(self):
        self.Name = ""
        self.Price = 0
    def SetBike(self, name, price):
        self.Name = name
        self.Price = price


names = ["bike1", "bike2", "bike3"]
prices = [100, 10, 1]
bikes = {}

for i in range(len(names)):
    b = Bike()
    b.SetBike(names[i], prices[i])
    bikes[names[i]] = b

for name in names:
    print(bikes[name].Name, bikes[name].Price)