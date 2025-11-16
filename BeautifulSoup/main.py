from bs4 import BeautifulSoup
import lxml
import requests


web_url = "https://news.ycombinator.com/"
response = requests.get(web_url)

soup = BeautifulSoup(response.text, "html.parser")

articles = soup.select(".titleline > a")
article_texts = [article.getText() for article in articles]
article_links = [article.get("href") for article in articles]

article_upvotes = []
subtexts = soup.select(".subtext")
for sub in subtexts:
    score_tag = sub.find("span", class_="score")
    if score_tag:
        article_upvotes.append(int(score_tag.get_text().split()[0]))
    else:
        article_upvotes.append(0)


largest_index = 0
largest_upvote = 0
current_index = 0
for num in article_upvotes:
    if num > largest_upvote:
        largest_upvote = num
        largest_index = current_index
    current_index += 1


print(largest_index)
print(article_upvotes)
print(article_links[largest_index])
print(article_texts[largest_index])









