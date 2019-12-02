# parser.py
import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "peopleIn.settings")
import django
django.setup()
# BlogData를 import해옵니다
from crawled_data.models import BlogData

def parse_blog():
    req = requests.get('https://search.naver.com/search.naver?where=news&query=%EC%86%8C%EC%83%81%EA%B3%B5%EC%9D%B8%20%EC%B0%BD%EC%97%85&sm=tab_opt&sort=1&photo=0&field=1&reporter_article=&pd=0&ds=&de=&docid=&nso=so%3Add%2Cp%3Aall%2Ca%3At&mynews=0&refresh_start=0&related=0')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        'dt > a'
        )
    data = {}
    for title in my_titles:
        data[title.text] = title.get('href')
    return data

# 이 명령어는 이 파일이 import가 아닌 python에서 직접 실행할 경우에만 아래 코드가 동작하도록 합니다.
if __name__=='__main__':
    blog_data_dict = parse_blog()
    for t, l in blog_data_dict.items():
        BlogData(title=t, link=l).save()