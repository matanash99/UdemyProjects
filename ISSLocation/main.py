import smtplib

import requests
from tkinter import *
import datetime as dt
import time


my_longitude = 35.775719
my_latitude = 33.130280
MY_EMAIL = "mataniwani1999@gmail.com"
PASSWORD = "spbp hiex aetm oquh"




def iss_up():
    iss_response = requests.get(url= "http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    position = iss_response.json()

    iss_position = position["iss_position"]
    iss_longitude = float(iss_position["longitude"])
    iss_latitude = float(iss_position["latitude"])
    if my_longitude + 5 >= iss_longitude >= my_longitude - 5 and my_latitude + 5 >= iss_latitude >= my_latitude - 5:
        return True

    return False



def is_night():

    sun_response = requests.get(url="https://api.sunrisesunset.io/json", params={"lat": my_latitude, "lng": my_longitude})
    sun_response.raise_for_status()
    sun_json = sun_response.json()



    sunrise_hour = int(sun_json["results"]["sunrise"].split(":")[0])
    sunset_hour = int(sun_json["results"]["sunset"].split(":")[0])
    sunset_hour += 12
    hour_now = dt.datetime.now().hour

    print(sunrise_hour)
    print(sunset_hour)
    print(hour_now)
    if sunset_hour >= hour_now + 8 >= sunrise_hour:
        return False
    return True

while(True):
    time.sleep(60)
    if is_night() and iss_up():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr= MY_EMAIL, to_addrs= "mataniwani1999@gmail.com", msg= "Subject:ISS Located\n\n"
                                                                                              "Look up the ISS is visible")



#########Quotes###############
# def get_quote():
#     response = requests.get(url="https://zenquotes.io/api/random")
#
#     position = response.json()
#     new_quote = position[0]["q"]
#     canvas.itemconfig(quote_text, text= new_quote)
#
#
#
#
# window = Tk()
# window.title("Albert Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Quote", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# einstein_image = PhotoImage(file="einstein.png")
# einstein_button = Button(image=einstein_image, highlightthickness=0, command=get_quote)
# einstein_button.grid(row=1, column=0)
#
#
#
# window.mainloop()


