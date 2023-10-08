from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
import re
from scraper.scraper.items import ScraperItem


class PropertiesSpider(CrawlSpider):
    name = "properties"
    allowed_domains = ["https://www.alibaba.ir/"]
    start_urls = [
        "https://www.alibaba.ir/flights/THR-MHD?adult=1&child=0&infant=0&departing=1402-08-01"
    ]

    rules = (
        Rule(
            LinkExtractor(allow=("")),
            callback="parse_property",
            follow=True,
        ),
    )

    def parse_property(self, response):
        property_loader = ItemLoader(item=ScraperItem(), response=response)
        property_loader.default_output_processor = TakeFirst()

        property_loader.add_css(
            "price", "available-card__content"
        )
        property_loader.add_css(
            "start_location", "available-card__content"
        )
        property_loader.add_css(
            "landing_location", "available-card__content"
        )
        property_loader.add_css(
            "status", "available-card__content"
        )
        property_loader.add_css(
            "category", "available-card__content"
        )
        property_loader.add_css(
            "airline_company", "available-card__content"
        )
        property_loader.add_css(
            "landing_date", "available-card__content"
        )
        property_loader.add_css(
            "flying_date", "available-card__content"
        )        

        yield property_loader.load_item()