"""Object Oriented Programming in Python"""

# Assignment 1
class Smartphone:
    """Class representing a smartphone"""
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = 100
        self.is_on = False

    def power_toggle(self):
        """Toggle the power state of the smartphone"""
        self.is_on = not self.is_on
        return f"{self.brand} {self.model} is {'on' if self.is_on else 'off'}"

    def use_battery(self, amount):
        """Use a certain amount of battery"""
        if self.battery >= amount:
            self.battery -= amount
            return f"Battery remaining: {self.battery}%"
        return "Battery too low!"

class SmartphonePro(Smartphone):
    """Class representing a premium smartphone"""
    def __init__(self, brand, model, storage, camera_mp):
        super().__init__(brand, model, storage)
        self.camera_mp = camera_mp

    def take_photo(self):
        """Take a photo with the smartphone"""
        if self.is_on and self.battery > 5:
            self.use_battery(5)
            return f"Taking photo with {self.camera_mp}MP camera"
        return "Cannot take photo"

smartphone = Smartphone("Infinix", "Hot 10", 128)
print(smartphone.power_toggle())
print(smartphone.use_battery(20))

premium_smartphone = SmartphonePro("Samsung", "S22", 256, 108)
print(premium_smartphone.power_toggle())
print(premium_smartphone.take_photo())

# Polymorphism challenge
# Activity 2
class Car():
    """Car movement"""
    def move(self):
        """A method to define type of movement"""
        return "A car moves by driving"

class Boat():
    """Boat movement"""
    def move(self):
        """A method to define type of movement"""
        return "A boat moves by sailing"

class Airplane():
    """Airplane movement"""
    def move(self):
        """A method to define type of movement"""
        return "An airplane moves by flying"

class Train():
    """Train movement"""
    def move(self):
        """A method to define type of movement"""
        return "A train moves by chugging"

for vehicle in (Car(), Boat(), Airplane(), Train()):
    print(vehicle.move())
