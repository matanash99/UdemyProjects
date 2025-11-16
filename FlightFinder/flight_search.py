import requests

url = "https://booking-com15.p.rapidapi.com/api/v1/flights/getMinPrice"

headers = {
	"x-rapidapi-key": "00a6b66d82msh25dc36cebd0d8cap1d71e5jsn7b27ff58236d",
	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
}

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def check_flights(self, code, depart_date, search_dates):
        querystring = {"fromId": f"TLV.AIRPORT",
                        "toId":f"{code}.AIRPORT",
                        "cabinClass":"ECONOMY",
                        "currency_code":"USD",
                        "departDate":depart_date,
                        "searchDates": search_dates,
                        }
        print("hello")
        response = requests.get(url, headers=headers, params=querystring)
        print(response.text)
        data_json = response.json()
        return data_json