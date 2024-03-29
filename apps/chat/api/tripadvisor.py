import requests

import config


class set_value():
	locale = ["en-gb","en-us","de","nl","fr","es","es-ar","es-mx","ca","it","pt-pt","pt-br","no","fi","sv","da","cs","hu","ro","ja","zh-cn","zh-tw","pl","el","ru","tr","bg","ar","ko","he","lv","uk","id","ms","th","et","hr","lt","sk","sr","sl","vi","tl","is"]
	
	itineraryType = ["ONE_WAY","ROUND_TRIP","MULTI_CITY"]
	classOfService =["ECONOMY","PREMIUM_ECONOMY","BUSINESS","FIRST"]
	sortOrder =["ML_BEST_VALUE","DURATION","PRICE","EARLIEST_OUTBOUND_DEPARTURE","EARLIEST_OUTBOUND_ARRIVAL","LATEST_OUTBOUND_DEPARTURE","LATEST_OUTBOUND_ARRIVAL"]
	
	units = ["metric","imperial"]
	order_by = ["popularity","class_ascending","class_descending","distance","upsort_bh","review_score"]
	include_adjacency=["true","false"]
	categories_filte = "class::2,class::4,free_cancellation::1"
	customer_type = ['solo_traveller','review_category_group_of_friends']
	currency_codes = [
    "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN",
    "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL",
    "BSD", "BTN", "BWP", "BYN", "BYR", "BZD", "CAD", "CDF", "CHF", "CLP",
    "CNY", "COP", "CRC", "CUP", "CVE", "CYP", "CZK", "DJF", "DKK", "DOP",
    "DZD", "EEK", "EUR", "EGP", "ETB", "FJD", "GBP", "GEL", "GHS", "GMD",
    "GNF", "GRD", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR",
    "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS",
    "KHR", "KMF", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD",
    "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT",
    "MOP", "MRO", "MTL", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD",
    "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP",
    "PKR", "PLN", "PYG", "QAR", "ROL", "RON", "RSD", "RUB", "RWF", "SAR",
    "SBD", "SCR", "SDG", "SEK", "SGD", "SIT", "SKK", "SLL", "SOS", "SRD",
    "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMM", "TND", "TOP", "TRY",
    "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VEB", "VEF",
    "VES", "VND", "VUV", "WST", "XAF", "XCD", "XOF", "XPF", "YER", "ZAR",
    "ZMK", "ZMW"]

	from_country = ["it", "de", "nl", "fr", "es", "ca", "no", "fi", "sv", "da", "cs", "hu", "ro", "ja", "pl", "el", "ru", "tr", "bg", "ar", "ko", "he", "lv", "uk", "id", "ms", "th", "et", "hr", "lt", "sk", "sr", "sl", "vi", "tl"]

class APIfunctoin(set_value):
    pass

class query(APIfunctoin):
	params = { }


class Airport(query):
	def Search(self,location):
		self.params["query"]=location
		

	def Search_Flights(self,location):
		self.params["query"]=location
		
		
	def filter(self,sourceAirportCode,destinationAirportCode,date,itineraryType,classOfService):
		self.params["sourceAirportCode"]=sourceAirportCode
		self.params["destinationAirportCode"]=destinationAirportCode
		self.params["date"]=date
		self.params["itineraryType"] =itineraryType
		self.params["classOfService"]=classOfService
		
		

class Hotels(query):

	def Search_Location(self,Name_location):
		self.params["query"]=Name_location

	def Get_Filters(self,sourceAirportCode,destinationAirportCode,date,itineraryType_num,classOfService_num):
		self.params["sourceAirportCode"]=sourceAirportCode
		self.params["destinationAirportCode"]=destinationAirportCode
		self.params["date"]=date
		self.params["itineraryType"]=self.itineraryType[itineraryType_num]
		self.params["classOfService"]=self.classOfService[classOfService_num]


	def Search_Hotels(self,hotel_id,locale_num):
		self.params["hotel_id"]=hotel_id
		self.params["locale"]=self.locale[locale_num]
	
	
	def Search_Hotels_Location(self):
		self.params["hotel_id"]=hotel_id
		self.params["locale"]=self.locale[locale_num]

	# Hotel Details
	

class Search(Hotels):
	def coordinates(self,units_num,room_number,longitude,latitude,filter_by_currency,order_by_num,locale_num,checkout_date,adults_number,checkin_date,children_ages,children_number,page_number,categories_filte_num):
		self.params["units"]=self.units[units_num]
		self.params["room_number"]=room_number
		self.params["longitude"]=longitude
		self.params["latitude"]=latitude
		self.params["filter_by_currency"]=filter_by_currency
		self.params["order_by"]=self.order_by[order_by_num]
		self.params["locale"]=self.locale[locale_num]
		self.params["checkout_date"]=checkout_date
		self.params["adults_number"]=self.include_adjacency[adults_number]
		self.params["checkin_date"]=checkin_date
		self.params["children_ages"]=children_ages
		self.params["children_number"]=children_number
		self.params["page_number"]=page_number
		self.params["categories_filter_ids"]=self.categories_filte[categories_filte_num]
		
	def Search_hotels(self,checkin_date,units_num,checkout_date,adults_number_data,order_by_num,dest_id,filter_by_currency_num,locale_num,children_number,categories_filte_num,page_number,adults_number):
		self.params["checkin_date"]=checkin_date
		self.params["units"]=self.units[units_num]
		self.params["checkout_date"]=checkout_date
		self.params["adults_number"]=adults_number_data
		self.params["order_by"]=self.order_by[order_by_num]
		self.params["dest_id"]=dest_id
		self.params["filter_by_currency"]=filter_by_currency_num
		self.params["locale"]=self.locale[locale_num]
		self.params["categories_filter_ids"]=self.categories_filte[categories_filte_num]
		self.params["page_number"]=page_number
		self.params["adults_number"]=self.include_adjacency[adults_number]
	
	def locations(self,name,locale_num):
		self.params["name"]=name
		self.params["locale"]=self.locale[locale_num]

