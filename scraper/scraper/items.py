# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from properties.models import Property
import scrapy


class ScraperItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = Property
SPIDER_MODULES = ['scraper.scraper.spiders']
NEWSPIDER_MODULE = 'scraper.scraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# replace this with your actual user-agent value

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# update the pipelines to this
ITEM_PIPELINES = {
   'scraper.scraper.pipelines.PropertyStatusPipeline': 100,
   'scraper.scraper.pipelines.PropertyPricePipeline': 200,
   'scraper.scraper.pipelines.ConvertNumPipeline': 300,
   'scraper.scraper.pipelines.ScraperPipeline': 400,
}