import scrapy
from scrapy.http import Response


class MySpider(scrapy.Spider):
    name = "MySpider"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response: Response):
        pass
