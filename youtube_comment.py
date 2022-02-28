import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class YoutubeCommentSpider(CrawlSpider):
    name = 'youtube_comment'
    allowed_domains = ['jumia.com.tn']
    start_urls = [
        'https://www.jumia.com.tn'
    ]

    commentaitre_detail = LinkExtractor(restrict_css='article > a')

    commenttairres = Rule(
        commentaitre_detail,
        callback='parse_item',
        follow=False
    ),

    rules = (
        commenttairres
    )

    def parse_item(self, response):
        yield {
            'titre': response.css("h1.-fs20::text").get(),
            'prix': response.css('span.-b::text').get(),
            'pourcentage': response.css('span.tag::text').get(),
            'image': response.css('a.itm>img').attrib['data-src'],
            'temps_restant': response.css('time::text').get(),
            'lien': response.url
        }
