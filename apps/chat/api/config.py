class API_Data():
    header = {"X-RapidAPI-Key": "f32c78986cmsh12ef2c5be09aae5p1ec3adjsne50e1b1deffa"}
    url = []

    def _key(self, key, main=None, sub=None, headers=header, urls=url):
        if key == "booking_com":
            headers["X-RapidAPI-Host"] = "booking-com.p.rapidapi.com"
            urls.append(f'https://booking-com.p.rapidapi.com/v1/{main}/{sub}')
        elif key == "Tripadvisor_com":
            headers["X-RapidAPI-Host"] = "tripadvisor16.p.rapidapi.com"
            urls.append(f'https://tripadvisor16.p.rapidapi.com/api/v1/{main}/{sub}')
        elif key == "sky_scrapper":
            headers["X-RapidAPI-Host"] = "sky-scrapper.p.rapidapi.com"
            urls.append(f'https://sky-scrapper.p.rapidapi.com/api/v1/{main}/{sub}')
        elif key == "google_map_business":
            headers["X-RapidAPI-Host"] = "local-business-data.p.rapidapi.com"
            urls.append(f'https://local-business-data.p.rapidapi.com/{main}')
        elif key == "google_Map_Geocoding":
            headers["X-RapidAPI-Host"] = "map-geocoding.p.rapidapi.com"
            urls.append(f'https://map-geocoding.p.rapidapi.com/{main}')
        elif key == "google_map_routes":
            headers["X-RapidAPI-Host"] = "trueway-directions2.p.rapidapi.com"
            urls.append(f'trueway-directions2.p.rapidapi.com{main}')



class config(API_Data):
    def booking_com(self, dmain, sub):
        self._key("booking_com", dmain, sub)

    def tripadvisor_com(self, dmain, sub):
        self._key("Tripadvisor_com", dmain, sub)
        
    def sky_scrapper_com(self, dmain, sub):
        self._key("sky_scrapper", dmain, sub)
    
    def google_map_business(self,dmain):
        self._key("google_map_business",dmain)

    def google_Map_Geocoding(self,dmain):
        self._key("google_Map_Geocoding",dmain)

    def google_map_routes(self,dmain):
        self._key("google_Map_Geocoding",dmain)

class OpenAi():
    OPENAI_API_KEY = "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"
        
    # end def      

class main(config):
    def run(self, data=None, dmain=None, sub=None):
        if data == "booking":
            return self.booking_com(dmain, sub)
        elif data == "Tripadvisor":
            return  self.tripadvisor_com(dmain, sub)
        elif data == "sky_scrapper":
            return  self.sky_scrapper_com(dmain, sub)
        elif data == "google_map_business":
            return  self.google_map_business(dmain)
        elif data == "google_Map_Geocoding":
            return  self.google_Map_Geocoding(dmain)
        elif data == "google_map_routes":
            return  self.google_map_routes(dmain)

