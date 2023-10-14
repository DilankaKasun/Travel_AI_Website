
import openai
# import booking
from apps.chat.api.config import * 
from apps.chat.api.jsonHandle import Handle
from apps.chat.api.Map import *
from apps.chat.api.proccesHandle import proccesHandle
import json



class AI_handle_data():
    
    def main_error_data(self):
      storege = Handle()
      req_use=storege.user_data_create(" \n \n It is not possible to provide trivel information because the time taken to access the data is very high")
      storege.join(req_use)
    
    def sub_error_data(self):
      storege = proccesHandle()
      req_use=storege.user_data_create("\n \n  It is not possible to provide trivel information because the time taken to access the data is very high")
      storege.join(req_use)
    
    
    def format_dictionary_as_string(self,data):
      data_str = json.dumps(data, indent=4)
      return data_str

    def user_promt(self,use_data):
       storege = Handle()
       req_use=storege.user_data_create(use_data)
       storege.join(req_use)
    
    def user_sub_promt(self,use_data):
       storege = proccesHandle()
       req_use=storege.user_data_create(use_data)
       storege.join(req_use)

    def AI_promt(self,use_data):
       storege = Handle()
       data=storege.AI_promt(use_data)
       storege.join(data)

    def AI_sub_promt(self,use_data):
       storege = proccesHandle()
       data=storege.AI_promt(use_data)
       storege.join(data)

    def AI_system(self,data):
       storege = Handle()
       req_use=storege.user_data_create(data)
       storege.join(req_use)

    def main_continue_required(self):
      storege = Handle()
      req_use=storege.user_data_create("continue")
      storege.join(req_use)
    
    def sub_continue_required(self):
      storege = proccesHandle()
      req_use=storege.user_data_create("continue")
      storege.join(req_use)

    def main_continue_required_AI(self,data):
      req_promt = Handle()
      data_=req_promt.AI_finish_reason(data)
      req_promt.join(data=data_)
    
    def sub_continue_required_AI(self,data):
      req_promt = proccesHandle()
      data_=req_promt.AI_finish_reason(data)
      req_promt.join(data=data_)
    
    def required_data(self):
      req = []
      storege= Handle()
      data =  storege.read()
      for key, value in data.items():
        req.append(data[key])
      return req
    
    def required_sub_data(self):
      req = []
      storege= proccesHandle()
      data =  storege.read()
      for key, value in data.items():
        req.append(data[key])
      return req
    
    def read_data(self):
      storege= proccesHandle()
      data =  storege.read()
      return data
       
    

    def convert_values_to_int(data, keys_to_convert):
      result = data.copy()  # Create a copy of the input dictionary to avoid modifying the original
      for key in keys_to_convert:
          if key in result:
              try:
                  result[key] = int(result[key])
              except ValueError:
                  print(f"Error: Unable to convert '{key}' value to an integer.")
      return result
    
    def delete_keys_from_dict(self,input_dict, keys_to_delete):
      # Create a copy of the input dictionary to avoid modifying the original
      result_dict = input_dict.copy()
      storege = proccesHandle()
      for key in keys_to_delete:
          if key in result_dict:
              del result_dict[key]
      
      storege.write(result_dict)


    def print_json_structure(self, data):
          if not data:
              print("Input JSON string is empty.")
              return
          try:
            json_data_ = json.loads(data) 

          except Exception as e:
             data_list = []
             data=self.read_data()
             last_key = list(data.keys())[-1]
             for x in range(int(last_key)-3,int(last_key)+1):
                
                data_list.append(str(x))
             print(data_list)
             self.delete_keys_from_dict(input_dict=data,keys_to_delete=data_list)
            
            
          MAP_API = []
          mapData = API_DATA()
          try:
           for key, value in json_data_.items():
              if isinstance(value, dict):  # Check if 'value' is a dictionary
                  for sub_1_key, sub_1_value in value.items():
                      if isinstance(sub_1_value, dict):  # Check if 'sub_1_value' is a dictionary
                          for sub_2_key, sub_2_value in sub_1_value.items():
        
                              if mapData.run(main=sub_1_key, sub=sub_2_key, par=sub_2_value):
                                API_MAP=mapData.respons_(main=sub_1_key, sub=sub_2_key, par=sub_2_value)
                                MAP_API.append(API_MAP)
                      else:
                          # return MAP_API 
                          print(f"Value for '{sub_1_key}' is not a dictionary.")
              else:
                  # return MAP_API 
                  print(f"Value for '{key}' is not a dictionary.")
           return MAP_API 
          except Exception as e:
            return MAP_API
       
          
                            
      
    
    def select_function(self, _asssistan):
      return self.print_json_structure(data=_asssistan)




        
