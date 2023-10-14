import json

# Function to load data from the JSON file
def load_data():
    try:
        with open('main.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"ai": {}, "user": {}}
    return data

# Function to save data to the JSON file
def save_data(data):
    with open('main.json', 'w') as file:
        json.dump(data, file, indent=4)

# Function to insert data into the JSON file
def insert_data(category, key, value):
    data = load_data()
    if category in data:
        data[category][key] = value
        save_data(data)
        print(f'Data inserted into {category} category: Key = {key}, Value = {value}')
    else:
        print(f'Category {category} not found.')

# Function to delete data from the JSON file
def delete_data(category, key):
    data = load_data()
    if category in data and key in data[category]:
        del data[category][key]
        save_data(data)
        print(f'Data deleted from {category} category: Key = {key}')
    else:
        print(f'Data not found in category {category}.')

# Function to append data into the JSON file with an automatically assigned numeric key
def append_data(category, value):
    data = load_data()
    if category in data:
        index = len(data[category])
        while str(index) in data[category]:
            index += 1
        data[category][str(index)] = value
        save_data(data)
        print(f'Data appended to {category} category with Key = {index}, Value = {value}')
    else:
        print(f'Category {category} not found.')



        
# Example Usage:
# insert_data("ai", "2", "how are you?")
# # delete_data("user", "0")
# append_data("ai", "I'm doing well.")
