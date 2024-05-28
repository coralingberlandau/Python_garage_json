"""
data structure
cars = {'NCar': 'polo', 'Model': '2024', 'Color': 'black', 'UName': 'coral'}
"""

from enum import Enum
import json
from helper.json import load_data_from_json, seve_data_to_json,restart_data_from_json 
from helper.helpers import add_car, print_data, delete_car, find_index_car, update_car, sum_cars

cars = []

class Menu(Enum):
    ADD = 1
    PRINT = 2
    DELETE = 3
    UPDATE = 4
    SUM = 5
    RESTART = 6
    EXIT =7

def display_menu():
    for men in Menu: print (f'{men.value} - {men.name}')
    return Menu (int(input("please enter what you need:")))

if __name__ == "__main__":
            cars = load_data_from_json('db/cars.json')
            while True:
                try: 
                    select_user = display_menu()
                    if select_user == Menu.ADD: add_car(cars)
                    if select_user == Menu.PRINT: print_data(cars)
                    if select_user == Menu.DELETE: delete_car(cars)
                    if select_user == Menu.UPDATE: update_car(cars)
                    if select_user == Menu.SUM: sum_cars(cars)
                    if select_user == Menu.RESTART: restart_data_from_json('db/cars.json')
                    if select_user == Menu.EXIT:
                        seve_data_to_json('db/cars.json', cars)
                        exit()
                except Exception as e:
                    print("Error:", e)
                    print("Recharge")
