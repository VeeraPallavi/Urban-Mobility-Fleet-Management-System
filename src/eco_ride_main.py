from vehicle import *
from fleet_manager import FleetManager


class EcoRideMain:
    def main(self):
        print("Welcome to Eco-Ride Urban Mobility System")

        fleet_manager = FleetManager()
        
        while True:

            choice = input ("Enter choice: ")

            if choice == "1":
                hub_name = input("Enter hub name : ")
                fleet_manager.add_hub(hub_name)
            
            elif choice == "2":
                hub_name = input("Enter hub name : ")
                vehicle_type = input("Enter Vehicle(Car/Scooter) : ")

                vehicle_id = input("Enter Vehicle ID: ")
                model = input("Enter Model Name: ")
                battery = int(input("Enter Battery Percentage: "))
                
                if vehicle_type == "ElectricCar":
                    seating_capacity = int(input("Enter maximum seating Capaicty"))
                    vehicle = ElectricCar(vehicle_id, model, battery, seating_capacity)
                    fleet_manager.add_vehicle_to_hub(hub_name, vehicle)
    
                elif vehicle_type == "ElectricScooter":
                    max_speed_limit = int(input("Enter Maximum Speed Limit"))
                    Vehicle = ElectricScooter(vehicle_id, model, battery, max_speed_limit)
                    fleet_manager.add_vehicle_to_hub(hub_name, vehicle)
                
                else:
                    print("Invalid Vehicle Type")

            elif choice == "3":
                hub_name = input("Enter hub name : ")

                vehicles = fleet_manager.get_vehicles_by_hub(hub_name)

                if not vehicles:
                    print("Vehicles not found or hub does not exist")
                else:
                    print(f"\nVehicles in {hub_name} Hub:")
                    for v in vehicles:
                        print(f"Vehicle id : {v.vehicle_id}")
                        print(f"Model: {v.model}")

            elif choice == "4":
                print("Exiting Eco-Ride System")
                break                
                

if __name__ == "__main__":
    ecoridemain = EcoRideMain()
    ecoridemain.main()