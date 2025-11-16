import requests
import datetime as dt
from requests.utils import to_key_val_list

token = "tainer1!"
pixela_endpoint = "https://pixe.la/v1/users/"

username = "mataniwani"
user_parameters = {"token":token,
              "username": username,
              "agreeTermsOfService": "yes",
              "notMinor": "yes"}
# response = requests.post(url= pixela_endpoint, json= parameters)
# print(response.text)

graph_id = "graph1"
graph_paramters = {
    "id":graph_id,
    "name":"Cycling Graph",
    "unit":"kilometers",
    "type":"float",
    "color":"ajisai",
}
header = {
    "X-USER-TOKEN":token
}
#
# graph_endpoint = f"{pixela_endpoint}{username}/graphs/"
# response = requests.post(headers= header, url= graph_endpoint, json= graph_paramters)

day = dt.datetime.today()
formatted_day = day.strftime("%Y%m%d")

post_graph_parameters = {
    "date":formatted_day,
    "quantity":input("How many kilometers have you done today? "),
}



post_graph_endpoint = f"{pixela_endpoint}{username}/graphs/{graph_id}"
post_response = requests.post(headers= header, url= post_graph_endpoint, json= post_graph_parameters)
print(post_response.text)

# put_graph_endpoint = f"{pixela_endpoint}{username}/graphs/{graph_id}/{formatted_day}"
# put_response = requests.put(headers= header, url= put_graph_endpoint, json= put_graph_parameters)
# print(put_response.text)

# delete_graph_endpoint = f"{pixela_endpoint}{username}/graphs/{graph_id}/{formatted_day}"
# delete_response = requests.delete(url= delete_graph_endpoint, headers= header)
# print(delete_response.text)
