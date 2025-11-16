import requests
from bs4 import BeautifulSoup
import smtplib as smtp

from pyexpat.errors import messages

url = "https://www.optical-center.co.il/%D7%9E%D7%A9%D7%A7%D7%A4%D7%99-%D7%A9%D7%9E%D7%A9/%D7%9E%D7%A9%D7%A7%D7%A4%D7%99-%D7%A9%D7%9E%D7%A9-RAY-BAN-RB-4306-60171-5419-28426.html?gad_source=1&gad_campaignid=22321481989&gbraid=0AAAAAoyv5gzLch0jN75VFRVs9J8RuNQvU&gclid=Cj0KCQjw5onGBhDeARIsAFK6QJZ7tNkN7ar-AN_wPGTVtmupDqQUJFy51lR8AlHFV6c7-tZ5xKwtPRQaAuViEALw_wcB"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "Accept-Language":"en,en-US;q=0.9,he;q=0.8"
}

response = requests.get(url, headers=headers)

oc_soup = BeautifulSoup(response.text, "html.parser")
rayban_tag = oc_soup.find(name="span", class_= "product-details__price truePrice")
rayban_price = int(rayban_tag.getText().split()[0])

print(rayban_price)

my_email = "mataniwani1999@gmail.com"
app_password = "zlza htit bdrb nmqa"

with smtp.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(my_email, app_password)


if rayban_price < 350:
    with smtp.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, app_password)
        connection.sendmail(my_email, my_email, msg="Subject:Ray-Ban price dropped below 350\n\n"
                                                    "This is your program notifying you that the Ray-Ban price is under 350 shekels.\n"
                                                    f"Link: {url}"
        )
