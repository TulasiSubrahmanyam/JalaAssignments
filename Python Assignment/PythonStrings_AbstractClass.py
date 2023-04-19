from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        print("Starting the vehicle.")
    
    @abstractmethod
    def stop(self):
        print("Stopping the vehicle.")
    
    def get_info(self):
        print(f"This is a {type(self).__name__}.")

class Car(Vehicle):
    def start(self):
        print("Starting the car.")
    
    def stop(self):
        print("Stopping the car.")

car = Car()
car.start()  # Output: "Starting the car."
car.stop()  # Output: "Stopping the car."
car.get_info()  # Output: "This is a Car."
