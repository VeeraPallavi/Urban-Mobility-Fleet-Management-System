class Vehicle:
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percntage = battery_percentage

    def display(self):
        print(f"Vehicle ID : {self.vehicle_id}")
        print(f"Vehicle Model : {self.model}")
        print(f"Battery Percentage : {self.battery_percntage}")
        