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

line_num=0
rmv_line=[1,2,16,17,18,19,20,21,22,23,24,25,26,27]
data=""
data1=""

file= open("F:\Work\Python Lessons\Exercise\Divyabhaskar Horoscope\Output\Test.txt",'r+',encoding='utf8')
for line in file:
    line_num+=1
    if line_num in rmv_line:
        line=[]
    data=''.join(line)
    data1=(data1+data)
file.close()

file= open("F:\Work\Python Lessons\Exercise\Divyabhaskar Horoscope\Output\Test.txt",'w',encoding='utf8')
file.write(data1)
file.close()
