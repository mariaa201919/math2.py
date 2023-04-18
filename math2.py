import math

class Tree:
    def __init__(self, name, height, diameter):
        self.name = name
        self.height = height
        self.diameter = diameter
    
    def calculate_volume(self):
        radius = self.diameter / 2
        volume = math.pi * (radius ** 2) * self.height
        return volume
    
oak = Tree("Oak", 15, 5)
maple = Tree("Maple", 20, 7)

print(f"The {oak.name} tree has a volume of {oak.calculate_volume()} cubic feet.")
print(f"The {maple.name} tree has a volume of {maple.calculate_volume()} cubic feet.")
