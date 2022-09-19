
from fake_headers import Headers
from requests import get
from bs4 import BeautifulSoup
headers = Headers(os="win", headers=True).generate()

url = 'https://habr.com/ru/all/'
keywords = ['дизайн', 'фото', 'web', 'Python']
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')
posts = soup.find_all('article')
for post in posts:
    hubs = post.find_all(class_="tm-article-snippet__hubs-item")
    hubs = [hub.text.strip(' *') for hub in hubs]
    headlines = post.find(class_="tm-article-snippet__title tm-article-snippet__title_h2")
    headlines = [headline.text for headline in headlines]
    datatime = post.find(class_="tm-article-snippet__datetime-published")
    datatime = [data.text for data in datatime]
    link = post.find(class_="tm-article-snippet__title-link").attrs['href']
    for hub in hubs:
        if hub in keywords:
            print(f' Время публикации: {datatime}, Названи:{headlines}, https://habr.com{link}')


   
   

    
    
    
   
 
