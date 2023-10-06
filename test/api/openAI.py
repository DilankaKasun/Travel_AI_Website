import os
import openai
import config
import jsonHandle
import booking
import temp
import proccesHandle
import json


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
    

    def print_json_structure(self,data):
      try:
          if not data:
              print("Input JSON string is empty.")
              return
          
          json_data = json.loads(data)
          # print(json_data)
          json_out ={}
          json_out_ = {}
          if isinstance(json_data, dict):
              for key, value in json_data.items():
                  if isinstance(value, dict):
                      
                      # print(f"Object Key: {key}")
                      for sub_key, sub_value in value.items():
                          if int(sub_value)>=50: 
                            json_out[sub_key] =sub_value
                            json_out_[key] = json_out 
                  else:
                      if int(value)>=50: 
                            json_out[key] =value
          else:
              print("Invalid JSON structure")
          return json_out_
      except json.JSONDecodeError as e:
          print(f"JSON decoding error: {e}")
      except Exception as e:
          print(f"Error: {e}")
    
    def select_function(self, _asssistan):
      Data = _asssistan['message']['content']
      out_KEY = None
      print(self.print_json_structure(data=Data))




        
class AI_required(AI_handle_data):
    
    def main_required(self):
      openai.api_key = config.OpenAi.OPENAI_API_KEY
      msg=self.required_data()
      
      response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=msg,
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
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
      temp.append(req_data["message"]["content"])
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
       assiten = resp['message']
       if assiten: 
        
        self.user_sub_promt(assiten['content'])
        sub_repons=self.sub_required()
        if sub_repons!={}:
          self.AI_sub_promt(use_data=sub_repons['message'])
          # # print(self.select_function(_asssistan=sub_repons))
          # req_ai_data = self.required_sub_data()[-1]["content"]   
          return self.select_function(_asssistan=sub_repons)
             
             
          
          
    
class AI_main(AI_response):
   def run(self,data):
      if data :
        self.user_promt(use_data=data)
        req_data=self.main_required()
        if (req_data["finish_reason"] != "stop"):
            self.finish_reason(req_data)
            # print(self.required_data()[-1]["content"])
            print(self.suport_system(self.finish_reason(req_data)))
           
        else:
           self.AI_promt(use_data=req_data["message"])
          #  print(self.required_data()[-1]["content"])
           print(self.suport_system(req_data))
   

while (True):
  data = input("Enter Input :")
  x = AI_main()
  x.run(data=data)
# x = AI_response()
# print(x.suport())
 