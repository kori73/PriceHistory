import scrapy
from urllib.parse import urljoin

class KadinPolarSpider(scrapy.Spider):
    name = "kadin_polar"
    base_url = 'https://www.trendyol.com/kadin+polar'

    def start_requests(self):
        urls = [
            'https://www.trendyol.com/kadin+polar?pi={}',
        ]
        for url in urls:
            yield scrapy.Request(url=url.format(1), callback=self.parse)

    def parse(self, response):
        # If statement checks whether the final page is reached.
        # If one tries to go to page n+1 where there are n pages, response url will be the base url.
        if response.url != self.base_url:
            page_num = int(response.url[-1])
            url_arg = "?pi={}".format(page_num + 1)
            for product in response.css('div.favorite'):
                yield {
                    'data-productcontentid': product.xpath('@data-productcontentid').extract(),
                    'price': product.xpath('@data-saleprice').extract(),
                    'data-productid': product.xpath('@data-productid').extract(),
                    'data-productmainid': product.xpath('@data-productmainid').extract(),
                }
            next_page = urljoin(response.url, url_arg)
            yield scrapy.Request(next_page, callback=self.parse)
