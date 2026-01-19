import pytest
import os

from src.vehicle import ElectricCar, ElectricScooter
from src.fleet_manager import FleetManager


@pytest.fixture
def fleet():
    fm = FleetManager()

    hubs = ["Downtown", "Airport"]
    for hub in hubs:
        fm.add_hub(hub)

    car1 = ElectricCar("101", "Tesla", 89, 5)
    scooter1 = ElectricScooter("201", "GT650", 76, 90)

    fm.add_vehicle_to_hub("Downtown", car1)
    fm.add_vehicle_to_hub("Airport", scooter1)

    return fm, car1, scooter1


def test_add_hub(fleet):
    fm = fleet[0]
    assert "Downtown" in fm.hubs

def test_search_by_hub(fleet):
    
    fm = fleet[0]
    vehicles = fm.search_by_hub("Airport")
    assert len(vehicles) == 1

def test_search_by_battery_percentage(fleet):
    
    fm, car1, *_ = fleet

    battery = 80
    result = fm.search_by_percentage(battery)

    assert car1 in result
    for v in result:
        assert v.get_battery_percentage() > 80

def test_catogarize_vehicles(fleet):
    fm, car1, scooter1 = fleet
    categories = fm.catogarize_vehicles()

    assert car1 in categories["ElectricCar"]
    assert scooter1 in categories["ElectricScooter"]

def test_count_status(fleet):
    
    fm, car1, scooter1 = fleet
    car1.set_maintenance_status("On Trip")
    scooter1.set_maintenance_status("Available")

    status = fm.count_status()
    assert status["On Trip"] == 1
    assert status["Available"] == 1

def test_sort_by_model(fleet):
    
    fm = fleet[0]
    fm.sort_by_model("Downtown")

    models = [v.model for v in fm.hubs["Downtown"]]
    assert models == sorted(models)

def test_sort_by_battery_percentage(fleet):
    
    fm = fleet[0]
    sorted_list = fm.sort_by_battery_percentage("Airport")

    batteries = [v.get_battery_percentage() for v in sorted_list]
    assert batteries == sorted(batteries, reverse=True)

def test_sort_by_rental_price(fleet):
    
    fm = fleet[0]
    sorted_list = fm.sort_by_rental_price("Downtown")

    prices = [v.get_rental_price() for v in sorted_list]
    assert prices == sorted(prices, reverse=True)


def test_save_csv(fleet, tmp_path):

    fm =fleet[0]
    file_name = tmp_path / "data.csv"
    fm.save_to_csv_file(file_name)
    assert os.path.exists(file_name) == True

def test_load_csv(fleet):
    fm = fleet[0]

    fm.load_from_csv("data_hub.csv")

    assert "Airport" in fm.hubs
    assert "Downtown" in fm.hubs

def test_save_data_to_json_file(fleet,tmp_path):

    fm = fleet[0]
    file_name=tmp_path/"data_hub.json"
    fm.save_data_to_json_file(file_name)
    assert os.path.exists(file_name)==True

def test_load_json(fleet):

    fm = fleet[0]
    fm.load_from_json_file("data.json")

    assert "Airport" in fm.hubs
    assert "Mall" not in fm.hubs