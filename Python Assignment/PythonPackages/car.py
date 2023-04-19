# car.py
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start(self):
        print(f"Starting the {self.make} {self.model}...")