import json

class Handle():
    file_name = "chat.json"

    def write(self, data):
        with open(self.file_name, "w") as json_file:
            json.dump(data, json_file, indent=4)

    def join(self, data):
        existing_data = self.read()
        if existing_data is not None:
            existing_data.update(data)
            with open(self.file_name, "w") as json_file:
                json.dump(existing_data, json_file, indent=4)

    def read(self):
        try:
            with open(self.file_name, "r") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            print(f"The file '{self.file_name}' does not exist.")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {str(e)}")
            return None

