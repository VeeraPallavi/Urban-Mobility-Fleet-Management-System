from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_id, model, battery_percentage):

        """
        Initializes a Vehicle object.

        :param vehicle_id: Unique ID of the vehicle
        :param model: Model name
        :param battery_percentage: Initial battery percentage
        """
        self.vehicle_id = vehicle_id
        self.model = model
        self.__battery_percentage = 0
        self.__maintenance_status = None
        self.__rental_price = None 

        self.set_battery_percentage(battery_percentage)

    def get_battery_percentage(self):

        """
        Returns the current battery percentage.

        :return: Battery percentage
        """
        return self.__battery_percentage
    
    def set_battery_percentage(self, battery_percentage):

        """
        Sets the battery percentage if it is within valid range (0–100).

        :param battery_percentage: Battery percentage to set
        """
        if 0 <= battery_percentage <= 100:
            self.__battery_percentage = battery_percentage
        else:
            print("Invalid battery Percentage . Enter valid percentage...")

    def get_rental_price(self):

        """
        Returns the rental price of the vehicle.

        :return: Rental price
        """
        return self.__rental_price
    
    def set_rental_price(self, rental_price):

        """
        Sets the rental price for the vehicle.

        :param rental_price: Rental price value
        """
        if rental_price < 0:
            print("Rental Price should be positive")
        self.__rental_price = rental_price
    
    def get_maintenance_status(self):

        """
        Returns the maintenance status of the vehicle.

        :return: Maintenance status
        """
        return self.__maintenance_status
    
    def set_maintenance_status(self, maintenance_status):

        """
        Sets the maintenance status of the vehicle.

        :param maintenance_status: Status (Available, On Trip, Under Maintenance)
        """
        self.__maintenance_status = maintenance_status

    @abstractmethod
    def calculate_trip_cost(self, distance):

        """
        Calculates the trip cost based on distance.

        Must be implemented by all subclasses.

        :param distance: Distance traveled
        :return: Trip cost
        """

        pass

    def __eq__(self, other):
        
        """
        Compares two vehicles based on their vehicle ID.

        :param other: Another vehicle object
        :return: True if vehicle IDs match, else False
        """
        if not isinstance(other, Vehicle):
            return False
        return self.vehicle_id == other.vehicle_id
    
    def display(self):
        print(f"Vehicle Id : {self.vehicle_id}")
        print(f"Model : {self.model}")
        print(f"Battery Percentage : {self.__battery_percentage}%")

    def __str__(self):

        """
        Returns a string representation of the vehicle.

        :return: Formatted vehicle details
        """
        return f"Vehicle ID : {self.vehicle_id} \nModel : {self.model}\nBattery_percentage : {self.__battery_percentage}%"
    

class ElectricCar(Vehicle):

    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):

        """
        Initializes an ElectricCar object.

        :param vehicle_id: Unique vehicle ID
        :param model: Model name
        :param battery_percentage: Battery level
        :param seating_capacity: Number of seats
        """
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity

    def calculate_trip_cost(self, distance):

        """
        Calculates trip cost for an electric car.

        :param distance: Distance traveled
        :return: Trip cost
        """
        return 5.0 + (0.50 * distance)

class ElectricScooter(Vehicle):

    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):

        """
        Initializes an ElectricScooter object.

        :param vehicle_id: Unique vehicle ID
        :param model: Model name
        :param battery_percentage: Battery level
        :param max_speed_limit: Maximum speed limit
        """
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit

    def calculate_trip_cost(self, distance):

        """
        Calculates trip cost for an electric scooter.

        :param distance: Distance traveled
        :return: Trip cost
        """
        return 1.0 + (0.15 * distance)

    