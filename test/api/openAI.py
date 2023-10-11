import os
import openai
import config
import jsonHandle
import booking
import temp
import proccesHandle
import json
import Map

class AI_handle_data():
    def user_promt(self,use_data):
       storege = jsonHandle.Handle()
       req_use=storege.user_data_create(use_data)
       storege.join(req_use)
    
    def user_sub_promt(self,use_data):
       storege = proccesHandle.proccesHandle()
       req_use=storege.user_data_create(use_data)
       storege.join(req_use)

    def AI_promt(self,use_data):
       storege = jsonHandle.Handle()
       data=storege.AI_promt(use_data)
       storege.join(data)

    def AI_sub_promt(self,use_data):
       storege = proccesHandle.proccesHandle()
       data=storege.AI_promt(use_data)
       storege.join(data)

    def AI_system(self,data):
       storege = jsonHandle.Handle()
       req_use=storege.user_data_create(data)
       storege.join(req_use)

    def continue_required(self):
      storege = jsonHandle.Handle()
      req_use=storege.user_data_create("continue")
      storege.join(req_use)

    def continue_required_AI(self,data):
      req_promt = jsonHandle.Handle()
      data_=req_promt.AI_finish_reason(data)
      req_promt.join(data=data_)
    
    def required_data(self):
      req = []
      storege= jsonHandle.Handle()
      data =  storege.read()
      for key, value in data.items():
        req.append(data[key])
      return req
    
    def required_sub_data(self):
      req = []
      storege= proccesHandle.proccesHandle()
      data =  storege.read()
      for key, value in data.items():
        req.append(data[key])
      return req
    

    def convert_values_to_int(data, keys_to_convert):
      result = data.copy()  # Create a copy of the input dictionary to avoid modifying the original
      for key in keys_to_convert:
          if key in result:
              try:
                  result[key] = int(result[key])
              except ValueError:
                  print(f"Error: Unable to convert '{key}' value to an integer.")
      return result



    def print_json_structure(self, data):
          if not data:
              print("Input JSON string is empty.")
              return
          json_data = json.loads(data)
          MAP_API = []
          mapData = Map.API_DATA()
          for key, value in json_data.items():
              if isinstance(value, dict):  # Check if 'value' is a dictionary
                  for sub_1_key, sub_1_value in value.items():
                      if isinstance(sub_1_value, dict):  # Check if 'sub_1_value' is a dictionary
                          for sub_2_key, sub_2_value in sub_1_value.items():
        
                              if mapData.run(main=sub_1_key, sub=sub_2_key, par=sub_2_value):
                                API_MAP=mapData.respons_(main=sub_1_key, sub=sub_2_key, par=sub_2_value)
                                MAP_API.append(API_MAP)
                      else:
                          print(f"Value for '{sub_1_key}' is not a dictionary.")
              else:
                  print(f"Value for '{key}' is not a dictionary.")
          return MAP_API
                            
      
    
    def select_function(self, _asssistan):
      return self.print_json_structure(data=_asssistan)




        
class AI_required(AI_handle_data):
    
    def main_required(self):
      openai.api_key = config.OpenAi.OPENAI_API_KEY
      msg=self.required_data()
      
      response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo-16k",
      messages=msg,
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["Do not make too long descriptions in the conversation between the assistant and the user. If the user understands the fact that he needs to explain in detail, then explain in detail"]

      )
      return response['choices'][0]

    def sub_required(self):
      data_msg=self.required_sub_data()
      response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=data_msg,
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
      )
      return response['choices'][0]


class AI_response(AI_required,AI_handle_data):
    def finish_reason(self,req_data):
      temp = []
      try:
        temp.append(req_data["message"]["content"])
      except Exception as e:
         temp.append(req_data)
        
      req_1=self.main_required()
      self.continue_required()
      while (req_1['finish_reason']!="stop"):
        req_1=self.main_required()
        temp.append(req_1["message"]["content"])
        self.continue_required()
        if req_1['finish_reason'] == "stop":
           break
      tot_data = ''
      for temp_x in temp: 
        tot_data +=temp_x
      self.continue_required_AI(tot_data)

    def suport_system(self,resp):
      API = booking.API()
      self.user_sub_promt(resp)
      sub_repons=self.sub_required()
      if sub_repons!={}:
        if (sub_repons["finish_reason"] != "stop"):
          self.finish_reason(sub_repons)
          self.AI_sub_promt(use_data=sub_repons['message'])
          API_OUTPUT=self.required_sub_data()[-1]["content"]
          
          return self.select_function(_asssistan=API_OUTPUT)
        else:
          self.AI_sub_promt(use_data=sub_repons['message'])
          API_OUTPUT=self.required_sub_data()[-1]["content"]
          
          return self.select_function(_asssistan=API_OUTPUT)
             

    
class AI_main(AI_response):
   def run(self,data):
      if data :
     
        self.user_promt(use_data=data)
        req_data=self.main_required()
        if (req_data["finish_reason"] != "stop"):
            self.finish_reason(req_data)
            self.required_data()[-1]["content"]
            self.suport_system(self.finish_reason(data))
            return self.required_data()[-1]["content"],self.suport_system(self.finish_reason(data))
           
        else:
           self.AI_promt(use_data=req_data["message"])
           self.required_data()[-1]["content"]
           self.suport_system(data)
           return  self.required_data()[-1]["content"],self.suport_system(data)
   


 