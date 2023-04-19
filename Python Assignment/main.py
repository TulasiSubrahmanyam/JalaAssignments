# main.py
from PythonPackages import Car, Driver


car = Car("Toyota", "Camry", 2021)
driver = Driver("John Doe", 35)

car.start()
driver.drive(car)
