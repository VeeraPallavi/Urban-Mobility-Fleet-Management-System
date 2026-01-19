import csv
import json
from src.vehicle import ElectricCar, ElectricScooter


class FleetManager:
    def __init__(self):

        """
        Initializes the FleetManager with an empty dictionary of hubs.
        Each hub maps to a list of vehicles.
        """
        self.hubs = {}

    def add_hub(self, hub_name):

        """
        Adds a new hub to the fleet system.

        :param hub_name: Name of the hub to be added
        """
        if hub_name not in self.hubs:
            self.hubs[hub_name] = []
        else:
            print(f"Hub '{hub_name}' already exists")

    def add_vehicle_to_hub(self, hub_name, vehicle):

        """
        Adds a vehicle to a specific hub after checking for duplicates.

        Duplicate vehicles are identified using the vehicle ID.

        :param hub_name: Name of the hub
        :param vehicle: ElectricCar or ElectricScooter object
        """
        if hub_name not in self.hubs:
            print(f"Hub '{hub_name}' does not exist")
            return

        duplicates = [v for v in self.hubs[hub_name] if v == vehicle]

        if duplicates:
            print(f"Duplicate Vehicle ID '{vehicle.vehicle_id}' not allowed in hub '{hub_name}'")
            return

        self.hubs[hub_name].append(vehicle)
    
    def search_by_hub(self, hub_name):

        """
        Retrieves all vehicles present in a given hub.

        :param hub_name: Name of the hub
        :return: List of vehicles in the hub
        """
        return self.hubs.get(hub_name, [])
    
    def search_by_percentage(self, battery):
        """Returns vehicles with battery percentage
           greater than the specified value across all hubs.
        """
        result = []

        for vehicles in self.hubs.values():
            result.extend(filter(lambda v: v.get_battery_percentage() > battery, vehicles))
        
        return result
    
    def catogarize_vehicles(self):

        """
        Categorizes vehicles based on their type.

        :return: Dictionary with vehicle type as key and list of vehicles as value
        """
        category = {}
        for vehicles in self.hubs.values():
            for vehicle in vehicles:
                vehicle_type = type(vehicle).__name__
                if vehicle_type not in category:
                    category[vehicle_type] = []
             
                category[vehicle_type].append(vehicle)
        return category
    
    def count_status(self):

        """
        Counts vehicles based on their maintenance status.

        :return: Dictionary containing maintenance status counts
        """
        status = {
            'Available' : 0,
            'On Trip' : 0, 
            'Under Maintainence' : 0
        }

        for vehicles in self.hubs.values():
            for vehicle in vehicles :
                maintenance_status = vehicle.get_maintenance_status()
                if maintenance_status in status:
                    status[maintenance_status] += 1
                
        return status
    
    def sort_by_model(self, hub_name):

        """
        Sorts vehicles in a hub by model name (ascending).

        :param hub_name: Name of the hub
        :return: Sorted list of vehicles
        """
        vehicles = self.hubs.get(hub_name, [])

        return sorted(vehicles, key = lambda v : v.model)
    
    def sort_by_battery_percentage(self, hub_name):

        """
        Sorts vehicles in a hub by battery percentage (descending).

        :param hub_name: Name of the hub
        :return: Sorted list of vehicles
        """
        vehicles = self.hubs.get(hub_name, [])

        return sorted(vehicles, key = lambda v : v.get_battery_percentage(), reverse = True)
    
    def sort_by_rental_price(self, hub_name):

        """
        Sorts vehicles in a hub by rental price (descending).

        :param hub_name: Name of the hub
        :return: Sorted list of vehicles
        """
        vehicles = self.hubs.get(hub_name, [])

        return sorted(vehicles, key = lambda v : v.get_rental_price(), reverse = True)
    
    def save_to_csv_file(self, filename):
         
        """
        Saves all fleet data to a CSV file.

        :param filename: Name of the CSV file
        """
        with open(filename, "w", newline = "") as file:
            write = csv.writer(file)

            write.writerow([
                "Hub", 
                "Vehicle Type",
                "Vehicle ID",
                "Model",
                "Battery Percentage",
                "Maintananence Status",
                "Rental Price",
                "Seating Capacity / Maximum Speed Limit"
            ])
            for hub, vehicles in self.hubs.items():
                for vehicle in vehicles:
                    if isinstance(vehicle, ElectricCar):
                        value = vehicle.seating_capacity
                    else:
                        value = vehicle.max_speed_limit

                    write.writerow([
                        hub,
                        vehicle.__class__.__name__,
                        vehicle.vehicle_id,
                        vehicle.model,
                        vehicle.get_battery_percentage(),
                        vehicle.get_maintenance_status(),
                        vehicle.get_rental_price(),
                        value
                    ])        
    
    def load_from_csv(self, filename):
        
        """
        Loads fleet data from a CSV file.

        :param filename: Name of the CSV file
        """
        with open(filename, "r", newline = "") as file:
            read = csv.DictReader(file)
            for line in read:
                hub = line["Hub"]
                vehicle_type = line["Vehicle Type"]
                vehicle_id = line["Vehicle ID"]
                model = line["Model"]
                battery_percentage = int(line["Battery Percentage"])
                maintenance_status = line["Maintananence Status"]
                rental_price = (line["Rental Price"])
                value = line["Seating Capacity / Maximum Speed Limit"]

                if hub not in self.hubs:
                    self.hubs[hub] = []
            
                if vehicle_type == "ElectricCar":
                    vehicle = ElectricCar(vehicle_id, model, battery_percentage, value)
                    
            
                elif vehicle_type == "ElectricScooter":
                    vehicle = ElectricScooter(vehicle_id, model, battery_percentage, value)
                
                vehicle.set_maintenance_status(maintenance_status)
                vehicle.set_rental_price(int(rental_price))
                self.hubs[hub].append(vehicle)
    
    def save_data_to_json_file(self, filename):

        """
        Saves fleet data to a JSON file.

        :param filename: Name of the JSON file
        """
        data = {}
        for hub, vehicles in self.hubs.items():
            data[hub] = []
            for vehicle in vehicles:
                vehicle_data = {
                "vehicle_type": vehicle.__class__.__name__,
                "vehicle_id": vehicle.vehicle_id,
                "model": vehicle.model,
                "battery_percentage": vehicle.get_battery_percentage(),
                "maintenance_status": vehicle.get_maintenance_status(),
                "rental_price": vehicle.get_rental_price()
            }

                if isinstance(vehicle, ElectricCar):
                    vehicle_data["seating_capacity"] = vehicle.seating_capacity
                else:
                    vehicle_data["max_speed_limit"] = vehicle.max_speed_limit

                data[hub].append(vehicle_data)
        
        with open(filename, "w") as json_file:
            json.dump(data, json_file, indent = 4)
    
    def load_from_json_file(self, filename):
        
        """
        Loads fleet data from a JSON file.

        :param filename: Name of the JSON file
        """
        with open(filename, "r") as file:
            data = json.load(file)

        for hub, vehicles in data.items():
            if hub not in self.hubs:
                self.hubs[hub] = []

            for v in vehicles:
                if v["vehicle_type"] == "ElectricCar":
                    vehicle = ElectricCar(
                        v["vehicle_id"],
                        v["model"],
                        v["seating_capacity"],
                        int(v["battery_percentage"])
                    )

                elif v["vehicle_type"] == "ElectricScooter":
                    vehicle = ElectricScooter(
                        v["vehicle_id"],
                        v["model"],
                        v["max_speed_limit"],
                        int(v["battery_percentage"])
                    )

                vehicle.set_maintenance_status(v["maintenance_status"])
                vehicle.set_rental_price(int(v["rental_price"]))
                
                self.hubs[hub].append(vehicle)
