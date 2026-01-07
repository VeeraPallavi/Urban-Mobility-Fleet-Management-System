from vehicle import Vehicle, ElectricCar, ElectricScooter

class EcoRideMain:
    def main(self):
        print("Welcome to Eco-Ride Urban Mobility System")
        car = ElectricCar("EV101", "Tesla", 80, 5)
        scooter = ElectricScooter("EV1001", "JAWA", 60, 100)
        
        vehicles = [car, scooter]
        for vehicle in vehicles:
            self.cost = vehicle.calculate_trip_cost(10)
            print(f"{vehicle.model} Total trip cost : {self.cost}")


if __name__ == "__main__":
    ecoridemain = EcoRideMain()
    ecoridemain.main()