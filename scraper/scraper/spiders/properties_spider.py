from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

from scraper.scraper.items import ScraperItem


class PropertiesSpider(CrawlSpider):
    name = "properties"
    allowed_domains = ["https://www.alibaba.ir/"]
    start_urls = [
        "https://www.alibaba.ir/flights/THR-MHD?adult=1&child=0&infant=0&departing=1402-08-01"
    ]

    rules = (
        Rule(
            LinkExtractor(allow=("HouseDetails\.aspx")),
            callback="parse_property",
            follow=True,
        ),
    )

    def parse_property(self, response):
        property_loader = ItemLoader(item=ScraperItem(), response=response)
        property_loader.default_output_processor = TakeFirst()

        property_loader.add_css(
            "price", "span#ContentPlaceHolder1_DetailsFormView_Shillings::text"
        )
        property_loader.add_css(
            "start_location", "span#ContentPlaceHolder1_DetailsFormView_LocationLabel::text"
        )
        property_loader.add_css(
            "landing_location", "span#ContentPlaceHolder1_DetailsFormView_LocationLabel::text"
        )
        property_loader.add_css(
            "status", "span#ContentPlaceHolder1_DetailsFormView_StatusLabel::text"
        )
        property_loader.add_css(
            "category", "span#ContentPlaceHolder1_DetailsFormView_CategoryLabel::text"
        )
        property_loader.add_css(
            "airline_company", "span#ContentPlaceHolder1_FormView1_CompanyLabel::text"
        )
        property_loader.add_css(
            "landing_date", "span#ContentPlaceHolder1_FormView1_CompanyLabel::text"
        )
        property_loader.add_css(
            "flying_date", "span#ContentPlaceHolder1_FormView1_CompanyLabel::text"
        )        

        yield property_loader.load_item()