import scrapy


class TwitterSpider(scrapy.Spider):
    name = 'twitter'
    allowed_domains = ['youtube.com']
    start_urls = [
        'https://www.youtube.com/results?search_query=reseaux+convolution']

    def parse(self, response):

        comments = response.css("#dismissible")
        print(f'Comment: {len(comments)}')
