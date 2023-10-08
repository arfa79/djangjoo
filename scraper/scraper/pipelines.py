# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from word2number import w2n

class ScraperPipeline(object):
     """
    Saves Item to the database
    """
     def process_item(self, item, spider):
        item.save()
        return item

class PropertyStatusPipeline(object):
    """
    Replace text for item status i.e For Rent will be replaced with Rent.
    """
    def process_item(self, item, spider):
        if item.get('status'):
            item['status'] = item['status'].replace('For ', '')
            return item
class PropertyPricePipeline(object):
    """
    Removes signs from the price value. i.e replaces 10000/= with 10000
    """
    def process_item(self, item, spider):
        if item.get('price'):
            item['price'] = item['price'].replace('/=', '')
            return item
