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
    

