from news_aggregator.models import News
import scrapy


class NewsSpiderSpider(scrapy.Spider):
    name = "news_spider"
    allowed_domains = ["www.belta.by"]
    start_urls = ["http://www.belta.by/"]

    def parse(self, response):
        title = response.css('h2.title::text').get()
        
        description = response.css('div.description::text').get()
        
        news_data = {
            'title' : title,
            'description' : description
        }
        
        news = News(title=title, description=description)
        news.save()

        yield news_data