class CarRent(query):
	def Search(self,locale_num,name):
		self.params["locale"]=self.locale[locale_num]
		self.params["name"]	=name

	def rental(self,currency_num,drop_off_latitude,sort_by,price_low_to_high,drop_off_datetime,from_country_num,pick_up_latitude,locale_num,pick_up_datetime,drop_off_longitude,pick_up_longitude):
		self.params["currency"]=self.currency_codes[currency_num]
		self.params["drop_off_latitude"]=drop_off_latitude
		self.params["sort_by"]=sort_by
		self.params["price_low_to_high"]=price_low_to_high
		self.params["drop_off_datetime"]=drop_off_datetime
		self.params["from_country"] = self.from_country[from_country_num]
		self.params["pick_up_latitude"]=pick_up_latitude
		self.params["locale"]=self.locale[locale_num]
		self.params["pick_up_datetime"]=pick_up_datetime
		self.params["drop_off_longitude"]=drop_off_longitude
		self.params["pick_up_longitude"]=pick_up_longitude

	def supplier_details(self, from_country_num, locale_num):
		self.params["from_country"] = self.from_country[from_country_num]
		self.params["locale"] = self.locale[locale_num]
		

	def Reviews_about_vehicles(self, locale_num, location_id, from_country_num):
		self.params["locale"] = self.locale[locale_num]
		self.params["location_id"] = location_id
		self.params["from_country"] = self.from_country[from_country_num]
		
	def Rental_terms(self, from_country, pick_up_location_id, locale): 
		self.params["from_country"] = from_country
		self.params["pick_up_location_id"] = pick_up_location_id
		self.params["locale"] = self.locale[locale]
	
	
class ListData(query):
	def Hotels(self, page=None, city_id=None, slug=None, region_id=None, country=None,exact_class=None, hotel_id=None, zip_code=None, hotel_type_id=None,district_id=None, name=None):
		self.params["page"] = page
		self.params["city_id"] = city_id
		self.params["slug"] = slug
		self.params["region_id"] = region_id
		self.params["country"] = country
		self.params["exact_class"] = exact_class
		self.params["hotel_id"] = hotel_id
		self.params["zip_code"] = zip_code
		self.params["hotel_type_id"] = hotel_type_id
		self.params["district_id"] = district_id
		self.params["name"] = name

	

class urlhandel():
	handel = {
		'exchange':{
			'exchange_rates':{
				'main':'metadata',
				'sub':'exchange-rates'
			}
		},
		'Hotels':{
			'Data_hotel':{
				'main':'hotels',
				'sub':'reviews-filter-metadata'

			},
			 'Reviews_hotel':{
				'main':'hotels',
				'sub':'reviews'
			 },
			 'Description_hotel':{
				'main':'hotels',
				'sub':'description'
			 },
			 'Review_scores':{
				'main':'hotels',
				'sub':'review-scores'
			 },
			 'coordinates':{
				'main':'hotels',
				'sub':'search-by-coordinates'
			 },
			 'Search_hotels':{
				'main':'hotels',
				'sub':'search'
			 },
			 'locations':{
				'main':'hotels',
				'sub':'locations'
			 }
		},
		'CarRent':{
			'Search':{
				'main':'car-rental',
				'sub':'locations'
			},
			
			'rental':{
				'main':'car-rental',
				'sub':'search'
			}
			,
			
			'supplier_details':{
				'main':'car-rental',
				'sub':'supplier/details'
			},
			
			'Reviews_about_vehicles':{
				'main':'car-rental',
				'sub':'supplier/reviews'
			}
		},
		"ListData":{
			'Hotels':{
				'main':'static',
				'sub':'hotels'
			}

		}

	}
	def _set(self,mainClass,method):
		 return self.handel[mainClass][method]
		
	
class queryhandle(exchange,Search,CarRent,ListData):
	def query(self,main,sub):
		pass
		



class urlhandle(urlhandel):
	def url(self,main,sub):
		config_run = config.main()
		config_url = urlhandel()
		data=config_url._set(main,sub)
		config_run.run(data='booking', dmain=data['main'], sub=data['sub'])
		return config_run.url,config_run.header


x = urlhandle()
w,y=x.url(main='Hotels',sub='locations')
print(w)
