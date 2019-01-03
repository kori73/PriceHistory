import scrapy
import re
from urllib.parse import urljoin
from urllib.parse import urlparse

class CepTelSpider(scrapy.Spider):
    name = "cep_tel"
    base_url = 'https://www.trendyol.com/telefon'

    def start_requests(self):
        urls = [
            'https://www.trendyol.com/telefon?pi={}',
        ]
        for url in urls:
            yield scrapy.Request(url=url.format(199), callback=self.parse)

    def parse(self, response):
        # If statement checks whether the final page is reached.
        # If one tries to go to page n+1 where there are n pages, response url will be the base url.
        if response.url != self.base_url:
            parsed_url = urlparse(response.url)
            page_num = int(re.search(r'\d+', parsed_url.query).group())
            new_query = "?pi={}".format(page_num + 1)
            for product in response.css('div.favorite'):
                yield {
                    'data-productcontentid': product.xpath('@data-productcontentid').extract(),
                    'price': product.xpath('@data-saleprice').extract(),
                    'data-productid': product.xpath('@data-productid').extract(),
                    'data-productmainid': product.xpath('@data-productmainid').extract(),
                }
            next_page = urljoin(response.url, new_query)
            yield scrapy.Request(next_page, callback=self.parse)
