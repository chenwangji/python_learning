# _*_ coding: utf-8 _*_
import requests
from lxml import html

url = 'https://movie.douban.com/chart'
# 二进制文件
r = requests.get(url).text
# 生成 xml 树
sel = html.fromstring(r)
# 获取标题
title = sel.xpath("//h1/text()") 
print(type(title))
print(title[0])
# 获取链接
links = sel.xpath('//div[@class="pl2"]/a/@href')
for link in links:
  print(link)
