import scrapy
from ..items import AmazontutItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 3

    start_urls = ['https://www.amazon.com/computer-monitors/s?k=computer+monitors&page=2']

    def parse(self, response):
        items = AmazontutItem()

        name = response.css('.a-size-medium.a-text-normal').css(
            '::text').extract()

        rating = response.css('a[class="a-popover-trigger a-declarative"] ::text').extract()
        num_of_ratings = response.css('.s-link-style .s-underline-text').css('::text').extract()
        price = response.css('.a-price-whole').css('::text').extract()
        size = response.css('.s-padding-right-small:nth-child(1) .a-text-bold ').css('::text').extract()
        resolution = response.css('.s-padding-right-small:nth-child(3) .a-text-bold ').css('::text').extract()
        refresh_rate = response.css('.s-padding-right-small:nth-child(2) .a-text-bold').css('::text').extract()

        items['name'] = name

        items['rating'] = rating
        items['num_of_ratings'] = num_of_ratings
        items['price'] = price
        items['size'] = size
        items['resolution'] = resolution
        items['refresh_rate'] = refresh_rate

        yield items

        next_page = f'https://www.amazon.com/computer-monitors/s?k=computer+monitors&page={AmazonSpiderSpider.page_number}'

        if AmazonSpiderSpider.page_number <= 12:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
