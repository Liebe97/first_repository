import requests
from bs4 import BeautifulSoup
import csv
import re

soup_objects = []

URL='https://movie.naver.com/movie/running/current.nhn'
response = requests.get(URL)

soup= BeautifulSoup(response.text, 'html.parser')

soup_objects.append(soup)

movie_section = soup.select(
    '#content > div.article > div.obj_section > div.lst_wrap > ul > li')
print(movie_section)

for movie in movie_section:
    a_tag = movie.select_one('dl > dt > a')
    p = re.compile(r'<.+code=(?P<href>\d+)..(?P<name>.+)</a>')

    # print(p.match(str(a_tag)).group('href'))
    # print(p.match(str(a_tag)).group('name'))

    movie_name = p.match(str(a_tag)).group('name')
    movie_code = p.match(str(a_tag)).group('href')
    print(movie_name, movie_code)
    movies_data = {
                'name': movie_name,
                'code': movie_code  
                }
    with open('./movie_review.csv', 'a') as csvfile:
        fieldnames = ['name', 'code']
        csvwriter = csv.DictWriter(csvfile, fieldnames = fieldnames)

        csvwriter.writerow(movies_data)