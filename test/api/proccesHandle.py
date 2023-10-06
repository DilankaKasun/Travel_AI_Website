import json

class proccesHandle():
    file_name = "procces.json"

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
        
    def AI_promt(self,data):
        existing_data ={}
        data_ = self.read()
        key_val=0
        for key, value in data_.items():
            key_val=int(key)
        key_val+=1
        existing_data[key_val]=data
        return existing_data
    
    def AI_finish_reason(self,data):
        promt = {}
        existing_data ={}
        data_ = self.read()
        key_val=0
        for key, value in data_.items():
            key_val=int(key)
        key_val+=1
        promt["role"]="assistant"
        promt["content"]=data
        existing_data[key_val]=promt
        return existing_data

    def user_data_create(self,data):
        promt = {}
        existing_data ={}
        data_ = self.read()
        key_val=0
        for key, value in data_.items():
            key_val=int(key)
        key_val+=1
        promt["role"]="user"
        promt["content"]=data
        existing_data[key_val]=promt
        return existing_data
    
    def system_data_create(self,data):
        promt = {}
        existing_data ={}
        data_ = self.read()
        key_val=0
        for key, value in data_.items():
            key_val=int(key)
        key_val+=1
        promt["role"]="system"
        promt["content"]=data
        existing_data[key_val]=promt
        return existing_data
    
    def delete_sub_data(self):
        data_ = self.read()
        key_val=0
        for key, value in data_.items():
            if key:
                print(key)


