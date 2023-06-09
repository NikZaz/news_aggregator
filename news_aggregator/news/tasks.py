import re
import requests
from bs4 import BeautifulSoup as BS
from .models import News
from celery import shared_task



@shared_task
def parse_content_task():
    get_content()

@shared_task
def parse_content_bbc_task():
    get_content_bbc()


def clean_text(text):
    # Удаление лишних символов и фраз
    text = re.sub(r"\d{2}:\d{2} \d{2}.\d{2}.\d{4}", "", text)  # Удаление времени и даты
    text = re.sub(r"РИА Новости, \d{2}.\d{2}.\d{4}", "", text)  # Удаление источника и даты
    text = re.sub(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}", "", text)  # Удаление временных меток
    text = re.sub(r"html/head/meta\[@name='og:title'\]/@content", "", text)  # Удаление метаданных
    text = re.sub(r"html/head/meta\[@name='og:description'\]/@content", "", text)  # Удаление метаданных
    text = re.sub(r"https://\S+", "", text)  # Удаление ссылок
    text = re.sub(r"https?://[^\s]+", "", text)  # Удаление ссылок
    text = re.sub(r"www\.\S+", "", text)  # Удаление ссылок
    text = re.sub(r"[^\w\s.,-]", "", text)  # Удаление специальных символов, кроме запятых, точек и дефисов
    text = re.sub(r"\s+", " ", text)  # Удаление лишних пробелов

    return text.strip()


def get_content():
    url = 'https://ria.ru/world/'
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }
    resp = requests.get(url, headers=header)
    if resp.status_code == 200:
        page = BS(resp.text, "html.parser")
        div_list = page.find_all('div', attrs={'class': 'list-item'})
        for div in div_list:
            div_title = div.find('a', attrs={'class': 'list-item__title color-font-hover-only'})
            title = div_title.text
            href = div.a['href']
            div_img = div.find('a', attrs={'class': 'list-item__image'})
            div_image = div_img.find('picture')
            div_image_img = div_image.find('img', attrs={'class': 'responsive_img m-list-img'})
            image_url = div_image_img['src']

            news_url = href
            news_resp = requests.get(news_url, headers=header)
            if news_resp.status_code == 200:
                news_page = BS(news_resp.text, "html.parser")

                article_body_div = news_page.find('div',
                                                  attrs={'class': 'article__body js-mediator-article mia-analytics'})
                article_block_divs = article_body_div.find_all('div',
                                                               attrs={'class': 'article__block', 'data-type': 'text'})

                # Получение очищенного текста из нужных div
                full_text = ''
                for div in article_block_divs:
                    text = div.get_text(separator='\n')
                    full_text += text + '\n'

                # Очистка текста
                full_text = clean_text(full_text)

                # Проверка наличия новости с таким же заголовком в базе данных
                if News.objects.filter(title=title).exists():
                    continue

                news = News(title=title, url=href, image_url=image_url, full_text=full_text.strip())
                news.save()


def parse_content():
    get_content()


if __name__ == '__main__':
    parse_content()


def get_content_bbc():
    url = 'https://www.bbc.com/russian'
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }
    resp = requests.get(url, headers=header)
    if resp.status_code == 200:
        page = BS(resp.text, "html.parser")
        article_list = page.find_all('li', {'class': 'ebmt73l0 bbc-lpu9rr e13i2e3d1'})
        for article in article_list:
            href = article.a['href']
            if not href.startswith('/'):
                continue
            title = article.a.text
            image_div = article.find('div', {'class': 'bbc-1o12lo8 evlkxz0'})
            image_url = image_div.find('img', {'class': 'bbc-1uwua2r'})['src'] if image_div else None

            news_url = 'https://www.bbc.com' + href
            news_resp = requests.get(news_url, headers=header)
            if news_resp.status_code == 200:
                news_page = BS(news_resp.text, "html.parser")

                bbc_1ff36h2 = news_page.find('div', {'class': 'bbc-1ff36h2'})
                if bbc_1ff36h2 is None:
                    continue

                e1j2237y5 = bbc_1ff36h2.find('div', {'class': 'e1j2237y5 bbc-1wf62vy ebmt73l0'})
                if e1j2237y5 is None:
                    continue

                e1j2237y4 = e1j2237y5.find('div', {'class': 'e1j2237y4 bbc-irdbz7 ebmt73l0'})
                if e1j2237y4 is None:
                    continue

                main_div = e1j2237y4.find('main', {'role': 'main'})
                if main_div is None:
                    continue

                full_text = ""
                paragraphs_divs = main_div.find_all('div', {'class': 'bbc-19j92fr ebmt73l0'})
                for div in paragraphs_divs:
                    paragraphs = div.find_all('p', {'class': 'bbc-hhl7in e17g058b0'})
                    for p in paragraphs:
                        full_text += p.get_text(separator='\n')

                full_text = clean_text(full_text)

                if News.objects.filter(title=title).exists():
                    continue

                news = News(title=title, url=news_url, image_url=image_url, full_text=full_text.strip())
                news.save()



def parse_content_bbc():
    get_content_bbc()


if __name__ == '__main__':
    parse_content_bbc()
