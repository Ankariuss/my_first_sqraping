import requests
from bs4 import BeautifulSoup
import time

# Загрузка картинки в указаную папку
def dowanload(url):
    rest = requests.get(url, stream=True)
    r = open('E:\\Python\\Практика\\Практика парсинга\\image\\' + url.split('/')[-1],'wb')
    for value in rest.iter_content(1024*1024):
        r.write(value)
    r.close()

#Парсим данные с сайта
def get_url():
    
    for count in range(1,7):
        
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
        respouns = requests.get(url)
        soup = BeautifulSoup(respouns.text, 'lxml')
        data = soup.find_all('div', class_ = "w-full rounded border")

        for i in data:
            card_url = 'https://scrapingclub.com' +  i.find('a').get('href')
            yield card_url
        
def array():
    for card_url in get_url():
        
        respouns = requests.get(card_url)
        soup = BeautifulSoup(respouns.text, 'lxml')
        data = soup.find('div', class_ = "my-8 w-full rounded border")
        
        title = data.find('h3', class_ = 'card-title').text
        prise = data.find('h4', class_ = 'my-4 card-price').text
        img_text = data.find('p', class_ = 'card-description').text
        img_url = 'https://scrapingclub.com' + data.find('img').get('src')
        dowanload(img_url)
        yield title, prise, img_text, img_url
