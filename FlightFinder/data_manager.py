import requests
from flight_data import FlightData

SHEETY_DOMAIN = "https://api.sheety.co"
sheety_id = "/e4f2f9a8c37e8ee2f07e1928711720d4"
flight_data_sheet_endpoint = "/flightTracker/flights/"
flight_tracker_url = f"{SHEETY_DOMAIN}{sheety_id}{flight_data_sheet_endpoint}"

class DataManager:

    # This class is responsible for talking to the Google Sheet.
    def upload_data(self, new_flight_data:FlightData):

        response = requests.get(flight_tracker_url)
        flight_tracker_json = response.json()
        for current_data in flight_tracker_json["flights"]:

            if current_data["city"] == new_flight_data.city:
                if int(current_data["lowestPrice"]) > int(new_flight_data.price):
                    flight_params= {
                        "flights": {
                            "city": new_flight_data.city,
                            "city_code": new_flight_data.city_code,
                            "lowestPrice": new_flight_data.price,
                        }
                    }
                    row_id = current_data["id"]
                    print(row_id)
                    post_response = requests.put(url= f"{flight_tracker_url}{row_id}", json= flight_params)
                    return True
                else:
                    print(f"No need to change for {new_flight_data.city}")
                    return False