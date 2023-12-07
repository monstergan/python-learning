#  使用requests库获取豆瓣网站的数据
import requests

user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

header = {'user-agent': user_agent}

myurl = 'https://movie.douban.com/top250?start=0'

response= requests.get(myurl,headers=header)

print(response.text)
print(f'返回码是：{response.status_code}')