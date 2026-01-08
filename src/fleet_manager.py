import csv
from vehicle import ElectricCar, ElectricScooter


class FleetManager:
    def __init__(self):
        self.hubs = {}

    def add_hub(self, hub_name):
        if hub_name not in self.hubs:
            self.hubs[hub_name] = []
        else:
            print(f"Hub '{hub_name}' already exists")

    def add_vehicle_to_hub(self, hub_name, vehicle):
        if hub_name not in self.hubs:
            print(f"Hub '{hub_name}' does not exist")
            return

        duplicates = [v for v in self.hubs[hub_name] if v == vehicle]

        if duplicates:
            print(f"Duplicate Vehicle ID '{vehicle.vehicle_id}' not allowed in hub '{hub_name}'")
            return

        self.hubs[hub_name].append(vehicle)
    
    def search_by_hub(self, hub_name):
        return self.hubs.get(hub_name, [])
    
    def search_by_percentage(self, battery):
        for hub, vehicles in self.hubs.items():
            vehicle = list(filter(lambda v : v.get_battery_percentage() > battery, vehicles))
            found = False 
            for v in vehicle:
                if not found :
                    print(f" Vehicle with battery percentage > 80 found in hub {hub}")
                    found = True
                    print(f"Vehicle id : {v.vehicle_id}")
                    print(f"Model: {v.model}")
                    print(f"Battery Percentage : {v.get_battery_percentage()}")

            if not found:
                print("Vehicle not found")
    def catogarize_vehicles(self):
        category = {}
        for vehicles in self.hubs.values():
            for vehicle in vehicles:
                vehicle_type = type(vehicle).__name__
                if vehicle_type not in category:
                    category[vehicle_type] = []
             
                category[vehicle_type].append(vehicle)
        return category
    
    def count_status(self):
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
        vehicles = self.hubs.get(hub_name, [])

        return sorted(vehicles, key = lambda v : v.model)
    
    def sort_by_battery_percentage(self, hub_name):
        vehicles = self.hubs.get(hub_name, [])

        return sorted(vehicles, key = lambda v : v.get_battery_percentage(), reverse = True)
    
    def sort_by_rental_price(self, hub_name):
        vehicles = self.hubs.get(hub_name, [])

        return sorted(vehicles, key = lambda v : v.get_rental_price(), reverse = True)
    
    def save_to_csv_file(self, filename):
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
        
        with open(filename, "r", newline = "") as file:
            read = csv.DictReader(file)
            for line in read:
                hub = line["Hub"]
                vehicle_type = line["Vehicle Type"]
                vehicle_id = line["Vehicle ID"]
                model = line["Model"]
                battery_percentage = int(line["Battery Percentage"])
                maintenance_status = line["Maintananence Status"]
                rental_price = line["Rental Price"]
                value = line["Seating Capacity / Maximum Speed Limit"]

                if hub not in self.hubs:
                    self.hubs[hub] = []
            
                if vehicle_type == "ElectricCar":
                    vehicle = ElectricCar(vehicle_id, model, battery_percentage, value)
                    
            
                elif vehicle_type == "ElectricScooter":
                    vehicle = ElectricScooter(vehicle_id, model, battery_percentage, value)
                
                vehicle.set_maintenance_status(maintenance_status)
                vehicle.set_rental_price(rental_price)
                self.hubs[hub].append(vehicle)

                
