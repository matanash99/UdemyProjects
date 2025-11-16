import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)

top_100_soup = BeautifulSoup(response.text, "html.parser")
top_100_titles = [movie.getText() for movie in top_100_soup.find_all(name="h3", class_="title")]

with open("top100List.txt", "w", encoding="utf-8") as file:
    for i in range(99, -1, -1):
        file.write(top_100_titles[i] + '\n')