import requests

class FlightData:

    def __init__(self,price, departure_date, city, city_code, search_dates):
        self.price = price
        self.departure_date = departure_date
        self.city = city
        self.city_code = city_code
        self.search_dates = search_dates