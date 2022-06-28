import scrapy
from ..items import AmazontutItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 3

    start_urls = ['https://www.amazon.com/computer-monitors/s?k=computer+monitors&page=2']

    def parse(self, response):

        global products
        items = AmazontutItem()

        for products in response.css('div.sg-col-inner'):
            yield {

                "name": products.css('.a-size-medium.a-text-normal').css(
                    '::text').extract(),

                "rating": products.css('a[class="a-popover-trigger a-declarative"] ::text').extract(),
                "num_of_ratings": products.css('.s-link-style .s-underline-text').css('::text').extract(),
                "price": products.css('.a-price-whole').css('::text').extract(),
                "size": products.css('.s-padding-right-small:nth-child(1) .a-text-bold ').css('::text').extract(),
                "resolution": products.css('.s-padding-right-small:nth-child(3) .a-text-bold ').css('::text').extract(),
                "refresh_rate": products.css('.s-padding-right-small:nth-child(2) .a-text-bold').css('::text').extract()
            }

        next_page = f'https://www.amazon.com/computer-monitors/s?k=computer+monitors&page={AmazonSpiderSpider.page_number}'

        if AmazonSpiderSpider.page_number < 12:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
