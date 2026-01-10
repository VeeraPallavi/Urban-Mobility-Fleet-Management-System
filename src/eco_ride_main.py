from vehicle import *
from fleet_manager import FleetManager


class EcoRideMain:

    """
    This class provides a menu-driven interface that allows users to:
    - Add hubs
    - Add electric vehicles to hubs
    - Search and filter vehicles
    - Sort vehicles by different attributes
    - Save and load vehicle data using CSV and JSON files
    """

    def main(self):

        """
        Displays a menu repeatedly and performs operations based on user input.
        The method continues execution until the user chooses to exit.
        """
         
        print("Welcome to Eco-Ride Urban Mobility System")

        fleet_manager = FleetManager()
        
        while True:

            print("1. Add Hub")
            print("2. Add Vehicle to hub")
            print("3. search vehicles by hub")
            print("4. Seach by battery_percentage")
            print("5. Cataogerize vehicles")
            print("6. Count_status")
            print("7. Sort by model")
            print("8. Sort by Battery Percentage / Rental Price")
            print("9. Save data to csv file")
            print("10. Load from csv file")
            print("11. Save data to json File")
            print("12. Load data from json File")
            print("13. Exit")
            
            choice = input ("Enter choice: ")

            if choice == "1":
                hub_name = input("Enter hub name : ")
                fleet_manager.add_hub(hub_name)
            
            elif choice == "2":
                hub_name = input("Enter hub name : ")
                vehicle_type = input("Enter Vehicle(ElectricCar/ElectricScooter) : ")

                vehicle_id = input("Enter Vehicle ID: ")
                model = input("Enter Model Name: ")
                battery = int(input("Enter Battery Percentage: "))
                
                if vehicle_type == "ElectricCar":
                    seating_capacity = int(input("Enter maximum seating Capaicty: "))
                    vehicle = ElectricCar(vehicle_id, model, battery, seating_capacity)
    
                elif vehicle_type == "ElectricScooter":
                    max_speed_limit = int(input("Enter Maximum Speed Limit: "))
                    vehicle = ElectricScooter(vehicle_id, model, battery, max_speed_limit)
                
                else:
                    print("Invalid Vehicle Type")
                
                maintan_status = ["Available", "On Trip", "Under Maintanence"]
                status = input("Enter Maintanence Status :")
                if status not in  maintan_status:
                    print("Invalid Status... Default status Avaliable is assigned")
                    vehicle.set_maintenance_status("Available")
                else:
                    vehicle.set_maintenance_status(status)
                price = int(input("Enter Rental Price: "))
                vehicle.set_rental_price(price)
                fleet_manager.add_vehicle_to_hub(hub_name, vehicle)

            elif choice == "3":
                hub_name = input("Enter hub name: ")

                vehicles = fleet_manager.search_by_hub(hub_name)

                if not vehicles:
                    print("Vehicles not found or hub does not exist")
                else:
                    print(f"\nVehicles in {hub_name} Hub:")
                    for v in vehicles:
                        print(f"Vehicle id : {v.vehicle_id}")
                        print(f"Model: {v.model}")
                        print(f"Battery Percentage : {v.get_battery_percentage()}")
                        print(f"Maintanence Status : {v.get_maintenance_status()}")
                        print(f"Rental Price : {v.get_rental_price()}")
            
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
                hub_name = input("Enter hub name : ")
                vehicles = fleet_manager.sort_by_model(hub_name)

                if not vehicles:
                    print("Vehicle not found or hub does not exist ")
                for v in vehicles:
                    print(v)

            elif choice == "8":
                hub_name = input("Enter hub name: ")
                print("1.Sort based on battery Percentage ")
                print("2.Sort based on rental price")
                print("3.Exit")

                ch = input("Enter your choice to sort : ")

                if ch == "1":
                    vehicles = fleet_manager.sort_by_battery_percentage(hub_name)
                    if not vehicles:
                        print("Vehicle not found or hub does not exist ")
                    print ("Vehicles sorted based on battery Percenatge ")
                    for v in vehicles:
                        print(v)
                
                elif ch == "2":
                    vehicles = fleet_manager.sort_by_rental_price(hub_name)
                    if not vehicles:
                        print("Vehicle no found or hub does not exist")
                    print("Vehicles Sorted based on rental price ")
                    for v in vehicles :
                        print(v)

                elif ch == "3":
                    print("Exit")
                    break
                else :
                    print("Please Enter valid choice ")

            elif choice == "9":
                filename = input("Enter File name :")
                fleet_manager.save_to_csv_file(filename)
            
            elif choice == "10":
                filename = input("Enter File Name : ")
                try :
                    fleet_manager.load_from_csv(filename)
                    print("Data loaded Successfully")
                except FileNotFoundError :
                    print("Invalid filename...Please enter correct filename")
                
            elif choice == "11":
                filename = input("Enter File name : ")
                fleet_manager.save_data_to_json_file(filename)
            
            elif choice == "12":
                filename = input("Enter File name : ")
                fleet_manager.load_from_json_file(filename)
                print("Data loaded successfully loaded from json file")

            elif choice == "13":
                print("Exit")
                break                
                

if __name__ == "__main__":
    ecoridemain = EcoRideMain()
    ecoridemain.main()