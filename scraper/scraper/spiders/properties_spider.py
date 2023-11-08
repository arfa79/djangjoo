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
        "https://ws.alibaba.ir/api/v1/flights/domestic/available"
    ]

    rules = (
        Rule(
            LinkExtractor(allow=("alibaba.ir/flights")),
            callback="parse_property",
            follow=True,
        ),
    )

    def parse_property(self, response):
        property_loader = ItemLoader(item=ScraperItem(), response=response)
        property_loader.default_output_processor = TakeFirst()

        property_loader.add_css(
            "price", "span.text-6.block.mt-2[data-v-1bed6fc4][data-v-661aad36]::text"
        )
        property_loader.add_css(
            "start_location", "span[style=margin-left: 0.5rem;]::text"
        )
        property_loader.add_css(
            "landing_location", "span[style=margin-left: 0.5rem;]::text"
        )
        property_loader.add_css(
            "status", "span[data-v-661aad36]::text"
        )
        property_loader.add_css(
            "category", "h3.md:text-5.text-4.mt-6.mb-3.md:mb-4.cards-flip-item.last:mb-0::text"
        )
        property_loader.add_css(
            "airline_company", "strong.block.text-1.mt-1.md:text-2.font-medium.airline-name.text-grays-500.mx-2[data-v-68766d8c]::text"
        )
        property_loader.add_css(
            "landing_date", "strong.text-5.md:text-6::text"
        )
        property_loader.add_css(
            "flying_date", "strong.text-5.md:text-6[style=margin-left: 0.5rem;]::text"
        )        

        yield property_loader.load_item()