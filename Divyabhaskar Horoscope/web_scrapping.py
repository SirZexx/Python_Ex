import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.divyabhaskar.co.in/rashifal/13/today/"
r = requests.get(URL)

soup = bs(r.content,'html.parser')
file = open("F:\Work\Python Lessons\Exercise\Divyabhaskar Horoscope\Output\Test.txt","w",encoding='utf8')
text_type = soup.findAll(['h1','p'])
for text in text_type:
    file.write(f"{text.text}\n")
file.close()