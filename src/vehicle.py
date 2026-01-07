from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.__battery_percentage = 0
        self.__maintenance_status = None
        self.__rental_price = None 

        self.set_battery_percentage(battery_percentage)

    def get_battery_percentage(self):
        return self.__battery_percentage
    
    def set_battery_percentage(self, battery_percentage):
        if 0<= battery_percentage <= 100:
            self.__battery_percentage = battery_percentage
        else:
            print("Invalid battery Percentage . Enter valid percentage...")

    def get_rental_price(self):
        return self.__rental_price
    
    def set_rental_price(self, rental_price):
        if rental_price < 0:
            print("Rental Price should be positive")
        self.__rental_price = rental_price
    
    def get_maintenance_status(self):
        return self.__maintenance_status
    
    def set_maintenance_status(self, maintenance_status):
        self.__maintenance_status = maintenance_status

    @abstractmethod
    def calculate_trip_cost(self, distance):
        pass
class ElectriCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, _seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = _seating_capacity
    def calculate_trip_cost(self, distance):
        return 5.0 + (0.50 * distance)

class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit= max_speed_limit

    def calculate_trip_cost(self, distance):
        return 1.0 + (0.15 * distance)

    