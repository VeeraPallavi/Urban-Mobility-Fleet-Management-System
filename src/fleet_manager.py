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
        
        duplicate_vehicles = [v for v in self.hubs[hub_name] if v == vehicle]

        if duplicate_vehicles:
            print("Duplicate Veicle id found ")
            return 
        
        self.hubs[hub_name].append(vehicle)

    def get_vehicles_by_hub(self, hub_name):
        return self.hubs.get(hub_name, [])