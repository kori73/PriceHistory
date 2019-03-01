import scrapy
from urllib.parse import urljoin, urlparse
import re

from .utility import filter_by_brands

class KadinSpider(scrapy.Spider):
    name = "kadin"
    base_url = 'https://www.trendyol.com/kadin+giyim?siralama=13&qs=search'

    def start_requests(self):
        links = filter_by_brands(self.base_url)
        start_urls = []
        stop_urls = []
        for link in links:
            p = urlparse(link) # Parse each url
            stop_url = 'https://' + p.netloc + p.path  # Obtain the stopping urls
            start_url = stop_url +'?pi={}'
            stop_urls.append(stop_url)
            start_urls.append(start_url)

        for url, stop in zip(start_urls, stop_urls):
            yield scrapy.Request(url=url.format(1), callback=self.parse, meta={'stop': stop})

    def parse(self, response):
        # If statement checks whether the final page is reached.
        # If one tries to go to page n+1 where there are n pages, response url will be the base url.
        if response.url != response.meta['stop']:
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
            yield scrapy.Request(next_page, callback=self.parse, meta=response.meta)
