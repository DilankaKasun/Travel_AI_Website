class API_Data():
    header = {"X-RapidAPI-Key":"4aa76929eemsh4bcb103455c220fp120f64jsnfbeadc4698b5"}
    url = []
    def _key(self,key,main,sub,headers=header,urls=url):
        if key == "booking_com":
            headers["X-RapidAPI-Host"]="booking-com.p.rapidapi.com"
            urls.append(f'https://booking-com.p.rapidapi.com/v1/{main}/{sub}')
        elif key == "Tripadvisor_com":
            headers["X-RapidAPI-Host"]="tripadvisor16.p.rapidapi.com"
            urls.append(f'https://tripadvisor16.p.rapidapi.com/api/v1/{main}/{sub}')
        elif key == "sky_scrapper":
            headers["X-RapidAPI-Host"]="sky-scrapper.p.rapidapi.com"    
            urls.append(f'https://sky-scrapper.p.rapidapi.com/api/v1//{main}/{sub}')

class config(API_Data):
    def booking_com(self):
        self._key("booking_com","data","data")
        querystring = None

    def tripadvisor_com(self):
        self._key("Tripadvisor_com","data","data")
        querystring = None

    def sky_scrapper_com(self):
        self._key("sky_scrapper","data","data")
        querystring = None

      

class  main(config):
    def run(self,data=None):
        if (data=="booking"):
            self.booking_com()
            print(self.header)
                  # end if
        
        


        

__main__ = __name__

x = main()
x.run(data='booking')


