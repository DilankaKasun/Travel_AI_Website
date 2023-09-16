class API_Data():
    header = {"X-RapidAPI-Key":"4aa76929eemsh4bcb103455c220fp120f64jsnfbeadc4698b5"}
    url = []
    def _key(self,key,headers=header,urls=url):
        if key == "booking_com":
            headers["X-RapidAPI-Host"]="booking-com.p.rapidapi.com"
            urls.append('https://booking-com.p.rapidapi.com/v1/metadata/exchange-rates')
        elif key == "Tripadvisor":
            headers["X-RapidAPI-Host"]="tripadvisor16.p.rapidapi.com"
            urls.append(urls = 'https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchAirport')
        elif key == "sky-scrapper":
            headers["X-RapidAPI-Host"]="sky-scrapper.p.rapidapi.com"    

            
class config(API_Data):
    def booking_com(self):
        self._key("booking_com")
        querystring = None

class  main(config):
    def run(self):
        self.booking_com()
        print(self.header)
        print(self.url)
        
  
x = main()
x.run()