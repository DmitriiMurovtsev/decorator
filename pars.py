import re
import requests
from bs4 import BeautifulSoup


def logger(path='C:\\Users\\user\Desktop'):
    from datetime import datetime

    def _logger(func):
        def log_func(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            with open(f'{path}\\log {func.__name__}.txt', 'w') as file:
                file.write(f'Дата и время вызова функции: {start}\n'
                           f'Имя функции: {func.__name__}\n'
                           f'Аргументы функции: {args} {kwargs}\n'
                           f'Результат функции: {result}')
            return result
        return log_func
    return _logger

@logger()
def search_for_matches(links_list, key_words):
    for link in links_list:
        res = requests.get(f'https://habr.com{link}')
        soup = BeautifulSoup(res.text, 'html.parser')
        temp_list = [key for key in key_words if soup.find(text=re.compile(key))]
        if len(temp_list) > 0:
            print(f"{soup.find(class_='tm-article-snippet__datetime-published').text}, "
                  f"{soup.find(class_='tm-article-snippet__title tm-article-snippet__title_h1').text}, "
                  f"https://habr.com{link}. "
                  f"Совпадения по словам: {temp_list}"
                  )


def get_links():
    res = requests.get('https://habr.com/ru/all')
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.find_all(class_='tm-article-snippet__title tm-article-snippet__title_h2')
    links_list = [link.find('a').get('href') for link in links]
    return links_list


key_words = ['data science', 'парсинг', 'web', 'python', 'дизайн', 'фото']

search_for_matches(get_links(), key_words)
