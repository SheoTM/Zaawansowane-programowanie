class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"Dom: {self.area} m2, {self.rooms} pokoi, cena: {self.price} zł, adres: {self.address}, działka: {self.plot} m2"

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Mieszkanie: {self.area} m2, {self.rooms} pokoi, cena: {self.price} zł, adres: {self.address}, piętro: {self.floor}"

house1 = House(150, 5, 850000, "Katowice, Leśna 10", 600)
flat1 = Flat(55, 3, 420000, "Katowice, Graniczna 61", 2)

print(house1)
print(flat1)