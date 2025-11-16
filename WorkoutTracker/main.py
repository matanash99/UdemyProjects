import requests
from data import *
import datetime as dt

########NUTRIENTS#########
nutrition_id = "2aadbe97"
nutrition_key = "81d59c0af266e8e48067d059432fd50c"

NUTRIENT_DOMAIN = "https://trackapi.nutritionix.com"
nutrients_endpoint = "/v2/natural/nutrients"

nutrients_url = f"{NUTRIENT_DOMAIN}{nutrients_endpoint}"
nutrientix_headers = {
    "x-app-id": nutrition_id ,
    "x-app-key": nutrition_key,
    "Content-Type": "application/json"
}

nutrient_parameters = {
    "query":"1 orange"
}

exercise_parameters = {
    "query":input("Enter your exercise: ")
}

exercise_endpoint = "/v2/natural/exercise"
exercise_url = f"{NUTRIENT_DOMAIN}{exercise_endpoint}"
exercise_response = requests.post(url= exercise_url, headers= nutrientix_headers, json=exercise_parameters)
exercises_data = exercise_response.json()

'''Test on orange'''
#######Helper##### nutrient_test = orange_data
# nutrients_test= requests.post(url= nutrients_url,headers= nutrientix_headers, json= nutrient_parameters)


############SHEETY#############
SHEETY_DOMAIN = "https://api.sheety.co/"
sheety_id = "e4f2f9a8c37e8ee2f07e1928711720d4/"
sheety_workout_endpoint = "workoutTracker/sheet1"
workout_sheet_url = f"{SHEETY_DOMAIN}{sheety_id}{sheety_workout_endpoint}"

today = dt.datetime.today()
date_now = today.strftime("%d/%m/%Y")
time_now = today.strftime("%H:%M:%S")


i = 1
'''Post'''
for exercise_data in exercises_data["exercises"]:
    exercise_name = exercise_data["user_input"]
    duration = exercise_data["duration_min"]
    calories = exercise_data["nf_calories"]

    workout_data = {
    "sheet1":{
        "date":date_now,
        "time":time_now,
        "exercise":exercise_name,
        "duration":duration,
        "calories":calories
        }
    }
    print(f"{i}- Name: {exercise_name} Duration: {duration} Calories: {calories}")
    i+=1
    workout_post = requests.post(url=workout_sheet_url, json=workout_data)






# '''Get'''
# workout_response = requests.get(url= workout_sheet_url)
# print(workout_response)
# print(workout_response.text)


