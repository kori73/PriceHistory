import scrapy
import re
from urllib.parse import urljoin
from urllib.parse import urlparse

class ElektronikSpider(scrapy.Spider):
    name = "elektronik"
    # Page 100 is called. 3 pages exist on electronics page. 100 is highly conservative.
    # However, in the future the response might be 404!
    base_url = 'https://www.trendyol.com/Butik/Liste/Elektronik?pi=100'
    temp = 'https://www.trendyol.com/?msg=Invisible'

    def start_requests(self):
        yield scrapy.Request(url=self.base_url, callback=self.gather_links)
        

    def gather_links(self, response):
        # links of the large and small images
        url_tails =  response.css('div.butik-large-image a::attr(href)').extract() + \
                     response.css('div.butik-small-image a::attr(href)').extract()

        for tail in url_tails:
            url_inter = urljoin(self.base_url, tail)
            url_complete = urljoin(url_inter, '?pi=1')
            yield scrapy.Request(url=url_complete, callback=self.product_count)

    def product_count(self, response):
        response.css('div.product-count').extract()
    def parse(self, response):
        # If statement checks whether the final page is reached.
        # If one tries to go to page n+1 where there are n pages, response url will be the base url.
        if response.url != self.temp:
            parsed_url = urlparse(response.url)
            page_num = int(re.search(r'\d+', parsed_url.query).group())
            new_query = "?pi={}".format(page_num + 1)
            for product in response.css('li.product-box'):
                yield {
                    'contentid': product.xpath('@data-id').extract(),
                    'price': product.css('div.sale-price::text').extract(),
                    'id': product.css('div.product a::attr(productid)').extract(),
                    'mainid': product.css('div.product a::attr(productmainid)').extract(),
                }
            next_page = urljoin(response.url, new_query)
            yield scrapy.Request(next_page, callback=self.parse)
