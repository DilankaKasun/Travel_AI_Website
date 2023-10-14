import requests
import json
from apps.chat.api.config import * 
class APIfunctoin():
    pass

class query(APIfunctoin):
	params = { }
     
class google_map_business(query):
     def Search(self,query,limit,lat,lng,zoom,region,language='en'):
        pass
        self.params["query"]=query
        self.params["limit"]=limit
        self.params["lat"]=lat
        self.params["lng"]=lng
        self.params["zoom"]=zoom
        self.params["language"]=language
        self.params["region"]=region

     def Search_In_Area(self,query,limit,lat,lng,zoom,region,language='en'):
        pass
        self.params["query"]=query
        self.params["limit"]=limit
        self.params["lat"]=lat
        self.params["lng"]=lng
        self.params["zoom"]=zoom
        self.params["region"]=region
        self.params["language"]=language


class google_Map_Geocoding(query):
     pass
     def Get_Data_Address(self,address,format='json'): 
        self.params["address"]=address
     

class google_map_routes(query):
    pass
    def FindDrivingRoute(self,stops):
        self.params["stops"]=stops


	

class Datahandel():
	handel = {
		'google_map_business':{
			'Search':{
				'main':'search'
			},
               'Search_In_Area':{
                    'main':'search-in-area'
               }
		},
		'google_Map_Geocoding':{
			'Get_Data_Address':{
				'main':'json',

			}
		},
		'google_map_routes':{
			'FindDrivingRoute':{
				'main':'FindDrivingRoute'
			}
			
			
		}

	}
	def _set(self,mainClass,method):
		 return self.handel[mainClass][method]

	
class queryhandle(google_map_business,google_map_routes,google_Map_Geocoding):
	def queryhandlerun(self,main,sub,paramete={}):
		if (main == "google_map_business"):
			if (sub == "Search"):
				query = paramete['query']
				limit = paramete['limit']
				lat = paramete['lat']
				lng = paramete['lng']
				zoom = paramete['zoom']
				language = paramete['language']
				region = paramete['region']
				self.Search(query=query,limit=limit,lat=lat,lng=lng,zoom=zoom,region=region,language=language)

				
			elif (sub=="Search_In_Area"):
				query = paramete['query']
				limit = paramete['limit']
				lat = paramete['lat']
				lng = paramete['lng']
				zoom = paramete['zoom']
				region = paramete['region']
				language = paramete['language']
				self.Search_In_Area(query=query,limit=limit,lat=lat,lng=lng,zoom=zoom,region=region,language=language)
	
		
		elif( main == "google_Map_Geocoding" ):

			if(sub =="Get_Data_Address"):
				address = paramete['address']
			
				self.Get_Data_Address(address=address)
				

		
		elif(main == "google_map_routes"):
			pass
			if(sub=="FindDrivingRoute"):
				stops=paramete['stops']
				self.FindDrivingRoute(stops=stops)
			
	

class handle(queryhandle,Datahandel):
	def url(self,main,sub):

		config_run = main()
		config_url = Datahandel()
		if (main == "google_map_business"):
			_data=config_url._set(main,sub)
			config_run.google_map_business(dmain=_data['main'])
			return config_run.url,config_run.header
		elif(main == "google_Map_Geocoding"):
			_data=config_url._set(main,sub)
			config_run.google_Map_Geocoding(dmain=_data['main'])
			return config_run.url,config_run.header
		elif(main == "google_map_routes"):
			_data=config_url._set(main,sub)
			config_run.google_map_routes(dmain=_data['main'])
			return config_run.url,config_run.header
		

	def query(self,main,sub,paramete):
		return self.queryhandlerun(main,sub,paramete)


class API_DATA (handle):
	def run(self,main,sub,par):
		handleAPI = handle()
		handleAPI.query(main=main,sub=sub,paramete=par)
		queryAPI = query()
		urlAPI,reqAPI=handleAPI.url(main=main,sub=sub)
		return queryAPI.params,urlAPI[0],reqAPI
    
	def respons_(self, main, sub, par):
		querystring, url, headers = self.run(main=main, sub=sub, par=par)
		# print(querystring, url, headers )
		response = requests.get(url, headers=headers, params=querystring)
		
		if response.status_code == 200:
			try:
				return response.json()
			except json.JSONDecodeError as e:
				print(f"Error decoding JSON: {e}")
				return None
		else:
			print(f"Request failed with status code: {response.status_code}")
			return None

# x = API_DATA()
# print(x.respons_(main="google_map_business",sub="Search_In_Area",par={'query': 'attractions', 'limit': '10', 'lat': '6.032319', 'lng': '80.217050 ', 'zoom': '13','region':'lk','language':'en'}))