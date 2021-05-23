import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests\
    .get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr')


for tr in trs:
    movie_index = tr.select_one('td > img')
    movie_name = tr.select_one('td.title > div > a')
    movie_rate = tr.select_one('td.point')
    if movie_name is not None:
      print(movie_index['alt'], movie_name.text, movie_rate.text)