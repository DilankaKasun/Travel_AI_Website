class API_Data():
    header = {"X-RapidAPI-Key": "4aa76929eemsh4bcb103455c220fp120f64jsnfbeadc4698b5"}
    url = []

    def _key(self, key, main, sub, headers=header, urls=url):
        if key == "booking_com":
            headers["X-RapidAPI-Host"] = "booking-com.p.rapidapi.com"
            urls.append(f'https://booking-com.p.rapidapi.com/v1/{main}/{sub}')
        elif key == "Tripadvisor_com":
            headers["X-RapidAPI-Host"] = "tripadvisor16.p.rapidapi.com"
            urls.append(f'https://tripadvisor16.p.rapidapi.com/api/v1/{main}/{sub}')
        elif key == "sky_scrapper":
            headers["X-RapidAPI-Host"] = "sky-scrapper.p.rapidapi.com"
            urls.append(f'https://sky-scrapper.p.rapidapi.com/api/v1/{main}/{sub}')


class config(API_Data):
    def booking_com(self, dmain, sub):
        self._key("booking_com", dmain, sub)
        

    def tripadvisor_com(self, dmain, sub):
        self._key("Tripadvisor_com", dmain, sub)
        

    def sky_scrapper_com(self, dmain, sub):
        self._key("sky_scrapper", dmain, sub)
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