class AI_required(AI_handle_data):
    
    def main_required(self,data =None):
      openai.api_key = OpenAi.OPENAI_API_KEY
      if (data == None):
         msg=self.required_data()
      else:
         msg = data 
      
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
      model="gpt-3.5-turbo-16k-0613",
      messages=data_msg,
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["Input-format inputs are received using helper_text_output and user_text_output. output assistant_text_output Returns output in the output-format Given the output, here the input-format takes care of assistant_text_output and user_text_output inputs, and the output-format API part provides the perform the write based on the input-format data."]
      )
      return response['choices'][0]


class AI_response(AI_required,AI_handle_data):
    def finish_reason(self,req_data):
      temp = []
      try:
        temp.append(req_data["message"]["content"])
        req_1=self.main_required()
        self.main_continue_required()
        system_run_count = 1
        while (req_1['finish_reason']!="stop"):
          req_1=self.main_required()
          temp.append(req_1["message"]["content"])
          self.main_continue_required()
          print(req_1['finish_reason'])
          system_run_count+=1

          if req_1['finish_reason'] == "stop":
            break
          elif (system_run_count>2):
            self.main_error_data()
        tot_data = ''
        for temp_x in temp: 
          tot_data +=temp_x
        self.main_continue_required_AI(tot_data)
      except Exception as e:
         
         if req_data:
          temp.append(req_data["user_text_output"])
          req_1=self.sub_required()
          temp.append(req_data["user_text_output"])
          req_1=self.sub_required()
          self.sub_continue_required()
          while (req_1['finish_reason']!="stop"):
            req_1=self.sub_required()
            temp.append(req_1["user_text_output"])
            self.sub_continue_required()
            if req_1['finish_reason'] == "stop":
              break
            # elif (system_run_count>2):
              # self.sub_error_data()
          tot_data = ''
          for temp_x in temp: 
            tot_data +=temp_x
          self.sub_continue_required_AI(tot_data)
         else :
          raise e
      

    def suport_system(self,resp):
      self.user_sub_promt(resp)
      sub_repons=self.sub_required()
      if not sub_repons:
        return {}
      else:  
        temp = []
        if (sub_repons["finish_reason"] != "stop"):
          temp.append(sub_repons["message"]["content"])
          req_1=self.main_required()
          self.sub_continue_required()
          system_run_count = 1
          while (req_1['finish_reason']!="stop"):
            req_1=self.main_required()
            temp.append(req_1["message"]["content"])
            self.sub_continue_required()
            print(req_1['finish_reason'])
            system_run_count+=1

            if req_1['finish_reason'] == "stop":
              break
            
          tot_data = ''
          for temp_x in temp: 
            tot_data +=temp_x
          self.sub_continue_required_AI(tot_data)
        self.AI_sub_promt(use_data=sub_repons['message'])
        API_OUTPUT=self.required_sub_data()[-1]["content"]
        return self.select_function(_asssistan=API_OUTPUT)
            

    
class AI_main(AI_response):
   def run(self,data):
      
      if data :
        output = {}
        input_api ={}
        self.user_promt(use_data=data)
        req_data=self.main_required()
        if (req_data["finish_reason"] != "stop"):
            self.finish_reason(req_data)
            chatdata = self.required_data()[-1]["content"]
            output['chat_data'] = chatdata
            input_api["assistant_text_output"]=chatdata
            input_api["user_text_output"]=data
            output['api_data'] = self.suport_system(self.finish_reason(resp=self.format_dictionary_as_string(input_api)))
            output["user_data"] = data
            return output
           
        else:
           self.AI_promt(use_data=req_data["message"])
           chatdata = self.required_data()[-1]["content"]
           input_api["assistant_text_output"]=chatdata
           input_api["user_text_output"]=data
           output['chat_data'] = chatdata
           output['api_data'] = self.suport_system(resp=self.format_dictionary_as_string(input_api))
           output["user_data"] = data
          #  print(input_api)
           return output
          


 