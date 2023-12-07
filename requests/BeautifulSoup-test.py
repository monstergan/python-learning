# 使用BeautifulSoup解析网页
import requests
from bs4 import BeautifulSoup as bs

user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

header = {'user-agent': user_agent}

myurl = 'https://movie.douban.com/top250?start=0'

response= requests.get(myurl,headers=header)

bs_info = bs(response.text,'html.parser')

for tags in bs_info.find_all('div',attrs={'class':'hd'}):
    for atag in tags.find_all('a'):
        # 获取所有链接
        print(atag.get('href'))
        # 获取电影名字
        print(atag.find('span').text)