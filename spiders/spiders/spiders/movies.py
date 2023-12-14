import scrapy


class MoviesSpider(scrapy.Spider):
    name = "movies"
    allowed_domains = ["douban.com"]
    start_urls = ["https://douban.com"]

    def parse(self, response):
        pass
