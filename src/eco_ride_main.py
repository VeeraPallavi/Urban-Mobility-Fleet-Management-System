from vehicle import *
from fleet_manager import FleetManager


class EcoRideMain:
    def main(self):
        print("Welcome to Eco-Ride Urban Mobility System")

        fleet_manager = FleetManager()
        
        while True:

            print("1. Add Hub")
            print("2. Add Vehicle to hub")
            print("3. search vehicles by hub")
            print("4. Seach by battery_percentage")
            print("5. Cataogerize vehicles")
            print("6. Count_status")
            print("7. Exit")
            
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
    
                elif vehicle_type == "ElectricScooter":
                    max_speed_limit = int(input("Enter Maximum Speed Limit"))
                    vehicle = ElectricScooter(vehicle_id, model, battery, max_speed_limit)
                
                else:
                    print("Invalid Vehicle Type")
                
                maintan_status = ["Available", "On Trip", "Under Maintanence"]
                status = input("Enter Maintanence Status :")
                if status not in  maintan_status:
                    print("Invalid Status")
                    vehicle.set_maintenance_status("Available")
        
                vehicle.set_maintenance_status(status)
                fleet_manager.add_vehicle_to_hub(hub_name, vehicle)

            elif choice == "3":
                hub_name = input("Enter hub name : ")

                vehicles = fleet_manager.search_by_hub(hub_name)

                if not vehicles:
                    print("Vehicles not found or hub does not exist")
                else:
                    print(f"\nVehicles in {hub_name} Hub:")
                    for v in vehicles:
                        print(f"Vehicle id : {v.vehicle_id}")
                        print(f"Model: {v.model}")
                        print(f"Battery Percentage : {v.get_battery_percentage()}")
            
            elif choice == "4":
                fleet_manager.search_by_percentage(80)
            
            elif choice == "5":
                category = fleet_manager.catogarize_vehicles()
                if not category:
                    print("No Vehicles found")
                else:
                    for vehicle_type, vehicle in category.items():
                        print(f"{vehicle_type} : ")
                        for v in vehicle:
                            print(f"Vehicle_id : {v.vehicle_id} Vechile_model : {v.model}")
            
            elif choice == "6":
                status = fleet_manager.count_status()
                
                for maintain_status, count in status.items():
                    print(f"{maintain_status} : {count}")

            elif choice == "7":
                print("Exit")
                break                
                

if __name__ == "__main__":
    ecoridemain = EcoRideMain()
    ecoridemain.main()