import requests

url = "https://booking-com.p.rapidapi.com/v1/hotels/locations"

querystring = {"name":"Berlin","locale":"en-gb"}

headers = {
	"X-RapidAPI-Key": "4aa76929eemsh4bcb103455c220fp120f64jsnfbeadc4698b5",
	"X-RapidAPI-Host": "booking-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())