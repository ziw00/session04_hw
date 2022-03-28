import requests
from bs4 import BeautifulSoup 
from uhaha import extract_info
import csv

file = open('comics.csv',mode='w',newline='')
writer = csv.writer(file)
writer.writerow(["title","artist","grade"])

final_result=[]
COMICS_URL = f'https://comic.naver.com/webtoon/weekdayList?week=mon'
comics_html = requests.get(COMICS_URL)
comics_soup = BeautifulSoup(comics_html.text,"html.parser")

comics_list_box = comics_soup.find ("ul",{"class":"img_list"})
comics_list = comics_list_box.find_all("li")

final_result += extract_info(comics_list)

for result in final_result:
    row=[]
    row.append(result['title'])
    row.append(result['artist'])
    row.append(result['grade'])
    writer.writerow(row)
print(final_result)