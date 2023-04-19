from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    def get_info(self):
        print(f"This is a {type(self).__name__}.")

class Car(Vehicle):
    def start(self):
        print("Starting the car.")
    
    def stop(self):
        print("Stopping the car.")

class SportsCar(Car):
    def __init__(self):
        super().__init__()

sports_car = SportsCar()
sports_car.get_info()  # Output: "This is a SportsCar."
