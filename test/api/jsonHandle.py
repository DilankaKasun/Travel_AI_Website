import json

class Handle():
    file_name = "chat.json"
    with open(file_name, "w") as json_file:
        def open (self,data,json_file=json_file):    
            json.dump(data, json_file, indent=4)
    
        




