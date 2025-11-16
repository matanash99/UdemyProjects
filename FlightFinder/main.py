from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch
import datetime as dt

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.

paris_test_json = {'status': True, 'message': 'Success', 'timestamp': 1751724990346, 'data': [{'departureDate': '2025-07-06', 'searchDates': ['2025-07-06'], 'offsetDays': 1, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0F5S2HwdrZ2uGuBB7LICMAhjsxYEpXUFKEFvgSxYkh-cswBUQ5sJAd7CKGCMnx47rQ', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 303, 'nanos': 640000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 304, 'nanos': 190000000}}, {'departureDate': '2025-07-07', 'searchDates': ['2025-07-07'], 'offsetDays': 2, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0G6xFMT-vehGnAQKN_Be_0BjsxYEpXUFKEFvgSxYkh-ceO9jg7gg6URdkXYazhXNrA', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 303, 'nanos': 310000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 303, 'nanos': 450000000}}, {'departureDate': '2025-07-08', 'searchDates': ['2025-07-08'], 'offsetDays': 3, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0F5S2HwdrZ2uGuBB7LICMAhjsxYEpXUFKEFvgSxYkh-c4X2YMUdub03XTEZHwnVbmQ', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 303, 'nanos': 610000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 304, 'nanos': 190000000}}, {'departureDate': '2025-07-09', 'searchDates': ['2025-07-09'], 'offsetDays': 4, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0A75vB9bbKsvwzEgfXb0lAdjsxYEpXUFKEFvgSxYkh-ceO9jg7gg6URdkXYazhXNrA', 'isCheapest': True, 'price': {'currencyCode': 'USD', 'units': 244, 'nanos': 600000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 244, 'nanos': 670000000}}, {'departureDate': '2025-07-10', 'searchDates': ['2025-07-10'], 'offsetDays': 5, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0F5S2HwdrZ2uGuBB7LICMAhjsxYEpXUFKEFvgSxYkh-c2Ih03-Qfw_q_jDlUPDnywA', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 303, 'nanos': 640000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 304, 'nanos': 190000000}}]}
london_test_json = {'status': True, 'message': 'Success', 'timestamp': 1751724991625, 'data': [{'departureDate': '2025-07-06', 'searchDates': ['2025-07-06'], 'offsetDays': 1, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0IDM37ARIRBM_MQRHuzMoM8b8510Fnp-EbokKDA1XKUJ2KT1nf8ngQJ2P3F9WrATWA', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 417, 'nanos': 690000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 418, 'nanos': 0}}, {'departureDate': '2025-07-07', 'searchDates': ['2025-07-07'], 'offsetDays': 2, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0AJWsrG95r_vWUYW5YvNGPwb8510Fnp-EbokKDA1XKUJByir-cnKw-ojOSXw3kdxjw', 'isCheapest': True, 'price': {'currencyCode': 'USD', 'units': 255, 'nanos': 310000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 256, 'nanos': 0}}, {'departureDate': '2025-07-08', 'searchDates': ['2025-07-08'], 'offsetDays': 3, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0LMR6HMiQuDI4sTVhSiY_YYb8510Fnp-EbokKDA1XKUJK5c58YxyDgo2qNiLfS0KVw', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 365, 'nanos': 700000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 366, 'nanos': 0}}, {'departureDate': '2025-07-09', 'searchDates': ['2025-07-09'], 'offsetDays': 4, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0PlnV45wt8UhUlhjrnc674cb8510Fnp-EbokKDA1XKUJmEoUVfvsvkRE0Si2Sj6A6Q', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 414, 'nanos': 860000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 415, 'nanos': 0}}, {'departureDate': '2025-07-10', 'searchDates': ['2025-07-10'], 'offsetDays': 5, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0HBUrHG8beYVGVb4uXNcyTwb8510Fnp-EbokKDA1XKUJazNvTsmUFQv3edH-fMpDNw', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 432, 'nanos': 160000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 433, 'nanos': 0}}]}
new_york_test_json = {'status': True, 'message': 'Success', 'timestamp': 1751724993281, 'data': [{'departureDate': '2025-07-06', 'searchDates': ['2025-07-06'], 'offsetDays': 1, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0Ojh1Tjh4VtdeQm3UMhIlpoKL5F-htWi3l1f6M3IuR4LUCI9QLMtIXZ8s_ouL7udAQ', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 950, 'nanos': 680000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 950, 'nanos': 770000000}}, {'departureDate': '2025-07-07', 'searchDates': ['2025-07-07'], 'offsetDays': 2, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0L27T1asEdAZKjHx5J_zcTgKL5F-htWi3l1f6M3IuR4LtCkx0ZS7S9MeEbGm9P2dYQ', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 876, 'nanos': 760000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 877, 'nanos': 300000000}}, {'departureDate': '2025-07-08', 'searchDates': ['2025-07-08'], 'offsetDays': 3, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0L27T1asEdAZKjHx5J_zcTihazZvro9NNGPVdEa4a2vT5_j8FIJAydzqdc2wkE6eJA', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 874, 'nanos': 810000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 875, 'nanos': 90000000}}, {'departureDate': '2025-07-09', 'searchDates': ['2025-07-09'], 'offsetDays': 4, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0GDGZxzLGQZaA7KHKD8XNOV4w5FDycNiDYDBntv-fbsgwXs9cEkYsthbhKmbxwUtPw', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 798, 'nanos': 120000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 798, 'nanos': 680000000}}, {'departureDate': '2025-07-10', 'searchDates': ['2025-07-10'], 'offsetDays': 5, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0BiQgHEG2XEs6JO4myI8jluKezxNdtXiEiEr_tY3wyc65GCbHzhpFX0KHXuYE4FvLA', 'isCheapest': True, 'price': {'currencyCode': 'USD', 'units': 717, 'nanos': 190000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 717, 'nanos': 850000000}}]}
tokyo_test_json = {'status': True, 'message': 'Success', 'timestamp': 1751724994302, 'data': [{'departureDate': '2025-07-06', 'searchDates': ['2025-07-06'], 'offsetDays': 1, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0OHNEXFRccVk0VmiRuZauXPV5bHXEPBZywSi6jXOZ3Bj1JxxwwzxC6FFTPQSnRhXmw', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 896, 'nanos': 520000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 897, 'nanos': 0}}, {'departureDate': '2025-07-07', 'searchDates': ['2025-07-07'], 'offsetDays': 2, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0EGhff_A4Grdu50nmKBh8I-5P_8VOkUJOnAxsXRRVh9YH0BqpSb_ljOGnmkDyk-IkA', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 1204, 'nanos': 120000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 1205, 'nanos': 0}}, {'departureDate': '2025-07-08', 'searchDates': ['2025-07-08'], 'offsetDays': 3, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0He5PZdu-n2XwrC0AGvHJEbV5bHXEPBZywSi6jXOZ3BjG2iIzI9MAYPcmAox8LOBKA', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 882, 'nanos': 320000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 883, 'nanos': 0}}, {'departureDate': '2025-07-09', 'searchDates': ['2025-07-09'], 'offsetDays': 4, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0IdabuECssZIFx-P8oZb_brV5bHXEPBZywSi6jXOZ3BjsDg5ZwhAGn0LKj_7olOcyw', 'isCheapest': True, 'price': {'currencyCode': 'USD', 'units': 813, 'nanos': 330000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 814, 'nanos': 0}}, {'departureDate': '2025-07-10', 'searchDates': ['2025-07-10'], 'offsetDays': 5, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0K_0yWtAMOCdMe8Rtmt9M1_V5bHXEPBZywSi6jXOZ3BjgBI15pzV6dhJRaQAMcDUeA', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 973, 'nanos': 780000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 974, 'nanos': 0}}]}
rome_test_json = {'status': True, 'message': 'Success', 'timestamp': 1751724995463, 'data': [{'departureDate': '2025-07-06', 'searchDates': ['2025-07-06'], 'offsetDays': 1, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0NZQhbsagC09W-guHSI_i18NQT5KIYOBl8OjSQNvA431xABNOYfkv9yjd5bqnZ9Paw', 'isCheapest': True, 'price': {'currencyCode': 'USD', 'units': 162, 'nanos': 100000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 163, 'nanos': 0}}, {'departureDate': '2025-07-07', 'searchDates': ['2025-07-07'], 'offsetDays': 2, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0NZQhbsagC09W-guHSI_i18NQT5KIYOBl8OjSQNvA431A5TL3P0yOOG93mY_5dfUIQ', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 162, 'nanos': 760000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 163, 'nanos': 0}}, {'departureDate': '2025-07-08', 'searchDates': ['2025-07-08'], 'offsetDays': 3, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0ALPzavufcdMbj_aAaZdfJ0NQT5KIYOBl8OjSQNvA4311s6aLtJWDpdxB-TQLRg_6Q', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 200, 'nanos': 110000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 201, 'nanos': 0}}, {'departureDate': '2025-07-09', 'searchDates': ['2025-07-09'], 'offsetDays': 4, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0Kf_uN1qURKDCZwLX9gdd7cNQT5KIYOBl8OjSQNvA431xABNOYfkv9yjd5bqnZ9Paw', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 230, 'nanos': 810000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 231, 'nanos': 0}}, {'departureDate': '2025-07-10', 'searchDates': ['2025-07-10'], 'offsetDays': 5, 'accuracyTrackerId': '01kp0_kh0lPPIRVopJAx0HQETzbJ_pe3NnvrYFm-uHcNQT5KIYOBl8OjSQNvA4310uzXmA_bm1kNNxfbbipYaw', 'isCheapest': False, 'price': {'currencyCode': 'USD', 'units': 201, 'nanos': 720000000}, 'priceRounded': {'currencyCode': 'USD', 'units': 202, 'nanos': 0}}]}

jsons_helper = [
    paris_test_json,
    london_test_json,
    new_york_test_json,
    tokyo_test_json,
    rome_test_json
]

airports = {
    "Paris": "CDG",        # Charles de Gaulle
    "London": "LHR",       # Heathrow
    "New York": "JFK",     # John F. Kennedy
    "Tokyo": "HND",        # Haneda
    "Rome": "FCO"          # Fiumicino
}

today = dt.datetime.today()
today_str = today.strftime("%Y-%m-%d")
return_date = "2025-07-18"
search_dates = [today_str, return_date]


def exception_helper(current_json):
    for current_data in current_json["data"]:
        if current_data["isCheapest"]:
            price = current_data["price"]["units"]
            departure_date = current_data["departureDate"]
            lowest_flight_data = FlightData(price, departure_date, city, city_code, search_dates)
            lowest_flight_manager = DataManager()
            return lowest_flight_manager.upload_data(lowest_flight_data)


i = 0

for city,city_code in airports.items():
    current_city = FlightSearch()
    current_json = current_city.check_flights(city_code, today_str, search_dates)

    try:
        is_price_changed = exception_helper(current_json)
    ##Used because reached limits of getting flight data from x-rapdid-api
    except KeyError:
        current_json = jsons_helper[i]
        i+=1
        is_price_changed = exception_helper(current_json)
    if is_price_changed:
        notification = NotificationManager()
        notification.notify(city)


