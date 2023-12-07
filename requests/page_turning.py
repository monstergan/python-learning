import requests
from bs4 import BeautifulSoup as bs

# Python 使用def定义函数，myUrl是函数的参数
def get_url_name(myUrl):
    user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

    header = {'user-agent': user_agent}
    response = requests.get(myUrl, headers=header)
    bs_info = bs(response.text, 'html.parser')

    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        for atag in tags.find_all('a'):
            # 获取所有链接
            print(atag.get('href'))
            # 获取电影名字
            print(atag.find('span').text)

# 生成包含所有页面的元组
urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(10))

print(urls)

# 控制请求的频率，引入了time模块
from time import sleep

sleep(10)

for page in urls:
    get_url_name(page)
    sleep(5)