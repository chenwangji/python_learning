import requests
import os
from lxml import html

FILE_NAME = 'top250.txt'
BASE_URL = 'https://movie.douban.com/top250'

def get_movies(base_url):
  COUNT_OF_SINGLE_PAGE = 25
  TOTAL = 250
  start = 0
  while start <= TOTAL:
    params = { 'start': start, 'filter': '' }
    url = base_url + '?start={0[start]}&filter={0[filter]}'.format(params)
    res = requests.get(url).content
    current_html = html.fromstring(res)
    get_sigle_page_movies(current_html, start)
    # 换至下页
    start += COUNT_OF_SINGLE_PAGE

def get_sigle_page_movies(current_html, start):
  movie_index = start
  for i in current_html.xpath('//div[@class="info"]'):
    try:
      # index
      movie_index += 1
      # 电影名称
      movie_title = i.xpath('div[@class="hd"]/a/span[@class="title"]/text()')[0]
      # 电影信息
      movie_info = i.xpath('div[@class="bd"]/p[1]/text()')[0].strip()
      # 电影评分
      move_rating_num = i.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')[0]
      # 电影评价人数
      rating_people_count = i.xpath('div[@class="bd"]/div[@class="star"]/span[last()]/text()')[0]

      data = (movie_index, movie_title, movie_info, move_rating_num, rating_people_count)
      save_data(data)
    except: 
      print('err')

def save_data(data):
  """
  w：以写方式打开，
  a：以追加模式打开 (从 EOF 开始, 必要时创建新文件)
  r+：以读写模式打开
  w+：以读写模式打开 (参见 w )
  a+：以读写模式打开 (参见 a )
  rb：以二进制读模式打开
  wb：以二进制写模式打开 (参见 w )
  ab：以二进制追加模式打开 (参见 a )
  rb+：以二进制读写模式打开 (参见 r+ )
  wb+：以二进制读写模式打开 (参见 w+ )
  ab+：以二进制读写模式打开 (参见 a+ )
  """
  with open(FILE_NAME, 'a') as f:
    movie = "TOP%s:\n电影名称：%s\n电影信息：%s\n电影评分：%s\n电影评价人数：%s\n"%(data)
    f.write(movie)
    f.write('='*50 + '\n')

def scraper():
  if os.path.exists(FILE_NAME):
      os.remove(FILE_NAME)
  get_movies(BASE_URL)

# 执行爬虫
scraper()