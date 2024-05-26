import json

def restart_data_from_json(filename):
    cars = []
    with open(filename, 'w') as file:
        json.dump(cars, file)

def load_data_from_json(filename):
    try:
        with open(filename, "r") as file:
            content = file.readlines()
        return [line.strip() for line in content]
    except FileNotFoundError:
        print(f"Creates a new file {filename}.")
        return []
    
def seve_data_to_json(filename, cars):
    with open(filename, "w") as file:
        json.dump(cars, file)