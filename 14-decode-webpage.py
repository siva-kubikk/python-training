"""
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

"""

import requests, bs4

r = requests.get("https://www.nytimes.com/")

soup = bs4.BeautifulSoup(r.text, features="html.parser")

for i in soup.find_all(class_="story_heading"):
    print(i.contents[0])
