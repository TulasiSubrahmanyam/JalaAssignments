# driver.py
class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def drive(self, car):
        print(f"{self.name} is driving a {car.year} {car.make} {car.model}.")