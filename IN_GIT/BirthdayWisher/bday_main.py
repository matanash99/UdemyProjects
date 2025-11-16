##################### Extra Hard Starting Project ######################
import smtplib as smtp
import datetime as dt
import pandas as pd
import random


my_email = "mataniwani1999@gmail.com"
password = "spbp hiex aetm oquh"


# 1. Update the birthdays.csv
# def create_entry(i):
#
#     names = ["Udemy", "Roni", "Eden", "Tamar", "Nissim", "Ayelet"]
#     emails = ["y.udemy09061999@yahoo.com", "ronirogani789@gmail.com", "eden@email.com",
#               "tamar@email.com", "nissim@email.com", "ayelet@email.com"]
#     month = random.randint(1, 12)
#     if month == 2:
#         day = random.randint(1, 28)
#     elif month == 4 or month == 6 or month == 9 or month == 11:
#         day = random.randint(1, 30)
#
#     else:
#         day = random.randint(1, 31)
#     year = random.randint(1960, 2010)
#
#     new_entry = {
#         "name": names[i],
#         "email": emails[i],
#         "day": day,
#         "month": month,
#         "year": year
#     }
#     return new_entry
#
# def fill_csv():
#
#     data_csv = pd.read_csv("birthdays.csv", on_bad_lines= 'skip')
#     data_dict = data_csv.to_dict(orient= "records")
#
#     data_dict[1] = create_entry(0)
#
#     for i in range(1,5):
#         data_dict.append(create_entry(i))
#
#     updated_df = pd.DataFrame(data_dict)
#     updated_df.to_csv("birthdays.csv", index=False)
#     print(updated_df)

# 2. Check if today matches a birthday in the birthdays.csv

dt.datetime.today()
data_csv = pd.read_csv("birthdays.csv", on_bad_lines='skip')
data_dict = data_csv.to_dict(orient="records")
current_day = dt.datetime.today().day
current_month = dt.datetime.today().month
for i in range(len(data_dict)):
    if data_dict[i]["day"] == current_day and data_dict[i]["month"] == current_month:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        to_email = data_dict[i]["email"]
        to_name = data_dict[i]["name"]

        placeholder = "[NAME]"
        letter_number = random.randint(1,3)
        with open(f"letter_templates/letter_{letter_number}.txt", "r") as letter_file:
            letter = letter_file.read()
# 4. Send the letter generated in step 3 to that person's email address.
        with open("new.txt", "w") as new_file:
            letter = letter.replace(placeholder, to_name)
            letter = letter.replace("Angela", "Matan")
            with smtp.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user= my_email, password= password)
                connection.sendmail(from_addr= my_email, to_addrs= to_email, msg= "Subject:Happy Birthday\n\n" + letter)

