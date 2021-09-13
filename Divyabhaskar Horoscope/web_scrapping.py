import requests
from bs4 import BeautifulSoup as bs
from datetime import date
import os

today = date.today()
os.mkdir(f"F:\Work\Python Lessons\Exercise\Divyabhaskar Horoscope\Daily_Rashi\{today}")

Rashi = {'Aries':13,'Taurus':15,'Gemini':16,'Cancer':19,'Leo':17,'Virgo':18,'Libra':20,'Scorpio':14,'Sagittarius':21,'Capricorn':22,'Aquarius':23,'Pisces':24}

for name,value in Rashi.items():
    URL = f"https://www.divyabhaskar.co.in/rashifal/{value}/today/"
    r = requests.get(URL)

    soup = bs(r.content,'html.parser')
    file = open(f"F:\Work\Python Lessons\Exercise\Divyabhaskar Horoscope\Daily_Rashi\{today}\{name}.txt","w",encoding='utf8')
    text_type = soup.findAll(['h1','p'])
    for text in text_type:
            file.write(f"{text.text}\n")
    file.close()

    line_num=0
    rmv_line=[1,2,16,17,18,19,20,21,22,23,24,25,26,27]
    data=""
    data1=""

    file= open(f"F:\Work\Python Lessons\Exercise\Divyabhaskar Horoscope\Daily_Rashi\{today}\{name}.txt",'r+',encoding='utf8')
    for line in file:
        line_num+=1
        if line_num in rmv_line:
            line=[]
        data=''.join(line)
        data1=(data1+data)
    file.close()

    file= open(f"F:\Work\Python Lessons\Exercise\Divyabhaskar Horoscope\Daily_Rashi\{today}\{name}.txt",'w',encoding='utf8')
    file.write(data1)
    file.close()
