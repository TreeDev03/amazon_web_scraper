# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
import pymongo

from itemadapter import ItemAdapter



class AmazonPipeline(object):
    def process_item(self, item, spider):
        return item
