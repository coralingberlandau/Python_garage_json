
from icecream import ic
from helper.json import seve_data_to_json


def add_car(cars):
    cars.append({'NCar': input("Name car:"), 'Model': input("Model car:"), 'Color': input("Color car:"), 'UName': input("User name car:")})
    seve_data_to_json('db/cars.json', cars)

def print_data(cars):
    for index,car in enumerate(cars):
        ic(f"({index}) NCar: {car['NCar']}, Model:{car['Model']}, Color:{car['Color']}, UName: {car['UName']} ")
      
def delete_car(cars):
    car_index = find_index_car()
    cars.pop(car_index)
    seve_data_to_json('db/cars.json', cars)

def find_index_car():
    print_data()
    car_index = int(input("please select what you want:"))
    return car_index
    
def update_car(cars):
    car_index = find_index_car()
    cars[car_index] = {'NCar': input("Name car:"), 'Model': input("Model car:"), 'Color': input("Color car:"), 'UName': input("User name car:")}
    seve_data_to_json('db/cars.json', cars)

def sum_cars(cars):
    sum_car = len(cars)
    print (f'The total of cars: {sum_car}')
    seve_data_to_json('db/cars.json', cars)