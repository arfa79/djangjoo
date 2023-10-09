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
            "price", "text-secondary-400"
        )
        property_loader.add_css(
            "start_location", "margin-left: 0.5rem"
        )
        property_loader.add_css(
            "landing_location", "margin-left: 0.5rem"
        )
        property_loader.add_css(
            "status", "flex flex-col text-2 mt-1 text-danger-400"
        )
        property_loader.add_css(
            "category", "a-card available-card is-disabled flex mb-3 md:mb-4 cards-flip-item last:mb-0"
        )
        property_loader.add_css(
            "airline_company", "block text-1 mt-1 md:text-2 font-medium airline-name text-grays-500 mx-2t"
        )
        property_loader.add_css(
            "landing_date", "text-5 md:text-6"
        )
        property_loader.add_css(
            "flying_date", "text-5 md:text-6"
        )        

        yield property_loader.load_item()